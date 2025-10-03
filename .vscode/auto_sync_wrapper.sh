#!/bin/bash
# VS Code Auto-Sync Wrapper
# Ensures container setup completes before running auto-sync

echo "🚀 VS Code Auto-Sync Wrapper Starting..."

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
            echo "✅ No container setup detected - proceeding with VS Code auto-sync"
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
    echo "   Proceeding with VS Code auto-sync anyway..."
else
    echo "🚀 Container setup complete - starting VS Code auto-sync..."
fi

# Now run the actual auto-sync script
echo ""
echo "=" * 60
echo "🚀 Starting VS Code Auto-Sync..."

# Set non-interactive mode for auto-sync during startup
export AUTO_SYNC_NON_INTERACTIVE=true

python3 .vscode/auto_sync.py

echo "=" * 60
echo "✅ VS Code Auto-Sync Wrapper Complete!"