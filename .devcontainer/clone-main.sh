#!/bin/bash
# On first container creation, force overwrite the repo to latest main

set -e

REPO_URL="https://github.com/EvilPatrick06/Programming-Class-Project.git"

if [ -d ".git" ]; then
    echo "Fetching and resetting to origin/main from EvilPatrick06/Programming-Class-Project..."
    git fetch origin main
    git reset --hard origin/main
else
    echo "No .git directory found; cloning repository..."
    TEMP_DIR="$(mktemp -d)"
    git clone "$REPO_URL" "$TEMP_DIR"
    rsync -av --exclude='.git' "$TEMP_DIR/" ./
    rm -rf "$TEMP_DIR"
    git init
    git remote add origin "$REPO_URL"
    git fetch origin main
    git reset --hard origin/main
fi

echo "Repository synced to origin/main."
