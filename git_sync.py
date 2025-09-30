#!/usr/bin/env python3
"""
Git Sync Script for Codespace to GitHub
Automates the git workflow while giving you control at each step
"""

import subprocess
import sys

def run_command(command, description):
    """Run a command and return the result"""
    print(f"\n{'='*50}")
    print(f"RUNNING: {description}")
    print(f"Command: {command}")
    print(f"{'='*50}")
    
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

def get_user_input(prompt, allow_empty=False):
    """Get user input with option to allow empty responses"""
    while True:
        response = input(prompt).strip()
        if response or allow_empty:
            return response
        print("Please provide a response.")

def main():
    print("🚀 Git Sync Script - Codespace to GitHub")
    print("This script will help you sync your changes to GitHub step by step.\n")
    
    # Step 1: Check git status
    print("Step 1: Checking what files have changed...")
    result = run_command("git status", "Check current git status")
    
    if result is None or result.returncode != 0:
        print("❌ Failed to check git status. Exiting.")
        sys.exit(1)
    
    continue_choice = get_user_input("\nDo you want to continue with adding files? (y/n): ")
    if continue_choice.lower() != 'y':
        print("Exiting script.")
        sys.exit(0)
    
    # Step 2: Add files
    print("\nStep 2: Adding files to staging area...")
    result = run_command("git add .", "Add all changed files")
    
    if result is None or result.returncode != 0:
        print("❌ Failed to add files. Exiting.")
        sys.exit(1)
    
    # Show what's staged
    print("\nLet's see what's staged for commit:")
    run_command("git status", "Check staged files")
    
    continue_choice = get_user_input("\nDo you want to continue with committing? (y/n): ")
    if continue_choice.lower() != 'y':
        print("Exiting script. You can unstage files with 'git reset' if needed.")
        sys.exit(0)
    
    # Step 3: Get commit message and commit
    print("\nStep 3: Creating a commit...")
    
    # Get commit message from user
    commit_message = get_user_input("Enter your commit message: ")
    
    # Show a preview of the commit
    print(f"\nCommit message will be: '{commit_message}'")
    confirm = get_user_input("Is this correct? (y/n): ")
    
    if confirm.lower() != 'y':
        # Allow them to re-enter the message
        commit_message = get_user_input("Enter your commit message again: ")
    
    # Run the commit
    commit_command = f'git commit -m "{commit_message}"'
    result = run_command(commit_command, "Commit changes")
    
    if result is None or result.returncode != 0:
        print("❌ Failed to commit changes. Exiting.")
        sys.exit(1)
    
    continue_choice = get_user_input("\nDo you want to continue with pushing to GitHub? (y/n): ")
    if continue_choice.lower() != 'y':
        print("Exiting script. Your changes are committed locally but not pushed to GitHub.")
        sys.exit(0)
    
    # Step 4: Push to GitHub
    print("\nStep 4: Pushing to GitHub...")
    result = run_command("git push", "Push changes to GitHub")
    
    if result is None or result.returncode != 0:
        print("❌ Failed to push to GitHub.")
        print("You might need to pull first if there are remote changes.")
        
        pull_choice = get_user_input("Do you want to try pulling first? (y/n): ")
        if pull_choice.lower() == 'y':
            pull_result = run_command("git pull", "Pull latest changes from GitHub")
            if pull_result and pull_result.returncode == 0:
                push_again = get_user_input("Pull successful. Try pushing again? (y/n): ")
                if push_again.lower() == 'y':
                    result = run_command("git push", "Push changes to GitHub (retry)")
        
        if result is None or result.returncode != 0:
            print("❌ Still failed to push. You may need to resolve conflicts manually.")
            sys.exit(1)
    
    # Success!
    print("\n" + "🎉" * 20)
    print("✅ SUCCESS! Your changes have been synced to GitHub!")
    print("🎉" * 20)
    
    # Show final status
    print("\nFinal status:")
    run_command("git status", "Final git status check")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Script interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)