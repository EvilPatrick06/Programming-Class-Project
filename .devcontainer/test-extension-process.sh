#!/bin/bash
# Test Extension Installation Process
# Simulates what happens in a new container

echo "🧪 Testing Extension Installation Process"
echo "=" * 50

echo "📊 Current Status:"
echo "  Extensions installed: $(code --list-extensions 2>/dev/null | wc -l)"
echo "  Python extension: $(code --list-extensions 2>/dev/null | grep -c 'ms-python.python')"
echo "  Pylance extension: $(code --list-extensions 2>/dev/null | grep -c 'ms-python.vscode-pylance')"

echo ""
echo "🔄 Simulating new container setup..."

# Remove marker file to simulate fresh container
rm -f /tmp/.vscode-extensions-installed
rm -f /tmp/extension-installer.log

echo "🚀 Running auto-installer (as it would in new container)..."
echo ""

# Run the auto-installer
if /workspaces/Programming-Class-Project/.devcontainer/auto-install-extensions.sh; then
    echo ""
    echo "✅ Auto-installer completed successfully!"
    
    echo ""
    echo "📋 Installation log:"
    if [ -f "/tmp/extension-installer.log" ]; then
        echo "  📁 Log location: /tmp/extension-installer.log"
        echo "  📝 Last 10 lines:"
        tail -10 /tmp/extension-installer.log | sed 's/^/    /'
    fi
    
    echo ""
    echo "🎯 Verification:"
    echo "  Marker file exists: $([ -f '/tmp/.vscode-extensions-installed' ] && echo 'Yes' || echo 'No')"
    echo "  Required extensions present:"
    if code --list-extensions 2>/dev/null | grep -q 'ms-python.python'; then
        echo "    ✅ ms-python.python"
    else
        echo "    ❌ ms-python.python"
    fi
    if code --list-extensions 2>/dev/null | grep -q 'ms-python.vscode-pylance'; then
        echo "    ✅ ms-python.vscode-pylance"
    else
        echo "    ❌ ms-python.vscode-pylance"
    fi
    
else
    echo "❌ Auto-installer failed!"
fi

echo ""
echo "💡 In a new container, this process will:"
echo "   1. Run automatically after container startup (20s delay)"
echo "   2. Install missing extensions from devcontainer.json"
echo "   3. Create marker file to prevent re-running"
echo "   4. Log all activity to /tmp/extension-installer.log"
echo ""
echo "🎉 No more manual clicking on Extensions tab needed!"
echo "=" * 50