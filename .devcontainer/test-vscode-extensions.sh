#!/bin/bash
# Test VS Code Extension Installation
# Helps diagnose extension installation issues

echo "🧪 VS Code Extension Installation Test"
echo "=" * 50

echo "📊 Current VS Code Status:"
if command -v code > /dev/null 2>&1; then
    echo "  ✅ VS Code CLI available"
    if timeout 5 code --version > /dev/null 2>&1; then
        echo "  ✅ VS Code responds to commands"
        code --version | sed 's/^/    /'
    else
        echo "  ❌ VS Code not responding to commands"
    fi
else
    echo "  ❌ VS Code CLI not available"
fi

echo ""
echo "📦 Extension Status:"
if command -v code > /dev/null 2>&1 && timeout 10 code --list-extensions > /dev/null 2>&1; then
    echo "  ✅ Can query extensions"
    echo "  📋 Currently installed extensions:"
    code --list-extensions | sed 's/^/    /'
    
    echo ""
    echo "  🎯 Target extensions from devcontainer.json:"
    echo "    ms-python.python"
    echo "    ms-python.vscode-pylance"
    
    echo ""
    echo "  📈 Installation status:"
    if code --list-extensions | grep -q "ms-python.python"; then
        echo "    ✅ Python extension: Installed"
    else
        echo "    ❌ Python extension: Missing"
    fi
    
    if code --list-extensions | grep -q "ms-python.vscode-pylance"; then
        echo "    ✅ Pylance extension: Installed"
    else
        echo "    ❌ Pylance extension: Missing"
    fi
else
    echo "  ❌ Cannot query extensions (VS Code may still be starting)"
fi

echo ""
echo "🔍 Process Diagnostics:"
echo "  🖥️  VS Code processes:"
vscode_processes=$(pgrep -f "vscode-server" | wc -l)
echo "    Count: $vscode_processes"

echo "  🔧 Extension processes:"
ext_processes=$(pgrep -f "extensionProcess\|extension.*host" | wc -l)
echo "    Count: $ext_processes"

echo ""
echo "💡 Troubleshooting Tips:"
echo "  1. If extensions are missing:"
echo "     - Wait 2-3 minutes after container creation"
echo "     - VS Code installs extensions automatically from devcontainer.json"
echo "     - Check Extensions tab in VS Code sidebar"
echo ""
echo "  2. If VS Code is slow:"
echo "     - This can happen during initial container setup"
echo "     - Extension installation runs in background"
echo "     - Performance improves once setup completes"
echo ""
echo "  3. Manual extension installation:"
echo "     - Open Extensions tab (Ctrl+Shift+X)"
echo "     - Search for 'Python' and install ms-python.python"
echo "     - Pylance should install automatically with Python extension"
echo ""
echo "=" * 50