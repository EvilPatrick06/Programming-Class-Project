#!/bin/bash
# Complete Container Setup Script
# Handles Ubuntu updates, extensions, and creates completion flag

echo "🚀         echo "📅 Scheduling GitHub environment setup for after extension installation..."
        # Create a delayed setup script that runs after extensions are installed
        cat > /tmp/delayed-terminal-setup.sh << 'EOF'
#!/bin/bash
# Wait for extensions to be installed, then setup terminal prompt
sleep 45  # Give VS Code and extensions time to fully initialize
if [ -f "/workspaces/Programming-Class-Project/.devcontainer/setup-terminal-prompt.sh" ]; then
    bash /workspaces/Programming-Class-Project/.devcontainer/setup-terminal-prompt.sh --container-init
fi
EOFomplete Container Setup..."
echo "=" * 60

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Create setup status directory
mkdir -p /tmp/container-setup

# Function to update status
update_status() {
    echo "$1" > "/tmp/container-setup/status"
    echo -e "${BLUE}[SETUP STATUS] $1${NC}"
}

# Function to mark completion
mark_completed() {
    local component="$1"
    touch "/tmp/container-setup/${component}-complete"
    echo -e "${GREEN}✅ $component completed${NC}"
}

# Function to check if running in container setup context
is_container_setup() {
    [ "$CODESPACES_CONTAINER_SETUP" = "true" ] || [ -n "$DEVCONTAINER_CONFIG" ] || [ -f "/.dockerenv" ]
}

# Only run full setup during actual container creation/start
if is_container_setup; then
    update_status "Starting Ubuntu system updates"
    
    echo -e "${BLUE}🐧 UBUNTU SYSTEM UPDATES${NC}"
    echo "=" * 40
    
    # Update package lists
    echo "📦 Updating package lists..."
    if apt-get update > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Package lists updated${NC}"
    else
        echo -e "${YELLOW}⚠️  Package list update had warnings${NC}"
    fi
    
    # Check for upgrades
    echo "🔍 Checking for available upgrades..."
    UPGRADE_COUNT=$(apt list --upgradable 2>/dev/null | grep -c upgradable || echo "0")
    
    if [ "$UPGRADE_COUNT" -gt 0 ]; then
        echo -e "${YELLOW}📦 Found $UPGRADE_COUNT package updates available${NC}"
        echo "🚀 Installing system updates (non-interactive)..."
        
        # Install updates non-interactively during container setup
        export DEBIAN_FRONTEND=noninteractive
        if apt-get upgrade -y > /dev/null 2>&1; then
            echo -e "${GREEN}✅ System packages updated successfully${NC}"
        else
            echo -e "${YELLOW}⚠️  Some packages may have had issues${NC}"
        fi
        
        # Clean up
        echo "🧹 Cleaning up package cache..."
        apt-get autoremove -y > /dev/null 2>&1
        apt-get autoclean > /dev/null 2>&1
        
    else
        echo -e "${GREEN}✅ System packages are already up to date${NC}"
    fi
    
    mark_completed "ubuntu-updates"
    update_status "Ubuntu updates completed, starting repository sync"
    
    # Run repository sync
    echo -e "${BLUE}📂 REPOSITORY SYNC${NC}"
    echo "=" * 30
    
    if [ -f ".devcontainer/auto-sync-branches.sh" ]; then
        bash .devcontainer/auto-sync-branches.sh
    else
        echo -e "${YELLOW}⚠️  Repository sync script not found${NC}"
    fi
    
    mark_completed "repo-sync"
    update_status "Ensuring VS Code extensions are installed"
    
    # Force VS Code extension installation
    echo -e "${BLUE}🧩 VS CODE EXTENSION INSTALLATION${NC}"
    echo "=" * 45
    
    if [ -f ".devcontainer/auto-install-extensions.sh" ]; then
        echo "🔧 Starting automatic VS Code extension installation..."
        # Create a delayed extension installation script with better timing
        cat > /tmp/delayed-extension-install.sh << 'EOF'
