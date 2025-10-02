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
    
    # Get current branch name
    current_branch = subprocess.run("git branch --show-current", shell=True, capture_output=True, text=True).stdout.strip()
    
    # Check if current branch is behind main (only if not on main branch)
    is_behind_main = False
    is_testing_branch = current_branch.lower() in ["testing", "test", "dev", "develop", "development"]
    
    if current_branch not in ["main", "master"]:
        # Check if main branch exists and if current branch is behind it
        main_exists = subprocess.run("git show-ref --verify --quiet refs/heads/main", shell=True, capture_output=True).returncode == 0
        if main_exists:
            behind_check = subprocess.run("git rev-list --count HEAD..main", shell=True, capture_output=True, text=True)
            if behind_check.returncode == 0:
                commits_behind = int(behind_check.stdout.strip()) if behind_check.stdout.strip().isdigit() else 0
                is_behind_main = commits_behind > 0
                if is_behind_main:
                    print(f"⚠️  Current branch '{current_branch}' is {commits_behind} commit(s) behind main.")
                    
                    if is_testing_branch:
                        print(f"💡 Since you're on a testing branch, you have options:")
                        print("   1. Sync with main (merge main into testing branch)")
                        print("   2. Continue without syncing (your changes will be on top of older main)")
                        print("   3. Exit and handle manually")
                        
                        sync_choice = get_user_input("Choose option (1-3): ")
                        
                        if sync_choice == "1":
                            print("🔄 Syncing testing branch with main...")
                            # Fetch latest changes
                            fetch_result = run_command_execute("git fetch origin", "Fetch latest changes from remote")
                            if fetch_result and fetch_result.returncode == 0:
                                # Try to merge main into current branch
                                merge_result = run_command_execute("git merge main", "Merge main into testing branch")
                                if merge_result and merge_result.returncode == 0:
                                    print("✅ Successfully synced testing branch with main!")
                                    is_behind_main = False
                                else:
                                    print("⚠️  Merge conflicts detected. Please resolve them manually and run the script again.")
                                    print("You can resolve conflicts and then run: git add . && git commit")
                                    sys.exit(1)
                            else:
                                print("⚠️  Failed to fetch latest changes from remote.")
                                sys.exit(1)
                        elif sync_choice == "2":
                            print("⚠️  Continuing without syncing. Your changes will be based on an older version of main.")
                            is_behind_main = False  # Continue anyway
                        else:
                            print("❌ Exiting. Please handle the sync manually.")
                            sys.exit(0)
                    else:
                        sync_with_main = get_user_input("Would you like to sync with main first? This will update your branch with the latest changes (y/n): ")
                        if sync_with_main.lower() == 'y':
                            print("🔄 Syncing with main branch...")
                            # Fetch latest changes
                            fetch_result = run_command_execute("git fetch origin", "Fetch latest changes from remote")
                            if fetch_result and fetch_result.returncode == 0:
                                # Try to merge main into current branch
                                merge_result = run_command_execute("git merge main", "Merge main into current branch")
                                if merge_result and merge_result.returncode == 0:
                                    print("✅ Successfully synced with main!")
                                    is_behind_main = False
                                else:
                                    print("⚠️  Merge conflicts detected. Please resolve them manually and run the script again.")
                                    print("You can resolve conflicts and then run: git add . && git commit")
                                    sys.exit(1)
                            else:
                                print("⚠️  Failed to fetch latest changes from remote.")
                                sys.exit(1)
    
    # First, check if there are any changes to commit
    status_check = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    has_changes = bool(status_check.stdout.strip())
    
    # Check if there are unpushed commits (only if upstream exists)
    unpushed_check = subprocess.run("git log @{u}..HEAD", shell=True, capture_output=True, text=True)
    has_unpushed_commits = unpushed_check.returncode == 0 and bool(unpushed_check.stdout.strip())
    
    # Check if branch exists on remote
    branch_check = subprocess.run("git push --dry-run", shell=True, capture_output=True, text=True)
    branch_needs_upstream = "has no upstream branch" in branch_check.stderr
    
    if not has_changes and not has_unpushed_commits and not branch_needs_upstream:
        print("✅ Everything is already up to date! No changes to sync.")
        sys.exit(0)
    
    # PREVIEW PHASE - Show everything first
    print("📋 PREVIEW PHASE - Here's what your git commands will do:")
    print("=" * 80)
    
    # Step 1: Preview what git add will stage (only if there are changes)
    if has_changes:
        print("\n1️⃣  What 'git add .' will stage:")
        add_preview = run_command_preview("git add . --dry-run", "Preview what files will be added")
        
        # Step 2: Show what files will be staged (simulate)
        print("\n2️⃣  After adding files, status would be:")
        # We'll run git add . and then git status, but reset afterward for the preview
        temp_add = subprocess.run("git add .", shell=True, capture_output=True)
        if temp_add.returncode == 0:
            staged_result = run_command_preview("git status", "Status after staging files")
            # Reset the staging for now
            subprocess.run("git reset", shell=True, capture_output=True)
    else:
        print("\n✅ No uncommitted changes found.")
    
    # Show what will be pushed
    if has_unpushed_commits or branch_needs_upstream:
        print(f"\n{'3️⃣' if has_changes else '1️⃣'}  What will be pushed to GitHub:")
        if branch_needs_upstream:
            print("   - This branch doesn't exist on GitHub yet, it will be created")
        if has_unpushed_commits:
            print("   - Unpushed commits will be synced")
            run_command_preview("git log --oneline @{u}..HEAD", "Unpushed commits")
        elif not branch_needs_upstream:
            # Show commits on current branch vs main/origin
            print("   - Local commits will be synced")
            run_command_preview("git log --oneline origin/main..HEAD", "Local commits to push")
    
    # Check if we should offer to create a pull request  
    is_not_main_branch = current_branch != "main" and current_branch != "master"
    
    if is_not_main_branch:
        print(f"\n{'4️⃣' if has_changes else '2️⃣'}  Pull Request Option:")
        print(f"   - After pushing, you can create a pull request from '{current_branch}' to 'main'")
        print("   - This will allow code review before merging your changes")
    
    # DECISION PHASE
    print("\n" + "🤔" * 20)
    print("DECISION TIME!")
    print("🤔" * 20)
    
    proceed = get_user_input("\nBased on the preview above, do you want to proceed with syncing to GitHub? (y/n): ")
    
    if proceed.lower() != 'y':
        print("❌ Sync cancelled. No changes were made.")
        sys.exit(0)
    
    # Ask about pull request creation if we're not on main branch
    create_pr = False
    merge_pr = False
    if is_not_main_branch:
        pr_response = get_user_input(f"\n🔄 After pushing, would you like to create a pull request from '{current_branch}' to 'main'? (y/n): ")
        create_pr = pr_response.lower() == 'y'
        
        if create_pr:
            merge_response = get_user_input("🔀 Would you also like to merge the pull request immediately after creating it? (y/n): ")
            merge_pr = merge_response.lower() == 'y'
            
            if merge_pr:
                print("⚠️  Note: This will merge the PR without waiting for reviews. Use with caution!")
    
    # Get commit message (only if there are changes to commit)
    commit_message = None
    if has_changes:
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
    
    step_counter = 1
    
    # Execute Step 1: Add files (only if there are changes)
    if has_changes:
        print(f"\n{step_counter}️⃣  Adding files to staging area...")
        add_result = run_command_execute("git add .", "Add all changed files")
        
        if add_result is None or add_result.returncode != 0:
            print("❌ Failed to add files. Stopping.")
            sys.exit(1)
        step_counter += 1
    
    # Execute Step 2: Commit (only if there are changes)
    if has_changes:
        print(f"\n{step_counter}️⃣  Committing changes...")
        commit_command = f'git commit -m "{commit_message}"'
        commit_result = run_command_execute(commit_command, "Commit changes")
        
        if commit_result is None or commit_result.returncode != 0:
            print("❌ Failed to commit changes. Stopping.")
            sys.exit(1)
        step_counter += 1
    
    # Execute Step 3: Push
    if has_unpushed_commits or branch_needs_upstream or has_changes:
        print(f"\n{step_counter}️⃣  Pushing to GitHub...")
        
        # Use appropriate push command based on whether branch exists
        if branch_needs_upstream:
            current_branch = subprocess.run("git branch --show-current", shell=True, capture_output=True, text=True).stdout.strip()
            push_command = f"git push --set-upstream origin {current_branch}"
            push_result = run_command_execute(push_command, "Push changes and set upstream")
        else:
            push_result = run_command_execute("git push", "Push changes to GitHub")
        
        if push_result is None or push_result.returncode != 0:
            print("❌ Failed to push to GitHub.")
            print("This might be due to remote changes. You may need to resolve conflicts manually.")
            sys.exit(1)
        
        step_counter += 1
    
    # Execute Step 4: Create Pull Request (if requested)
    if create_pr:
        print(f"\n{step_counter}️⃣  Creating Pull Request...")
        
        # Get PR title and body
        pr_title = get_user_input("\n📝 Enter pull request title (or press Enter to use commit message): ", allow_empty=True)
        if not pr_title and commit_message:
            pr_title = commit_message
        elif not pr_title:
            pr_title = f"Changes from {current_branch}"
        
        # Use commit message as default PR description
        if commit_message:
            print(f"\n📝 Pull request description will be: '{commit_message}'")
            use_commit_msg = get_user_input("Use this as PR description? (y/n, or press Enter for yes): ", allow_empty=True)
            if use_commit_msg.lower() in ['', 'y', 'yes']:
                pr_body = commit_message
            else:
                pr_body = get_user_input("📝 Enter custom pull request description: ")
        else:
            pr_body = get_user_input("📝 Enter pull request description (optional): ", allow_empty=True)
        
        # Create the pull request
        pr_command = f'gh pr create --title "{pr_title}" --base main --head {current_branch}'
        if pr_body:
            pr_command += f' --body "{pr_body}"'
        else:
            pr_command += ' --body "Automated pull request created by git sync script."'
        
        pr_result = run_command_execute(pr_command, "Create pull request")
        
        if pr_result and pr_result.returncode == 0:
            print("✅ Pull request created successfully!")
            # Show the PR URL
            pr_url_result = subprocess.run(f"gh pr view {current_branch} --json url -q .url", shell=True, capture_output=True, text=True)
            if pr_url_result.returncode == 0 and pr_url_result.stdout.strip():
                print(f"🔗 PR URL: {pr_url_result.stdout.strip()}")
            
            # Merge the PR if requested
            if merge_pr:
                print(f"\n{step_counter + 1}️⃣  Merging Pull Request...")
                
                # Get merge method preference
                print("\nChoose merge method:")
                print("1. Merge commit (preserves branch history)")
                print("2. Squash and merge (combines all commits into one)")
                print("3. Rebase and merge (replays commits without merge commit)")
                
                merge_method_input = get_user_input("Enter choice (1-3, or press Enter for merge commit): ", allow_empty=True)
                
                if merge_method_input == "2":
                    merge_method = "--squash"
                elif merge_method_input == "3":
                    merge_method = "--rebase"
                else:
                    merge_method = "--merge"
                
                merge_command = f"gh pr merge {current_branch} {merge_method}"
                merge_result = run_command_execute(merge_command, f"Merge pull request using {merge_method} method")
                
                if merge_result and merge_result.returncode == 0:
                    print("✅ Pull request merged successfully!")
                    
                    # Switch back to main and pull the merged changes
                    print(f"\n{step_counter + 2}️⃣  Updating local main branch...")
                    checkout_result = run_command_execute("git checkout main", "Switch to main branch")
                    if checkout_result and checkout_result.returncode == 0:
                        pull_result = run_command_execute("git pull", "Pull merged changes")
                        if pull_result and pull_result.returncode == 0:
                            print("✅ Local main branch updated with merged changes!")
                            
                            # Handle branch cleanup based on branch type
                            if is_testing_branch:
                                print(f"\n🔄 Since '{current_branch}' is a testing branch, updating it with latest main...")
                                checkout_feature = run_command_execute(f"git checkout {current_branch}", "Switch back to testing branch")
                                if checkout_feature and checkout_feature.returncode == 0:
                                    # Merge main into testing branch to keep it up to date
                                    merge_main = run_command_execute("git merge main", "Update testing branch with latest main")
                                    if merge_main and merge_main.returncode == 0:
                                        # Push updated testing branch
                                        push_updated = run_command_execute(f"git push origin {current_branch}", "Push updated testing branch")
                                        if push_updated and push_updated.returncode == 0:
                                            print("✅ Testing branch updated with latest main changes!")
                                        else:
                                            print("⚠️  Failed to push updated testing branch, but local branch is updated.")
                                    else:
                                        print("⚠️  Failed to merge main into testing branch. You may need to resolve conflicts manually.")
                                else:
                                    print("⚠️  Failed to switch back to testing branch.")
                            else:
                                # For regular feature branches, offer deletion
                                delete_branch = get_user_input(f"\n🗑️  Delete the feature branch '{current_branch}'? (y/n): ")
                                if delete_branch.lower() == 'y':
                                    # Delete local branch
                                    delete_local = run_command_execute(f"git branch -d {current_branch}", "Delete local feature branch")
                                    # Delete remote branch
                                    delete_remote = run_command_execute(f"git push origin --delete {current_branch}", "Delete remote feature branch")
                                    if delete_local and delete_local.returncode == 0 and delete_remote and delete_remote.returncode == 0:
                                        print("✅ Feature branch cleaned up!")
                                else:
                                    # If user chooses not to delete the branch, update it to match main
                                    print(f"\n🔄 Updating feature branch '{current_branch}' to match main...")
                                    checkout_feature = run_command_execute(f"git checkout {current_branch}", "Switch back to feature branch")
                                    if checkout_feature and checkout_feature.returncode == 0:
                                        # Reset feature branch to main
                                        reset_result = run_command_execute("git reset --hard main", "Update feature branch to match main")
                                        if reset_result and reset_result.returncode == 0:
                                            # Force push to update remote branch
                                            force_push = run_command_execute(f"git push --force-with-lease origin {current_branch}", "Update remote feature branch")
                                            if force_push and force_push.returncode == 0:
                                                print("✅ Feature branch updated to match main!")
                                            else:
                                                print("⚠️  Failed to update remote feature branch, but local branch is updated.")
                                        else:
                                            print("⚠️  Failed to update feature branch.")
                                    else:
                                        print("⚠️  Failed to switch back to feature branch.")
                else:
                    print("⚠️  Failed to merge pull request. You can merge it manually on GitHub.")
        else:
            print("⚠️  Failed to create pull request, but your changes were pushed successfully.")
            print("You can create the pull request manually on GitHub.")
    
    # SUCCESS!
    print("\n" + "🎉" * 30)
    if create_pr and merge_pr:
        print("✅ SUCCESS! Your changes have been synced, PR created, and merged to main!")
    elif create_pr:
        print("✅ SUCCESS! Your changes have been synced to GitHub and pull request created!")
    else:
        print("✅ SUCCESS! Your changes have been synced to GitHub!")
    print("🎉" * 30)
    
    # Show final status
    print("\nFinal status:")
    run_command_preview("git status", "Final git status")
    
    # Provide helpful tips based on branch type
    if is_testing_branch and not create_pr:
        print(f"\n💡 TESTING BRANCH TIPS:")
        print(f"   • Your '{current_branch}' branch is now updated and pushed to GitHub")
        print(f"   • You can continue making changes and running this script to sync")
        print(f"   • When ready, create a PR from '{current_branch}' to 'main' for code review")
        print(f"   • The script will keep your testing branch synced with main when merging PRs")
    elif not create_pr and is_not_main_branch and not is_testing_branch:
        print(f"\n💡 TIP: Your branch '{current_branch}' has been pushed to GitHub.")
        print("   To avoid 'branch behind main' issues in the future, consider:")
        print("   1. Creating pull requests to merge changes to main")
        print("   2. Deleting feature branches after they're merged")
        print("   3. Regularly syncing feature branches with main")
    
    # Final check for branches that might be behind main
    if not create_pr and is_not_main_branch:
        print(f"\n💡 TIP: Your branch '{current_branch}' has been pushed to GitHub.")
        print("   To avoid 'branch behind main' issues in the future, consider:")
        print("   1. Creating pull requests to merge changes to main")
        print("   2. Deleting feature branches after they're merged")
        print("   3. Regularly syncing feature branches with main")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Script interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)