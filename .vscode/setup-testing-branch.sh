#!/bin/bash
# Codespace startup script to ensure we're on Testing branch

echo "🚀 Setting up codespace for development..."

# Check if we're in a git repository
if [ -d ".git" ]; then
    CURRENT_BRANCH=$(git branch --show-current)
    echo "Current branch: $CURRENT_BRANCH"
    
    # If we're on main, try to switch to Testing
    if [ "$CURRENT_BRANCH" = "main" ]; then
        echo "💡 Switching to Testing branch for development work..."
        
        # Check if Testing branch exists locally
        if git branch --list Testing | grep -q Testing; then
            echo "🔄 Switching to existing Testing branch..."
            git checkout Testing
            git pull origin Testing 2>/dev/null || true
            echo "✅ Switched to Testing branch!"
        elif git ls-remote --heads origin Testing | grep -q Testing; then
            echo "🔄 Checking out Testing branch from remote..."
            git checkout -b Testing origin/Testing
            echo "✅ Checked out Testing branch from remote!"
        else
            echo "🔄 Creating new Testing branch..."
            git checkout -b Testing
            echo "✅ Created Testing branch!"
        fi
    else
        echo "✅ Already on development branch: $CURRENT_BRANCH"
    fi
else
    echo "⚠️  Not in a git repository"
fi

echo "🎉 Codespace setup complete!"