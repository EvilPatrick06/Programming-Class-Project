#!/bin/bash

REPO_URL="https://github.com/EvilPatrick06/Programming-Class-Project.git"
# Get the workspace directory (parent of .vscode directory)
WORKSPACE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TEMP_DIR="$WORKSPACE_DIR/.vscode/tmp/repo-sync"

# Check if branch parameter is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <branch>"
    echo "Available branches: main, Testing"
    exit 1
fi

BRANCH="$1"

# Validate branch name
if [ "$BRANCH" != "main" ] && [ "$BRANCH" != "Testing" ]; then
    echo "Error: Branch must be either 'main' or 'Testing'"
    exit 1
fi

# Ensure temp directory parent exists
mkdir -p "$(dirname "$TEMP_DIR")"

# Clone the repository to a temporary directory with specific branch
git clone -b "$BRANCH" "$REPO_URL" "$TEMP_DIR"

# Change to workspace directory and remove everything except .vscode directory
cd "$WORKSPACE_DIR"
find . -mindepth 1 -not -path "./.vscode*" -exec rm -rf {} +

# Move everything from temp directory to workspace directory
mv "$TEMP_DIR"/* "$TEMP_DIR"/.* "$WORKSPACE_DIR/" 2>/dev/null || true

# Clean up
rm -rf "$TEMP_DIR"
cd "$WORKSPACE_DIR"

echo "Repository sync complete from branch: $BRANCH!"
