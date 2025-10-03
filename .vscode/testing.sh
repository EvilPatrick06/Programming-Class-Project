#!/bin/bash
# Quick command to switch to Testing branch
# Usage: testing

echo "🔄 Switching to Testing branch..."

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" = "Testing" ]; then
    echo "✅ Already on Testing branch!"
else
    echo "📍 Currently on: $CURRENT_BRANCH"
    
    # Check for uncommitted changes
    if ! git diff-index --quiet HEAD -- 2>/dev/null; then
        echo "⚠️ You have uncommitted changes on $CURRENT_BRANCH"
        echo "🔄 Stashing changes before switching branches..."
        git stash push -m "Auto-stash before switching to Testing from $CURRENT_BRANCH"
    fi
    
    # Switch to Testing branch
    if git branch --list Testing | grep -q Testing; then
        git checkout Testing
    elif git branch -r --list origin/Testing | grep -q origin/Testing; then
        git checkout -b Testing origin/Testing
    else
        git checkout -b Testing
    fi
    
    if [ $? -eq 0 ]; then
        echo "✅ Successfully switched to Testing branch!"
        
        # Check if we stashed anything and offer to restore
        STASH_COUNT=$(git stash list | wc -l)
        if [ "$STASH_COUNT" -gt 0 ]; then
            echo "💾 You have $STASH_COUNT stash(es) available"
            echo "   Run 'git stash pop' to restore your changes when ready"
        fi
    else
        echo "❌ Failed to switch to Testing branch"
        exit 1
    fi
fi