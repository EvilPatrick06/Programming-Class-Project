#!/bin/bash
# Terminal Prompt Setup for GitHub Codespaces
# Ensures GITHUB_USER is available for the terminal prompt

echo "🖥️  Setting up terminal prompt for GitHub Codespaces..."

# Function to wait for GitHub environment variables to be available
wait_for_github_env() {
    local max_wait=30
    local waited=0
    
    while [ $waited -lt $max_wait ]; do
        if [ ! -z "${GITHUB_USER:-}" ]; then
            echo "✅ GITHUB_USER found: $GITHUB_USER"
            return 0
        fi
        
        # Try to source the codespaces environment
        if [ -f "/workspaces/.codespaces/shared/.env-secrets" ]; then
            echo "🔄 Loading GitHub environment variables..."
            while read line; do
                key=$(echo $line | sed "s/=.*//")
                value=$(echo $line | sed "s/$key=//1")
                decodedValue=$(echo $value | base64 -d 2>/dev/null)
                if [ ! -z "$decodedValue" ]; then
                    export $key="$decodedValue"
                fi
            done < /workspaces/.codespaces/shared/.env-secrets
        fi
        
        # Check again after loading
        if [ ! -z "${GITHUB_USER:-}" ]; then
            echo "✅ GITHUB_USER loaded: $GITHUB_USER"
            return 0
        fi
        
        echo "⏳ Waiting for GitHub environment... (${waited}s/${max_wait}s)"
        sleep 2
        waited=$((waited + 2))
    done
    
    echo "⚠️  GITHUB_USER not found within ${max_wait}s - using fallback"
    return 1
}

# Function to refresh the bash prompt
refresh_prompt() {
    if [ -n "$BASH_VERSION" ]; then
        # Re-source the bash prompt function if it exists
        if declare -f __bash_prompt >/dev/null; then
            __bash_prompt
        fi
        
        # Force prompt refresh
        export PS1="$PS1"
    fi
}

# Only run during container initialization
if [ "$1" = "--container-init" ] || [ ! -z "$CODESPACES_CONTAINER_SETUP" ]; then
    echo "🚀 Container initialization mode - setting up GitHub environment"
    
    # Wait for GitHub environment to be available
    wait_for_github_env
    
    # Add to user's bashrc to ensure it's available for all future shells
    BASHRC_ADDITION="
# GitHub Codespaces Environment Fix (Added by Programming Class Project setup)
# Source GitHub environment early to ensure proper terminal prompt
if [ -f \"/workspaces/Programming-Class-Project/.devcontainer/github-env.sh\" ]; then
    source /workspaces/Programming-Class-Project/.devcontainer/github-env.sh
fi
"
    
    # Check if we need to add this to .bashrc (add at the beginning)
    if ! grep -q "GitHub Codespaces Environment Fix" "$HOME/.bashrc"; then
        echo "📝 Adding GitHub environment fix to beginning of .bashrc"
        # Create a temporary file with our addition + existing content
        echo "$BASHRC_ADDITION" > /tmp/bashrc_new
        cat "$HOME/.bashrc" >> /tmp/bashrc_new
        mv /tmp/bashrc_new "$HOME/.bashrc"
        echo "✅ GitHub environment fix added to .bashrc"
    fi
    
    echo "✅ Terminal prompt setup complete"
else
    echo "💡 Run with --container-init flag during container setup"
fi