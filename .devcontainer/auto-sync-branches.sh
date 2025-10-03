#!/bin/bash
# Smart Auto-Sync Script for Codespace
# Checks for recent commits across branches and auto-syncs with the most recent

echo "🚀 Smart Codespace Auto-Sync Starting..."
echo "=" * 60

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo -e "${RED}❌ Not in a git repository!${NC}"
    exit 1
fi

# Fetch all remote branches and latest commits
echo -e "${BLUE}🔄 Fetching latest information from GitHub...${NC}"
git fetch --all --quiet

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
echo -e "${BLUE}📍 Current branch: $CURRENT_BRANCH${NC}"

# Function to get the last commit date of a branch
get_last_commit_date() {
    local branch=$1
    git log -1 --format="%ct" "origin/$branch" 2>/dev/null || echo "0"
}

# Function to get human-readable time
get_human_time() {
    local timestamp=$1
    if [ "$timestamp" = "0" ]; then
        echo "Never"
    else
        date -d "@$timestamp" "+%Y-%m-%d %H:%M:%S"
    fi
}

# Get list of all remote branches
echo -e "${BLUE}🔍 Analyzing branch activity...${NC}"
BRANCHES=$(git branch -r | grep -v 'HEAD' | sed 's/origin\///' | tr -d ' ')

# Create associative arrays for branch data
declare -A BRANCH_TIMES
declare -A BRANCH_DATES
declare -A BRANCH_COMMITS

# Analyze each branch
for branch in $BRANCHES; do
    if [ "$branch" != "" ]; then
        timestamp=$(get_last_commit_date "$branch")
        human_date=$(get_human_time "$timestamp")
        last_commit=$(git log -1 --format="%h - %s" "origin/$branch" 2>/dev/null || echo "No commits")
        
        BRANCH_TIMES["$branch"]=$timestamp
        BRANCH_DATES["$branch"]="$human_date"
        BRANCH_COMMITS["$branch"]="$last_commit"
        
        echo -e "${YELLOW}  📂 $branch${NC}: $human_date"
        echo -e "      └─ $last_commit"
    fi
done

# Find the most recently updated branch
LATEST_BRANCH=""
LATEST_TIME=0

for branch in "${!BRANCH_TIMES[@]}"; do
    if [ "${BRANCH_TIMES[$branch]}" -gt "$LATEST_TIME" ]; then
        LATEST_TIME=${BRANCH_TIMES[$branch]}
        LATEST_BRANCH=$branch
    fi
done

echo ""
echo -e "${GREEN}🏆 Most recently updated branch: $LATEST_BRANCH${NC}"
echo -e "${GREEN}   Last updated: ${BRANCH_DATES[$LATEST_BRANCH]}${NC}"
echo -e "${GREEN}   Latest commit: ${BRANCH_COMMITS[$LATEST_BRANCH]}${NC}"

# Check if we need to sync
NEEDS_SYNC=false
SYNC_MESSAGE=""

if [ "$CURRENT_BRANCH" != "$LATEST_BRANCH" ]; then
    NEEDS_SYNC=true
    SYNC_MESSAGE="Different branch: You're on '$CURRENT_BRANCH', but '$LATEST_BRANCH' has newer commits"
elif [ "$CURRENT_BRANCH" = "$LATEST_BRANCH" ]; then
    # Check if local branch is behind remote
    LOCAL_COMMIT=$(git rev-parse HEAD 2>/dev/null || echo "")
    REMOTE_COMMIT=$(git rev-parse "origin/$CURRENT_BRANCH" 2>/dev/null || echo "")
    
    if [ "$LOCAL_COMMIT" != "$REMOTE_COMMIT" ]; then
        NEEDS_SYNC=true
        SYNC_MESSAGE="Local branch is behind remote '$LATEST_BRANCH'"
    fi
fi

# Check for local uncommitted changes
if ! git diff-index --quiet HEAD -- 2>/dev/null; then
    echo -e "${YELLOW}⚠️  You have uncommitted local changes${NC}"
    HAS_LOCAL_CHANGES=true
else
    HAS_LOCAL_CHANGES=false
fi

echo ""
echo "=" * 60

