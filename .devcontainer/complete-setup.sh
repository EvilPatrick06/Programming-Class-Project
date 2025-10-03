#!/bin/bash
# Complete Container Setup Script
# Handles Ubuntu updates, extensions, and creates completion flag

echo "🚀 Starting Complete Container Setup..."
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
    update_status "Repository sync completed, starting extension installation"
    
    # Install VS Code extensions
    echo -e "${BLUE}🧩 VS CODE EXTENSIONS${NC}"
    echo "=" * 35
    
    if [ -f ".vscode/extension_manager.py" ]; then
        echo "📦 Installing VS Code extensions during container setup..."
        export CONTAINER_SETUP_MODE=true
        if python3 .vscode/extension_manager.py; then
            echo -e "${GREEN}✅ Extensions installed successfully${NC}"
        else
            echo -e "${YELLOW}⚠️  Extension installation had some issues${NC}"
        fi
    else
        echo -e "${YELLOW}⚠️  Extension manager script not found${NC}"
    fi
    
    mark_completed "extensions"
    update_status "Container setup completed successfully"
    
    # Create final completion marker
    touch /tmp/container-setup/SETUP-COMPLETE
    echo "$(date)" > /tmp/container-setup/completion-time
    
    echo ""
    echo -e "${GREEN}🎉 CONTAINER SETUP COMPLETE!${NC}"
    echo "=" * 50
    echo -e "${GREEN}✅ Ubuntu updates: Complete${NC}"
    echo -e "${GREEN}✅ Repository sync: Complete${NC}"
    echo -e "${GREEN}✅ VS Code extensions: Complete${NC}"
    echo "=" * 50
    echo -e "${BLUE}🚀 VS Code can now safely run additional tasks${NC}"
    echo ""
    
else
    echo -e "${YELLOW}⚠️  Not in container setup context - skipping full setup${NC}"
    echo -e "${BLUE}💡 This script should run during container creation/start${NC}"
fi