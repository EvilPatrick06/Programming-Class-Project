#!/bin/bash
# Auto Extension Installer for GitHub Codespaces
# Runs automatically when VS Code starts to ensure extensions are installed

EXTENSION_INSTALLER_LOG="/tmp/extension-installer.log"
EXTENSION_MARKER="/tmp/.vscode-extensions-installed"

# Redirect all output to log file
exec 1> >(tee -a "$EXTENSION_INSTALLER_LOG")
exec 2> >(tee -a "$EXTENSION_INSTALLER_LOG" >&2)

echo "=================================="
echo "VS Code Extension Auto-Installer"
echo "Started: $(date)"
echo "=================================="

# Check if extensions are already installed by this script
if [ -f "$EXTENSION_MARKER" ]; then
    echo "✅ Extensions already processed by auto-installer"
    echo "   Marker file: $EXTENSION_MARKER"
    echo "   Created: $(stat -c %y "$EXTENSION_MARKER" 2>/dev/null || echo 'unknown')"
    exit 0
fi

# Function to wait for VS Code to be responsive
wait_for_vscode() {
    local max_attempts=20
    local attempt=0
    
    echo "⏳ Waiting for VS Code to be responsive..."
    
    while [ $attempt -lt $max_attempts ]; do
        if timeout 10 code --version >/dev/null 2>&1; then
            echo "✅ VS Code is responsive (attempt $((attempt + 1)))"
            return 0
        fi
        
        echo "🔄 VS Code not ready yet (attempt $((attempt + 1))/$max_attempts)"
        sleep 3
        attempt=$((attempt + 1))
    done
    
    echo "❌ VS Code did not become responsive within $((max_attempts * 3)) seconds"
    return 1
}

# Function to install missing extensions
install_missing_extensions() {
    local required_extensions=(
        "ms-python.python"
        "ms-python.vscode-pylance"
    )
    
    echo "🔍 Checking for missing extensions..."
    
    # Get currently installed extensions
    local installed_extensions
    if ! installed_extensions=$(timeout 15 code --list-extensions 2>/dev/null); then
        echo "❌ Could not query installed extensions"
        return 1
    fi
    
    echo "📦 Currently installed extensions:"
    echo "$installed_extensions" | sed 's/^/  /'
    
    local missing_extensions=()
    local install_needed=false
    
    # Check each required extension
    for ext in "${required_extensions[@]}"; do
        if echo "$installed_extensions" | grep -q "^$ext$"; then
            echo "✅ Found: $ext"
        else
            echo "❌ Missing: $ext"
            missing_extensions+=("$ext")
            install_needed=true
        fi
    done
    
    # Install missing extensions
    if [ "$install_needed" = true ]; then
        echo ""
        echo "🚀 Installing ${#missing_extensions[@]} missing extensions..."
        
        for ext in "${missing_extensions[@]}"; do
            echo "📥 Installing: $ext"
            if timeout 90 code --install-extension "$ext" --force; then
                echo "✅ Successfully installed: $ext"
            else
                echo "❌ Failed to install: $ext"
            fi
        done
        
        # Verify installation
        echo ""
        echo "🔍 Verifying installation..."
        sleep 2
        
        if updated_extensions=$(timeout 15 code --list-extensions 2>/dev/null); then
            echo "📦 Updated extension list:"
            echo "$updated_extensions" | grep -E "(python|pylance)" | sed 's/^/  ✅ /'
        fi
        
    else
        echo "🎉 All required extensions are already installed!"
    fi
}

# Main execution
main() {
    if wait_for_vscode; then
        echo ""
        install_missing_extensions
        
        # Create marker file to prevent re-running
        echo "$(date)" > "$EXTENSION_MARKER"
        echo ""
        echo "✅ Extension auto-installer completed successfully"
        echo "   Log file: $EXTENSION_INSTALLER_LOG"
        echo "   Marker file: $EXTENSION_MARKER"
        
    else
        echo "❌ Could not connect to VS Code - extensions may not be installed"
        return 1
    fi
}

# Run main function
main

echo "=================================="
echo "Completed: $(date)"
echo "=================================="