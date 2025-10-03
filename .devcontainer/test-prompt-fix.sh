#!/bin/bash
# Test script to verify the terminal prompt fix works

echo "🧪 Testing Terminal Prompt Fix"
echo "=" * 40

echo "📊 Current Environment:"
echo "  GITHUB_USER: ${GITHUB_USER:-not set}"
echo "  Current prompt shows: $(whoami)"
echo ""

echo "🔍 Checking secrets file:"
if [ -f "/workspaces/.codespaces/shared/.env-secrets" ]; then
    echo "  ✅ Secrets file exists"
    echo "  📁 Location: /workspaces/.codespaces/shared/.env-secrets"
    
    # Test loading the environment (without showing actual secrets)
    echo "🔄 Testing environment loading..."
    
    # Create a temporary test
    source .devcontainer/load-github-env.sh
    
    if [ ! -z "${GITHUB_USER:-}" ]; then
        echo "  ✅ GITHUB_USER successfully loaded: $GITHUB_USER"
    else
        echo "  ❌ GITHUB_USER not found in secrets"
    fi
else
    echo "  ❌ Secrets file not found"
fi

echo ""
echo "🖥️  Current PS1 prompt test:"
echo "Expected format: @username ➜ /path (branch) $"
echo "Your current prompt prefix: $(echo "$PS1" | grep -o '@[^"]*' | head -1 || echo "No @ found")"

echo ""
echo "💡 Instructions for new containers:"
echo "1. The fix will be applied during container setup"
echo "2. New terminals should show: @${GITHUB_USER:-username} ➜ ..."
echo "3. If issues persist, check the setup logs during container creation"

echo ""
echo "🔧 To manually test the fix:"
echo "   source .devcontainer/load-github-env.sh"
echo "   exec bash  # Restart shell to see new prompt"