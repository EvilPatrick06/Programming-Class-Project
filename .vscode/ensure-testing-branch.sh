#!/bin/bash
# Ensure Testing Branch Script
# Always switch to Testing branch for development work

echo "🔄 Ensuring you're on Testing branch for development..."

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" = "Testing" ]; then
    echo "✅ Already on Testing branch!"
else
    echo "📍 Currently on: $CURRENT_BRANCH"
    echo "🔄 Switching to Testing branch..."
    
    # Check if Testing branch exists locally
    if git branch --list Testing | grep -q Testing; then
        # Local Testing branch exists, switch to it
        git checkout Testing
    elif git branch -r --list origin/Testing | grep -q origin/Testing; then
        # Remote Testing branch exists, create local tracking branch
        git checkout -b Testing origin/Testing
    else
        # No Testing branch exists, create it
        echo "⚠️ Testing branch doesn't exist. Creating it..."
        git checkout -b Testing
    fi
    
    if [ $? -eq 0 ]; then
        echo "✅ Successfully switched to Testing branch!"
    else
        echo "❌ Failed to switch to Testing branch"
        exit 1
    fi
fi

echo "🎉 Ready for development work on Testing branch!"