# Decide what to do
if [ "$NEEDS_SYNC" = true ]; then
    echo -e "${YELLOW}🔄 Sync needed: $SYNC_MESSAGE${NC}"
    
    if [ "$HAS_LOCAL_CHANGES" = true ]; then
        echo -e "${RED}⚠️  You have local changes that would be lost!${NC}"
        echo ""
        echo "Options:"
        echo "1. 🗑️  Discard local changes and sync with $LATEST_BRANCH"
        echo "2. � Complete overwrite sync (like fresh clone)"
        echo "3. �💾 Keep local changes and skip auto-sync"
        echo "4. 🔍 Show what changes would be lost"
        echo ""
        
        # In a non-interactive environment, default to keeping changes
        if [ -t 0 ]; then
            read -p "Choose option (1-4): " choice
        else
            choice="3"
            echo "Non-interactive mode: Keeping local changes (option 3)"
        fi
        
        case $choice in
            1)
                echo -e "${YELLOW}🗑️  Discarding local changes and syncing...${NC}"
                git reset --hard HEAD
                git clean -fd
                SYNC_ACTION="discard_and_sync"
                ;;
            2)
                echo -e "${YELLOW}🔄 Performing complete overwrite sync...${NC}"
                source .devcontainer/smart-overwrite-sync.sh
                if smart_overwrite_sync "$LATEST_BRANCH"; then
                    SYNC_ACTION="complete"
                else
                    SYNC_ACTION="skip"
                fi
                ;;
            4)
                echo -e "${BLUE}🔍 Here are your local changes that would be lost:${NC}"
                echo "----------------------------------------"
                git status --porcelain
                echo "----------------------------------------"
                git diff HEAD
                echo "----------------------------------------"
                echo ""
                read -p "Choose sync method - (1) Regular sync, (2) Complete overwrite, (N) Skip: " confirm
                case $confirm in
                    1)
                        git reset --hard HEAD
                        git clean -fd
                        SYNC_ACTION="discard_and_sync"
                        ;;
                    2)
                        source .devcontainer/smart-overwrite-sync.sh
                        if smart_overwrite_sync "$LATEST_BRANCH"; then
                            SYNC_ACTION="complete"
                        else
                            SYNC_ACTION="skip"
                        fi
                        ;;
                    *)
                        SYNC_ACTION="skip"
                        ;;
                esac
                ;;
            *)
                echo -e "${GREEN}💾 Keeping your local changes${NC}"
                SYNC_ACTION="skip"
                ;;
        esac
    else
        # No local changes, but offer sync options
        echo -e "${GREEN}✅ No local changes detected${NC}"
        echo ""
        echo "Sync options:"
        echo "1. 📥 Regular sync (git pull)"
        echo "2. 🔄 Complete overwrite sync (fresh clone)"
        echo "3. ⏭️  Skip auto-sync"
        echo ""
        
        if [ -t 0 ]; then
            read -p "Choose sync method (1-3): " choice
        else
            choice="1"
            echo "Non-interactive mode: Using regular sync (option 1)"
        fi
        
        case $choice in
            2)
                echo -e "${YELLOW}🔄 Performing complete overwrite sync...${NC}"
                source .devcontainer/smart-overwrite-sync.sh
                if smart_overwrite_sync "$LATEST_BRANCH"; then
                    SYNC_ACTION="complete"
                else
                    SYNC_ACTION="sync"
                fi
                ;;
            3)
                SYNC_ACTION="skip"
                ;;
            *)
                SYNC_ACTION="sync"
                ;;
        esac
    fi
    
    # Perform the sync
    if [ "$SYNC_ACTION" = "sync" ] || [ "$SYNC_ACTION" = "discard_and_sync" ]; then
        echo -e "${BLUE}🔄 Regular syncing with $LATEST_BRANCH...${NC}"
        
        # Switch to the latest branch and pull
        if [ "$CURRENT_BRANCH" != "$LATEST_BRANCH" ]; then
            echo "   📂 Switching to $LATEST_BRANCH..."
            git checkout "$LATEST_BRANCH" --quiet 2>/dev/null || git checkout -b "$LATEST_BRANCH" "origin/$LATEST_BRANCH" --quiet
        fi
        
        echo "   📥 Pulling latest changes..."
        git pull origin "$LATEST_BRANCH" --quiet
        
        echo -e "${GREEN}✅ Successfully synced with $LATEST_BRANCH!${NC}"
        echo -e "${GREEN}   Latest commit: ${BRANCH_COMMITS[$LATEST_BRANCH]}${NC}"
        
    elif [ "$SYNC_ACTION" = "complete" ]; then
        echo -e "${GREEN}✅ Complete overwrite sync completed!${NC}"
        echo -e "${GREEN}   Latest commit: ${BRANCH_COMMITS[$LATEST_BRANCH]}${NC}"
        
    else
        echo -e "${YELLOW}⏭️  Skipping auto-sync${NC}"
        echo -e "${BLUE}💡 You can manually run sync later using:${NC}"
        echo "   python3 .vscode/auto_sync.py"
    fi
    
    # Trigger VS Code reload for any sync action
    if [ "$SYNC_ACTION" != "skip" ] && [ "$CODESPACES" = "true" ]; then
        echo -e "${BLUE}🔄 Codespace synced - VS Code may reload automatically${NC}"
    fi
else
    echo -e "${GREEN}✅ Already up to date!${NC}"
    echo -e "${GREEN}   You're on the latest branch ($CURRENT_BRANCH) with recent commits${NC}"
fi

echo ""
echo "=" * 60
echo -e "${GREEN}🎉 Smart Auto-Sync Complete!${NC}"

# Optional: Run the VS Code auto_sync script after this
if [ -f ".vscode/auto_sync.py" ] && [ "$SYNC_ACTION" != "skip" ]; then
    echo -e "${BLUE}🚀 Launching VS Code Auto-Sync interface...${NC}"
    sleep 2
    # python3 .vscode/auto_sync.py
fi