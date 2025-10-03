#!/bin/bash
# Smart Repository Overwrite Sync
# Completely replaces codespace content with the most recent branch from GitHub

REPO_URL="https://github.com/EvilPatrick06/Programming-Class-Project.git"

smart_overwrite_sync() {
    local target_branch=$1
    local temp_dir="/tmp/smart-repo-sync-$$"
    
    echo "🔄 Performing complete repository sync from $target_branch..."
    echo "⚠️  This will replace ALL files with the latest from GitHub!"
    
    # Clone the target branch
    if git clone -b "$target_branch" "$REPO_URL" "$temp_dir" --quiet; then
        echo "✅ Successfully cloned $target_branch"
        
        # Remove everything except .git and preserve some files
        find . -mindepth 1 \
            -not -path './.git*' \
            -not -name '.gitignore' \
            -not -path './.devcontainer*' \
            -exec rm -rf {} + 2>/dev/null || true
        
        # Copy everything from temp directory
        cp -r "$temp_dir"/. . 2>/dev/null || true
        
        # Cleanup
        rm -rf "$temp_dir"
        
        # Update git to point to the correct branch
        git checkout "$target_branch" --quiet 2>/dev/null || git checkout -b "$target_branch" --quiet
        git reset --hard "origin/$target_branch" --quiet 2>/dev/null || true
        
        echo "✅ Repository completely synced with $target_branch!"
        return 0
    else
        echo "❌ Failed to clone $target_branch"
        rm -rf "$temp_dir" 2>/dev/null || true
        return 1
    fi
}

# Export the function so it can be used by other scripts
export -f smart_overwrite_sync