#!/bin/bash
# Wait for VS Code to be ready, then auto-install extensions
sleep 20  # Give VS Code server time to fully start
if [ -f "/workspaces/Programming-Class-Project/.devcontainer/auto-install-extensions.sh" ]; then
    bash /workspaces/Programming-Class-Project/.devcontainer/auto-install-extensions.sh
fi
EOF
        chmod +x /tmp/delayed-extension-install.sh
        # Run in background so it doesn't block container startup
        nohup /tmp/delayed-extension-install.sh &
        echo -e "${GREEN}✅ Automatic extension installation scheduled${NC}"
        echo -e "${BLUE}📋 Extensions will be installed automatically in background${NC}"
        echo -e "${BLUE}📝 Check log: /tmp/extension-installer.log${NC}"
    else
        echo -e "${YELLOW}⚠️  Auto extension installer not found${NC}"
    fi
    
    mark_completed "extensions"
    update_status "Setting up terminal prompt after extension installation"
    
    # Schedule terminal prompt setup to run after VS Code is fully ready
    echo -e "${BLUE}🖥️  TERMINAL PROMPT SETUP${NC}"
    echo "=" * 40
    
    if [ -f ".devcontainer/setup-terminal-prompt.sh" ]; then
        echo "� Scheduling GitHub environment setup for after VS Code initialization..."
        # Create a delayed setup script that runs after VS Code is ready
        cat > /tmp/delayed-terminal-setup.sh << 'EOF'
#!/bin/bash
# Wait for VS Code to be fully ready, then setup terminal prompt
sleep 30  # Give VS Code time to fully initialize
if [ -f "/workspaces/Programming-Class-Project/.devcontainer/setup-terminal-prompt.sh" ]; then
    bash /workspaces/Programming-Class-Project/.devcontainer/setup-terminal-prompt.sh --container-init
fi
EOF
        chmod +x /tmp/delayed-terminal-setup.sh
        # Run in background so it doesn't block container startup
        nohup /tmp/delayed-terminal-setup.sh > /tmp/terminal-setup.log 2>&1 &
        echo -e "${GREEN}✅ Terminal prompt setup scheduled for background execution${NC}"
    else
        echo -e "${YELLOW}⚠️  Terminal prompt setup script not found${NC}"
    fi
    
    mark_completed "terminal-prompt"
    update_status "Container setup completed successfully"
    
    # Create final completion marker with timestamp
    echo "$(date '+%Y-%m-%d %H:%M:%S')" > /tmp/container-setup/completion-time
    touch /tmp/container-setup/SETUP-COMPLETE
    update_status "All container setup operations completed successfully"
    
    echo ""
    echo -e "${GREEN}🎉 CONTAINER SETUP COMPLETE!${NC}"
    echo "=" * 60
    echo -e "${GREEN}✅ Ubuntu updates: Complete${NC}"
    echo -e "${GREEN}✅ Repository sync: Complete${NC}"
    echo -e "${GREEN}✅ VS Code extensions: Force installation scheduled${NC}"
    echo -e "${GREEN}✅ Terminal prompt: Scheduled for background setup${NC}"
    echo -e "${GREEN}✅ Completion marker: /tmp/container-setup/SETUP-COMPLETE${NC}"
    echo "=" * 60
    echo -e "${BLUE}🚀 VS Code auto-sync task can now safely proceed${NC}"
    echo -e "${BLUE}📁 Setup status directory: /tmp/container-setup/${NC}"
    echo ""
    
    # List all completion markers for debugging
    echo -e "${BLUE}🔍 Completion markers created:${NC}"
    ls -la /tmp/container-setup/
    
else
    echo -e "${YELLOW}⚠️  Not in container setup context - skipping full setup${NC}"
    echo -e "${BLUE}💡 This script should run during container creation/start${NC}"
fi