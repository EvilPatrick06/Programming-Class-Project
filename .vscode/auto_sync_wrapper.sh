#!/bin/bash
# VS Code Auto-Sync Wrapper
# Ensures container setup completes before running auto-sync

echo "🚀 VS Code Auto-Sync Wrapper Starting..."
echo "💡 This task waits for VS Code extensions and container setup to complete"
echo "   before running auto-sync to avoid conflicts during initialization."
echo ""

# Show debug information if debug script is available
if [ -f ".devcontainer/debug-container-startup.sh" ]; then
    echo "🔍 Debug Information:"
    bash .devcontainer/debug-container-startup.sh
    echo ""
fi

# Function to check if container setup is running or completed
check_container_setup() {
    # Check if setup is currently running
    if pgrep -f "complete-setup.sh" > /dev/null; then
        return 1  # Setup is running
    fi
    
    # Check if setup completed successfully
    if [ -f "/tmp/container-setup/SETUP-COMPLETE" ]; then
        return 0  # Setup completed
    fi
    
    # Check if setup never started (no setup directory)
    if [ ! -d "/tmp/container-setup" ]; then
        return 0  # No setup running, can proceed
    fi
    
    return 1  # Setup directory exists but not complete, assume running
}

# Function to check if VS Code extensions are still installing
check_vscode_extensions() {
    # Use the dedicated readiness checker script if available
    if [ -f ".vscode/check_vscode_ready.sh" ]; then
        if bash .vscode/check_vscode_ready.sh > /dev/null 2>&1; then
            return 0  # Ready
        else
            return 1  # Not ready
        fi
    fi
    
    # Fallback to manual checks if script not available
    # Check if code command is available
    if ! command -v code > /dev/null 2>&1; then
        return 1  # Code not available, assume still setting up
    fi
    
    # Wait for essential extensions to be active
    # Check if VS Code is responsive (but don't be too strict about extensions)
    if command -v code > /dev/null 2>&1; then
        # Try to check if code command works, but don't timeout aggressively
        if timeout 5 code --version > /dev/null 2>&1; then
            # VS Code is working, that's enough for auto-sync to proceed
            # Extensions will install naturally - don't block on them
            echo "VS Code is responsive - proceeding"
        else
            return 1  # VS Code not responding
        fi
    else
        return 1  # Code command not available
    fi
    
    # Check for VS Code server processes that indicate extension installation
    if pgrep -f "vscode-server.*extensionProcess" > /dev/null 2>&1; then
        # Extension process is running, check if it's actively installing
        if pgrep -f "vscode-server.*install" > /dev/null 2>&1; then
            return 1  # Extensions still installing
        fi
    fi
    
    # Check VS Code logs for recent extension installation activity
    if [ -d "$HOME/.vscode-server" ]; then
        # Look for very recent extension installation logs (last 1 minute)
        recent_logs=$(find "$HOME/.vscode-server/logs" -name "*.log" -mmin -1 2>/dev/null | head -3)
        if [ -n "$recent_logs" ]; then
            # Check if any logs mention extension installation in the last 60 seconds
            if echo "$recent_logs" | xargs grep -l "Installing extension\|Activating extension" 2>/dev/null | head -1 > /dev/null; then
                return 1  # Extensions still being installed/activated
            fi
        fi
    fi
    
    # Check if there are any VS Code extension management processes
    if pgrep -f "node.*extensions" > /dev/null 2>&1; then
        return 1  # Extension processes still running
    fi
    
    return 0  # Extensions appear to be done
}

# Function to wait for VS Code to be ready
wait_for_vscode_ready() {
    local max_wait=120  # 2 minutes - reduced since we're less strict
    local waited=0
    
    echo "⏳ Waiting for VS Code to be ready (extensions will install naturally)..."
    
    while [ $waited -lt $max_wait ]; do
        if check_vscode_extensions; then
            echo "✅ VS Code appears to be ready"
            return 0
        else
            echo "� VS Code still initializing... (${waited}s / ${max_wait}s)"
            sleep 10  # Check every 10 seconds
            waited=$((waited + 10))
        fi
    done
    
    echo "⚠️  VS Code did not respond within ${max_wait} seconds"
    echo "   Proceeding anyway - VS Code and extensions will continue loading"
    return 1
}

# Wait for container setup to complete
echo "⏳ Checking container setup status..."
max_wait=300  # 5 minutes
waited=0

while [ $waited -lt $max_wait ]; do
    if check_container_setup; then
        if [ -f "/tmp/container-setup/SETUP-COMPLETE" ]; then
            completion_time=$(cat /tmp/container-setup/completion-time 2>/dev/null || echo "recently")
            echo "✅ Container setup completed at: $completion_time"
        else
            echo "✅ No container setup detected"
        fi
        break
    else
        # Show current status if available
        if [ -f "/tmp/container-setup/status" ]; then
            status=$(cat /tmp/container-setup/status 2>/dev/null || echo "In progress")
            echo "📊 Container setup status: $status"
        else
            echo "⏳ Container setup in progress..."
        fi
        
        # Wait and increment counter
        sleep 10
        waited=$((waited + 10))
        echo "   Waited ${waited}s / ${max_wait}s"
    fi
done

if [ $waited -ge $max_wait ]; then
    echo "⚠️  Container setup did not complete within ${max_wait} seconds"
    echo "   Proceeding anyway..."
else
    echo "🚀 Container setup complete!"
fi

# Wait for VS Code extensions to finish installing
wait_for_vscode_ready

# Now run the actual auto-sync script
echo ""
echo "=" * 60
echo "🚀 Starting VS Code Auto-Sync..."

# Set non-interactive mode for auto-sync during startup
export AUTO_SYNC_NON_INTERACTIVE=true

python3 .vscode/auto_sync.py

echo "=" * 60
echo "✅ VS Code Auto-Sync Wrapper Complete!"