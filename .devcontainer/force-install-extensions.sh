#!/bin/bash
# Force VS Code Extension Installation
# Ensures extensions from devcontainer.json are installed automatically

echo "🔧 Force VS Code Extension Installation"
echo "=" * 45

# Wait for VS Code server to be ready
wait_for_vscode_server() {
    local max_wait=60
    local waited=0
    
    echo "⏳ Waiting for VS Code server to be ready..."
    
    while [ $waited -lt $max_wait ]; do
        if pgrep -f "server-main.js" > /dev/null 2>&1; then
            echo "✅ VS Code server is running"
            return 0
        fi
        
        echo "🔄 Waiting for VS Code server... (${waited}s/${max_wait}s)"
        sleep 5
        waited=$((waited + 5))
    done
    
    echo "⚠️  VS Code server not detected within ${max_wait}s"
    return 1
}

# Install extensions from devcontainer.json
install_extensions() {
    local extensions=(
        "ms-python.python"
        "ms-python.vscode-pylance"
    )
    
    echo "📦 Installing extensions from devcontainer.json..."
    
    for ext in "${extensions[@]}"; do
        echo "🔧 Installing: $ext"
        
        # Check if already installed
        if code --list-extensions 2>/dev/null | grep -q "^$ext$"; then
            echo "  ✅ Already installed: $ext"
        else
            echo "  📥 Installing: $ext"
            if timeout 60 code --install-extension "$ext" --force; then
                echo "  ✅ Successfully installed: $ext"
            else
                echo "  ❌ Failed to install: $ext"
            fi
        fi
    done
}

# Main execution
main() {
    # Wait for VS Code server
    if wait_for_vscode_server; then
        # Give it a moment to fully initialize
        echo "⏳ Giving VS Code server time to initialize..."
        sleep 10
        
        # Install extensions
        install_extensions
        
        echo ""
        echo "🎉 Extension installation complete!"
        echo "📋 Final extension list:"
        code --list-extensions 2>/dev/null | grep -E "(python|pylance)" || echo "  No Python extensions found"
        
    else
        echo "❌ Could not connect to VS Code server"
        return 1
    fi
}

# Only run if called directly or with --force flag
if [ "${BASH_SOURCE[0]}" = "${0}" ] || [ "$1" = "--force" ]; then
    main "$@"
else
    echo "💡 This script should be called directly or with --force flag"
fi