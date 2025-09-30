#!/usr/bin/env python3
"""
Git Sync Script for Codespace to GitHub
Shows you what will happen first, then lets you decide
"""

import subprocess
import sys

def run_command_preview(command, description):
    """Run a command and return the result for preview"""
    print(f"\n{'='*60}")
    print(f"PREVIEW: {description}")
    print(f"Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Print stdout if there is any
        if result.stdout:
            print("OUTPUT:")
            print(result.stdout)
        
        # Print stderr if there is any
        if result.stderr:
            print("WARNINGS/ERRORS:")
            print(result.stderr)
        
        print(f"Exit code: {result.returncode}")
        return result
    
    except Exception as e:
        print(f"Error running command: {e}")
        return None

def run_command_execute(command, description):
    """Execute a command for real"""
    print(f"\n✅ EXECUTING: {description}")
    print(f"Command: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        return result
    
    except Exception as e:
        print(f"Error executing command: {e}")
        return None

def get_user_input(prompt, allow_empty=False):
    """Get user input with option to allow empty responses"""
    while True:
        response = input(prompt).strip()
        if response or allow_empty:
            return response
        print("Please provide a response.")

def main():
    print("🚀 Git Sync Script - Codespace to GitHub")
    print("This script will show you what changes will be made, then ask for your approval.\n")
    
    # PREVIEW PHASE - Show everything first
    print("📋 PREVIEW PHASE - Here's what your git commands will do:")
    print("=" * 80)
    
    # Step 1: Check git status
    print("\n1️⃣  Current git status:")
    status_result = run_command_preview("git status", "Check current git status")
    
    if status_result is None or status_result.returncode != 0:
        print("❌ Failed to check git status. Cannot continue.")
        sys.exit(1)
    
    # Step 2: Preview what git add will stage
    print("\n2️⃣  What 'git add .' will stage:")
    add_preview = run_command_preview("git add . --dry-run", "Preview what files will be added")
    
    # Step 3: Show what files will be staged (simulate)
    print("\n3️⃣  After adding files, status would be:")
    # We'll run git add . and then git status, but reset afterward for the preview
    temp_add = subprocess.run("git add .", shell=True, capture_output=True)
    if temp_add.returncode == 0:
        staged_result = run_command_preview("git status", "Status after staging files")
        # Reset the staging for now
        subprocess.run("git reset", shell=True, capture_output=True)
    
    # DECISION PHASE
    print("\n" + "🤔" * 20)
    print("DECISION TIME!")
    print("🤔" * 20)
    
    proceed = get_user_input("\nBased on the preview above, do you want to proceed with syncing to GitHub? (y/n): ")
    
    if proceed.lower() != 'y':
        print("❌ Sync cancelled. No changes were made.")
        sys.exit(0)
    
    # Get commit message
    commit_message = get_user_input("\n💬 Enter your commit message: ")
    
    # Confirm commit message
    print(f"\nCommit message: '{commit_message}'")
    confirm_message = get_user_input("Is this commit message correct? (y/n): ")
    
    if confirm_message.lower() != 'y':
        commit_message = get_user_input("Enter your commit message again: ")
    
    # EXECUTION PHASE
    print("\n" + "⚡" * 20)
    print("EXECUTING COMMANDS...")
    print("⚡" * 20)
    
    # Execute Step 1: Add files
    print("\n1️⃣  Adding files to staging area...")
    add_result = run_command_execute("git add .", "Add all changed files")
    
    if add_result is None or add_result.returncode != 0:
        print("❌ Failed to add files. Stopping.")
        sys.exit(1)
    
    # Execute Step 2: Commit
    print("\n2️⃣  Committing changes...")
    commit_command = f'git commit -m "{commit_message}"'
    commit_result = run_command_execute(commit_command, "Commit changes")
    
    if commit_result is None or commit_result.returncode != 0:
        print("❌ Failed to commit changes. Stopping.")
        sys.exit(1)
    
    # Execute Step 3: Push
    print("\n3️⃣  Pushing to GitHub...")
    push_result = run_command_execute("git push", "Push changes to GitHub")
    
    if push_result is None or push_result.returncode != 0:
        print("❌ Failed to push to GitHub.")
        print("This might be due to remote changes. Trying to pull first...")
        
        pull_result = run_command_execute("git pull", "Pull latest changes")
        if pull_result and pull_result.returncode == 0:
            print("Pull successful. Trying to push again...")
            push_result = run_command_execute("git push", "Push changes (retry)")
        
        if push_result is None or push_result.returncode != 0:
            print("❌ Still failed to push. You may need to resolve conflicts manually.")
            sys.exit(1)
    
    # SUCCESS!
    print("\n" + "🎉" * 30)
    print("✅ SUCCESS! Your changes have been synced to GitHub!")
    print("🎉" * 30)
    
    # Show final status
    print("\nFinal status:")
    run_command_preview("git status", "Final git status")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Script interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)