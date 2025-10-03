#!/bin/bash
# VS Code Readiness Checker
# Simple script to check if VS Code and extensions are ready

echo "🔍 VS Code Readiness Checker"
echo "=========================================="

# Check if code command is available
if command -v code > /dev/null 2>&1; then
    echo "✅ VS Code CLI available"
else
    echo "❌ VS Code CLI not available"
fi

# Check VS Code server processes
if pgrep -f "vscode-server" > /dev/null 2>&1; then
    echo "✅ VS Code server processes running:"
    pgrep -f "vscode-server" | head -3 | while read pid; do
        ps -p $pid -o pid,cmd --no-headers | cut -c1-80
    done
else
    echo "❌ No VS Code server processes found"
fi

# Check extension processes
if pgrep -f "vscode-server.*extensionProcess" > /dev/null 2>&1; then
    echo "⚙️  Extension processes found:"
    pgrep -f "vscode-server.*extensionProcess" | wc -l | xargs echo "   Count:"
    
    # Check if actively installing
    if pgrep -f "vscode-server.*install" > /dev/null 2>&1; then
        echo "📦 Extensions currently installing"
    else
        echo "✅ Extension processes running (not installing)"
    fi
else
    echo "ℹ️  No extension processes found (may be ready or not started)"
fi

# Check VS Code logs
if [ -d "$HOME/.vscode-server" ]; then
    echo "📄 VS Code server directory exists"
    
    # Check for recent logs
    recent_logs=$(find "$HOME/.vscode-server/logs" -name "*.log" -mmin -5 2>/dev/null | wc -l)
    echo "   Recent log files (last 5 min): $recent_logs"
    
    # Check for extension activity in logs
    if find "$HOME/.vscode-server/logs" -name "*.log" -mmin -2 2>/dev/null | xargs grep -l "Installing extension\|Activating extension" 2>/dev/null | head -1 > /dev/null; then
        echo "📦 Recent extension installation/activation activity detected"
    else
        echo "✅ No recent extension installation activity"
    fi
else
    echo "❌ VS Code server directory not found"
fi

# Check node extension processes
node_ext_processes=$(pgrep -f "node.*extensions" | wc -l)
if [ "$node_ext_processes" -gt 0 ]; then
    echo "⚙️  Node extension processes: $node_ext_processes"
else
    echo "✅ No Node extension processes running"
fi

echo "=========================================="

# Overall assessment
ready=true

if ! command -v code > /dev/null 2>&1; then
    ready=false
fi

if pgrep -f "vscode-server.*install" > /dev/null 2>&1; then
    ready=false
fi

if find "$HOME/.vscode-server/logs" -name "*.log" -mmin -1 2>/dev/null | xargs grep -l "Installing extension" 2>/dev/null | head -1 > /dev/null; then
    ready=false
fi

if [ "$ready" = true ]; then
    echo "✅ VS Code appears to be READY for auto-sync"
    exit 0
else
    echo "⏳ VS Code is still INITIALIZING - wait before running auto-sync"
    exit 1
fi