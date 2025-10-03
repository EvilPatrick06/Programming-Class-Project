#!/bin/bash

REPO_URL="https://github.com/EvilPatrick06/Programming-Class-Project.git"
TEMP_DIR=".vscode/tmp/repo-sync"

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

# Remove everything in current directory except this script
find . -mindepth 1 -not -name "sync-repo.sh" -exec rm -rf {} +

# Move everything from temp directory to current directory
mv "$TEMP_DIR"/* "$TEMP_DIR"/.* . 2>/dev/null || true

# Clean up
rm -rf "$TEMP_DIR"

echo "Repository sync complete from branch: $BRANCH!"
