#!/bin/bash
# Debug script to help diagnose container startup timing issues

echo "🔍 Container Startup Debug Information"
echo "=" * 50
echo "Timestamp: $(date)"
echo ""

echo "📊 Container Environment:"
echo "  - CODESPACES_CONTAINER_SETUP: ${CODESPACES_CONTAINER_SETUP:-not set}"
echo "  - DEVCONTAINER_CONFIG: ${DEVCONTAINER_CONFIG:-not set}"
echo "  - Container check (/.dockerenv): $([ -f "/.dockerenv" ] && echo "exists" || echo "not found")"
echo ""

echo "📦 VS Code Extension Status:"
if command -v code > /dev/null 2>&1; then
    echo "  - code command: available"
    echo "  - Installed extensions:"
    code --list-extensions 2>/dev/null | sed 's/^/    /'
else
    echo "  - code command: not available"
fi
echo ""

echo "🏗️  Container Setup Status:"
if [ -d "/tmp/container-setup" ]; then
    echo "  - Setup directory: exists"
    echo "  - Setup files:"
    ls -la /tmp/container-setup/ 2>/dev/null | sed 's/^/    /'
    
    if [ -f "/tmp/container-setup/status" ]; then
        echo "  - Current status: $(cat /tmp/container-setup/status)"
    fi
    
    if [ -f "/tmp/container-setup/SETUP-COMPLETE" ]; then
        echo "  - Setup completed: YES"
        if [ -f "/tmp/container-setup/completion-time" ]; then
            echo "  - Completion time: $(cat /tmp/container-setup/completion-time)"
        fi
    else
        echo "  - Setup completed: NO"
    fi
else
    echo "  - Setup directory: does not exist"
fi
echo ""

echo "🔄 Running Processes (setup related):"
echo "  - complete-setup.sh processes:"
pgrep -f "complete-setup.sh" | wc -l | sed 's/^/    Count: /'
pgrep -f "complete-setup.sh" | sed 's/^/    PID: /' 2>/dev/null || echo "    None running"

echo "  - VS Code server processes:"
pgrep -f "vscode-server" | wc -l | sed 's/^/    Count: /'

echo "  - Extension processes:"
pgrep -f "extensionProcess\|node.*extensions" | wc -l | sed 's/^/    Count: /'
echo ""

echo "📁 Workspace Status:" 
echo "  - Current directory: $(pwd)"
echo "  - Git status: $([ -d ".git" ] && echo "Git repository" || echo "No git repository")"
echo "  - Python version: $(python3 --version 2>/dev/null || echo "Python not available")"
echo ""

echo "⏰ Timing Recommendations:"
echo "  - If extensions not ready: wait 30-60s more"
echo "  - If setup incomplete: wait for complete-setup.sh to finish"
echo "  - If no setup directory: container setup may have been skipped"
echo ""
echo "=" * 50