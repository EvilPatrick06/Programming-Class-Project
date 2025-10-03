#!/usr/bin/env python3
"""
Git Sync Script - Push Changes TO GitHub
Shows VS Code dialogs and notifications instead of terminal prompts
Comprehensive script for committing and pushing your local changes to GitHub

Purpose: Push your local changes TO GitHub
Note: To update your codespace FROM GitHub, use auto_sync.py instead
"""

import subprocess
import sys
import os
import time
import tempfile
import textwrap

def create_vscode_dialog_html(title, message, options):
    """Create an HTML file for VS Code dialog simulation"""
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #1e1e1e;
            color: #cccccc;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        .dialog {{
            background: #2d2d30;
            border: 1px solid #3e3e42;
            border-radius: 6px;
            padding: 24px;
            max-width: 500px;
            width: 100%;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }}
        .title {{
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 16px;
            color: #ffffff;
        }}
        .message {{
            margin-bottom: 24px;
            line-height: 1.5;
            white-space: pre-wrap;
        }}
        .options {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .option {{
            background: #0e639c;
            color: white;
            border: none;
            padding: 12px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: background-color 0.2s;
        }}
        .option:hover {{
            background: #1177bb;
        }}
        .option.secondary {{
            background: #5a5a5a;
        }}
        .option.secondary:hover {{
            background: #6a6a6a;
        }}
        .instructions {{
            margin-top: 16px;
            font-size: 12px;
            color: #999999;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="dialog">
        <div class="title">{title}</div>
        <div class="message">{message}</div>
        <div class="options">
            {"".join([f'<button class="option {'secondary' if i > 0 else ''}" onclick="selectOption({i})">{opt}</button>' for i, opt in enumerate(options)])}
        </div>
        <div class="instructions">
            Click an option above or respond in the terminal with the number (1-{len(options)})
        </div>
    </div>
    <script>
        function selectOption(index) {{
            document.querySelectorAll('.option').forEach((btn, i) => {{
                if (i === index) {{
                    btn.style.background = '#28a745';
                    btn.textContent += ' ✓';
                }}
            }});
        }}
    </script>
</body>
</html>
"""
    return html_content

def show_vscode_notification(message, message_type="info"):
    """Show a VS Code notification using the integrated terminal"""
    colors = {
        "info": "\033[94m",      # Blue
        "success": "\033[92m",   # Green  
        "warning": "\033[93m",   # Yellow
        "error": "\033[91m"      # Red
    }
    reset = "\033[0m"
    
    icons = {
        "info": "ℹ️",
        "success": "✅", 
        "warning": "⚠️",
        "error": "❌"
    }
    
    color = colors.get(message_type, colors["info"])
    icon = icons.get(message_type, icons["info"])
    
    # Clear the terminal and show prominent message
    print("\033[2J\033[H")  # Clear screen and move cursor to top
    print("=" * 80)
    print(f"{color}{icon} Git Sync to GitHub{reset}")
    print("=" * 80)
    print(f"{color}{message}{reset}")
    print("=" * 80)
    print()

def show_vscode_dialog(title, message, options):
    """Show a prominent dialog-like interface in the terminal"""
    # Create HTML file for potential viewing
    html_content = create_vscode_dialog_html(title, message, options)
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
        f.write(html_content)
        html_file = f.name
    
    # Show in terminal with nice formatting
    print("\033[2J\033[H")  # Clear screen
    print("┌" + "─" * 78 + "┐")
    print(f"│{title:^78}│")
    print("├" + "─" * 78 + "┤")
    
    # Word wrap the message
    wrapped_lines = textwrap.wrap(message, width=76)
    for line in wrapped_lines:
        print(f"│ {line:<76} │")
    
    print("├" + "─" * 78 + "┤")
    print("│ Options:                                                                   │")
    
    for i, option in enumerate(options):
        option_text = f"{i+1}. {option}"
        if len(option_text) > 74:
            option_text = option_text[:71] + "..."
        print(f"│ {option_text:<76} │")
    
    print("└" + "─" * 78 + "┘")
    print()
    
    # Try to open HTML in VS Code's simple browser as a bonus
    try:
        subprocess.run(["code", "--command", "simpleBrowser.show", f"file://{html_file}"], 
                      capture_output=True, timeout=2)
    except:
        pass  # Ignore if it fails
    
    return html_file

def get_vscode_input(prompt, options=None):
    """Get user input through VS Code-style dialog interface"""
    try:
        if options:
            # Show the dialog-style interface
            html_file = show_vscode_dialog("Git Sync to GitHub", prompt, options)
            
            # Get input from terminal
            while True:
                try:
                    choice = input(f"\nEnter your choice (1-{len(options)}): ").strip()
                    if choice.isdigit():
                        idx = int(choice) - 1
                        if 0 <= idx < len(options):
                            # Clean up HTML file
                            try:
                                os.unlink(html_file)
                            except:
                                pass
                            return options[idx]
                    print("Invalid choice. Please try again.")
                except (EOFError, KeyboardInterrupt):
                    # Clean up HTML file
                    try:
                        os.unlink(html_file)
                    except:
                        pass
                    return None
        else:
            # Simple text input with nice formatting
            print("\n" + "="*60)
            print(f"📝 {prompt}")
            print("="*60)
            try:
                return input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                return None
    except Exception as e:
        print(f"Error getting input: {e}")
        # Fallback to simple terminal input
        if options:
            print(f"\n{prompt}")
            for i, option in enumerate(options):
                print(f"{i+1}. {option}")
            while True:
                try:
                    choice = input(f"Enter your choice (1-{len(options)}): ").strip()
                    if choice.isdigit():
                        idx = int(choice) - 1
                        if 0 <= idx < len(options):
                            return options[idx]
                    print("Invalid choice. Please try again.")
                except (EOFError, KeyboardInterrupt):
                    return None
        else:
            try:
                return input(f"{prompt}: ").strip()
            except (EOFError, KeyboardInterrupt):
                return None

def run_command_preview(command, description):
    """Run a command and return the result for preview"""
    print(f"\n{'='*60}")
    print(f"🔍 PREVIEW: {description}")
    print(f"Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.stdout:
            print("OUTPUT:")
            print(result.stdout)
        
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

def check_git_status():
    """Check git repository status"""
    try:
        # Check for uncommitted changes
        status_result = subprocess.run("git status --porcelain", 
                                     shell=True, capture_output=True, text=True)
        has_changes = bool(status_result.stdout.strip())
        
        # Check for unpushed commits
        try:
            unpushed_result = subprocess.run("git log @{u}..HEAD", 
                                           shell=True, capture_output=True, text=True)
            has_unpushed = unpushed_result.returncode == 0 and bool(unpushed_result.stdout.strip())
        except:
            has_unpushed = False
        
        # Check if branch exists on remote
        try:
            branch_check = subprocess.run("git push --dry-run", shell=True, capture_output=True, text=True)
            branch_needs_upstream = "has no upstream branch" in branch_check.stderr
        except:
            branch_needs_upstream = True
        
        return has_changes, has_unpushed, branch_needs_upstream
    except Exception:
        return False, False, True

def main():
    """Main git sync function"""
    
    # Show welcome message
    show_vscode_notification("🚀 Git Sync Started! Preparing to push your changes to GitHub...", "info")
    
    print("🚀 Git Sync Script - Push to GitHub")
    print("=" * 50)
    print("📤 This script helps you commit and push your changes TO GitHub")
    print("📥 To update your codespace FROM GitHub, use auto_sync.py instead")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        show_vscode_notification("❌ Not in a git repository!", "error")
        return
    
    # Get current branch name
    try:
        current_branch = subprocess.run("git branch --show-current", 
                                      shell=True, capture_output=True, text=True).stdout.strip()
    except:
        current_branch = "unknown"
    
    print(f"Current branch: {current_branch}")
    
    # If we're on main and Testing branch exists, suggest switching
    if current_branch == "main":
        # Check if Testing branch exists
        testing_exists = subprocess.run("git branch --list Testing", 
                                       shell=True, capture_output=True, text=True)
        if testing_exists.stdout.strip():
            switch_to_testing = get_vscode_input(
                "💡 You're on main branch, but Testing branch exists. Switch to Testing for development work?",
                ["Yes, switch to Testing branch", "No, stay on main"]
            )
            
            if switch_to_testing and "Yes" in switch_to_testing:
                print("🔄 Switching to Testing branch...")
                switch_result = subprocess.run("git checkout Testing", shell=True, capture_output=True, text=True)
                if switch_result.returncode == 0:
                    current_branch = "Testing"
                    show_vscode_notification("✅ Switched to Testing branch for development!", "success")
                    print("✅ Switched to Testing branch for development!")
                else:
                    print("⚠️ Failed to switch to Testing branch, continuing on main...")
    
    # Check git status
    has_changes, has_unpushed, branch_needs_upstream = check_git_status()
    
    # If nothing to do
    if not has_changes and not has_unpushed and not branch_needs_upstream:
        show_vscode_notification("✅ Everything is already up to date! No changes to sync.", "success")
        print("✅ Everything is already up to date! No changes to sync.")
        return
    
    # Check if current branch is behind main (only if not on main branch)
    is_behind_main = False
    is_testing_branch = current_branch.lower() in ["testing", "test", "dev", "develop", "development"]
    
    if current_branch not in ["main", "master"]:
        # Check if main branch exists and if current branch is behind it
        try:
            main_exists_result = subprocess.run("git show-ref --verify --quiet refs/heads/main", 
                                               shell=True, capture_output=True)
            main_exists = main_exists_result.returncode == 0
            
            if main_exists:
                behind_check = subprocess.run("git rev-list --count HEAD..main", 
                                            shell=True, capture_output=True, text=True)
                if behind_check.returncode == 0:
                    commits_behind = int(behind_check.stdout.strip()) if behind_check.stdout.strip().isdigit() else 0
                    is_behind_main = commits_behind > 0
                    
                    if is_behind_main:
                        print(f"⚠️  Current branch '{current_branch}' is {commits_behind} commit(s) behind main.")
                        
                        if is_testing_branch:
                            sync_choice = get_vscode_input(
                                f"Your testing branch is {commits_behind} commits behind main. What would you like to do?",
                                [
                                    "Sync with main first (merge main into testing branch)",
                                    "Continue without syncing (push changes on top of older main)",
                                    "Exit and handle manually"
                                ]
                            )
                            
                            if sync_choice and "Sync with main" in sync_choice:
                                print("🔄 Syncing testing branch with main...")
                                # Fetch latest changes
                                fetch_result = run_command_execute("git fetch origin", "Fetch latest changes from remote")
                                if fetch_result and fetch_result.returncode == 0:
                                    # Try to merge main into current branch
                                    merge_result = run_command_execute("git merge main", "Merge main into testing branch")
                                    if merge_result and merge_result.returncode == 0:
                                        show_vscode_notification("✅ Successfully synced testing branch with main!", "success")
                                        is_behind_main = False
                                    else:
                                        show_vscode_notification("⚠️ Merge conflicts detected. Please resolve them manually.", "error")
                                        print("You can resolve conflicts and then run: git add . && git commit")
                                        return
                                else:
                                    show_vscode_notification("⚠️ Failed to fetch latest changes from remote.", "error")
                                    return
                            elif sync_choice and "Continue without" in sync_choice:
                                print("⚠️  Continuing without syncing. Your changes will be based on an older version of main.")
                                is_behind_main = False  # Continue anyway
                            else:
                                show_vscode_notification("❌ Exiting. Please handle the sync manually.", "warning")
                                return
                        else:
                            sync_with_main = get_vscode_input(
                                f"Your branch is {commits_behind} commits behind main. Sync with main first?",
                                ["Yes, sync with main first", "No, continue without syncing"]
                            )
                            
                            if sync_with_main and "Yes" in sync_with_main:
                                print("🔄 Syncing with main branch...")
                                # Fetch latest changes
                                fetch_result = run_command_execute("git fetch origin", "Fetch latest changes from remote")
                                if fetch_result and fetch_result.returncode == 0:
                                    # Try to merge main into current branch
                                    merge_result = run_command_execute("git merge main", "Merge main into current branch")
                                    if merge_result and merge_result.returncode == 0:
                                        show_vscode_notification("✅ Successfully synced with main!", "success")
                                        is_behind_main = False
                                    else:
                                        show_vscode_notification("⚠️ Merge conflicts detected. Please resolve them manually.", "error")
                                        print("You can resolve conflicts and then run: git add . && git commit")
                                        return
                                else:
                                    show_vscode_notification("⚠️ Failed to fetch latest changes from remote.", "error")
                                    return
        except Exception as e:
            print(f"Warning: Could not check if branch is behind main: {e}")
    
    # PREVIEW PHASE - Show everything first
    show_vscode_notification("📋 Preview Phase - Here's what your git commands will do:", "info")
    print("📋 PREVIEW PHASE - Here's what your git commands will do:")
    print("=" * 80)
    
    step_counter = 1
    
    # Step 1: Preview what git add will stage (only if there are changes)
    if has_changes:
        print(f"\n{step_counter}️⃣  What 'git add .' will stage:")
        add_preview = run_command_preview("git add . --dry-run", "Preview what files will be added")
        
        # Show what files will be staged (simulate)
        print(f"\n{step_counter + 1}️⃣  After adding files, status would be:")
        # We'll run git add . and then git status, but reset afterward for the preview
        temp_add = subprocess.run("git add .", shell=True, capture_output=True)
        if temp_add.returncode == 0:
            staged_result = run_command_preview("git status", "Status after staging files")
            # Reset the staging for now
            subprocess.run("git reset", shell=True, capture_output=True)
        step_counter += 2
    else:
        print("\n✅ No uncommitted changes found.")
    
    # Show what will be pushed
    if has_unpushed or branch_needs_upstream:
        print(f"\n{step_counter}️⃣  What will be pushed to GitHub:")
        if branch_needs_upstream:
            print("   - This branch doesn't exist on GitHub yet, it will be created")
        if has_unpushed:
            print("   - Unpushed commits will be synced")
            run_command_preview("git log --oneline @{u}..HEAD", "Unpushed commits")
        elif not branch_needs_upstream:
            print("   - Local commits will be synced")
            run_command_preview("git log --oneline origin/main..HEAD", "Local commits to push")
    
    # Show push and PR options available
    print(f"\n{'4️⃣' if has_changes else '2️⃣'}  Push Options Available:")
    print(f"   - Push to current branch ({current_branch})")
    print("   - Push to Testing branch (Development)")
    print("   - Push to main branch (Production)")
    print("   - Create pull request with code review")
    print("   - Create new feature branch")
    
    # DECISION PHASE
    print("\n" + "🤔" * 20)
    print("DECISION TIME!")
    print("🤔" * 20)
    
    proceed = get_vscode_input(
        "Based on the preview above, do you want to proceed with pushing to GitHub?",
        ["Yes, proceed with sync", "No, cancel"]
    )
    
    if not proceed or "No" in proceed:
        show_vscode_notification("❌ Sync cancelled. No changes were made.", "warning")
        print("❌ Sync cancelled. No changes were made.")
        return
    
    # Ask about pull request creation and target branch
    create_pr = False
    merge_pr = False
    target_branch = "main"  # default
    
    # Re-get current branch to make sure we have the correct one
    try:
        current_branch = subprocess.run("git branch --show-current", 
                                      shell=True, capture_output=True, text=True).stdout.strip()
    except:
        pass
    
    print(f"🔍 Debug: Current branch is '{current_branch}'")
    
    # Universal push options - always available regardless of current branch
    push_option = get_vscode_input(
        f"You're on branch '{current_branch}'. Where would you like to push your changes?",
        [
            f"Push to current branch ({current_branch})",
            "Push to Testing branch (Development)",
            "Push to main branch (Production)", 
            "Create pull request instead",
            "Create new feature branch"
        ]
    )
    
    if f"current branch ({current_branch})" in push_option:
        # Push to current branch - simple case
        print(f"🔄 Will push to current branch: {current_branch}")
        target_branch = current_branch
        create_pr = False
        sync_testing = False
        
    elif "Push to main" in push_option:
        # Push to main branch (and also sync Testing to keep it up-to-date)
        if current_branch == "main":
            print("🔄 Will push to main branch and sync Testing")
            target_branch = "main"
            create_pr = False
            sync_testing = True
        else:
            print(f"🔄 Will push {current_branch} changes to main branch and sync Testing")
            target_branch = "main"
            create_pr = False
            sync_testing = True
            
    elif "Push to Testing" in push_option:
        # Push to Testing branch
        if current_branch == "Testing":
            print("🔄 Will push to Testing branch")
            target_branch = "Testing"
            create_pr = False
            sync_testing = False
        else:
            print(f"🔄 Will push {current_branch} changes to Testing branch")
            target_branch = "Testing"
            create_pr = False
            sync_testing = False
            
    elif "Create pull request" in push_option:
        # Create PR workflow
        print(f"🔄 Will push {current_branch} and create pull request")
        create_pr = True
        sync_testing = False
        
        # Ask which branch to target for PR
        target_branch_response = get_vscode_input(
            f"Which branch should the pull request target?",
            ["main (production)", "Testing (development)", "Other branch"]
        )
        
        if "Testing" in target_branch_response:
            target_branch = "Testing"
        elif "Other" in target_branch_response:
            custom_branch = get_vscode_input("Enter the target branch name")
            target_branch = custom_branch if custom_branch else "main"
        else:
            target_branch = "main"
        
        print(f"📋 Will create PR: {current_branch} → {target_branch}")
        
        # Ask about immediate merge
        merge_response = get_vscode_input(
            f"Would you also like to merge the pull request to '{target_branch}' immediately?",
            ["Yes, merge immediately", "No, leave for review"]
        )
        merge_pr = merge_response and "Yes" in merge_response
        
        if merge_pr:
            print(f"⚠️  Note: This will merge the PR to '{target_branch}' without waiting for reviews. Use with caution!")
            
    elif "Create new feature branch" in push_option:
        # Create new feature branch
        feature_branch_name = get_vscode_input("Enter name for new feature branch")
        if feature_branch_name:
            print(f"🔄 Will create new branch: {feature_branch_name}")
            # Create and switch to new branch
            subprocess.run(f"git checkout -b {feature_branch_name}", shell=True)
            current_branch = feature_branch_name
            target_branch = current_branch
            
            # Ask if they want to create PR after pushing
            pr_after_push = get_vscode_input(
                f"After pushing '{feature_branch_name}', create pull request?",
                ["Yes, create PR to main", "Yes, create PR to Testing", "No, just push branch"]
            )
            
            if "PR to main" in pr_after_push:
                create_pr = True
                target_branch = "main"
            elif "PR to Testing" in pr_after_push:
                create_pr = True  
                target_branch = "Testing"
            else:
                create_pr = False
                target_branch = current_branch
        else:
            # Fallback to current branch
            target_branch = current_branch
            create_pr = False
    
    # Get commit message (only if there are changes to commit)
    commit_message = None
    if has_changes:
        commit_message = get_vscode_input("Enter your commit message")
        
        if not commit_message:
            show_vscode_notification("❌ Commit message is required. Cancelling sync.", "error")
            return
        
        # Confirm commit message
        print(f"\nCommit message: '{commit_message}'")
        confirm_message = get_vscode_input(
            "Is this commit message correct?",
            ["Yes, use this message", "No, let me change it"]
        )
        
        if confirm_message and "No" in confirm_message:
            commit_message = get_vscode_input("Enter your commit message again")
            if not commit_message:
                show_vscode_notification("❌ Commit message is required. Cancelling sync.", "error")
                return
    
    # EXECUTION PHASE
    show_vscode_notification("⚡ Executing commands...", "info")
    print("\n" + "⚡" * 20)
    print("EXECUTING COMMANDS...")
    print("⚡" * 20)
    
    step_counter = 1
    
    # Execute Step 1: Add files (only if there are changes)
    if has_changes:
        print(f"\n{step_counter}️⃣  Adding files to staging area...")
        add_result = run_command_execute("git add .", "Add all changed files")
        
        if add_result is None or add_result.returncode != 0:
            show_vscode_notification("❌ Failed to add files. Stopping.", "error")
            return
        step_counter += 1
    
    # Execute Step 2: Commit (only if there are changes)
    if has_changes:
        print(f"\n{step_counter}️⃣  Committing changes...")
        commit_command = f'git commit -m "{commit_message}"'
        commit_result = run_command_execute(commit_command, "Commit changes")
        
        if commit_result is None or commit_result.returncode != 0:
            show_vscode_notification("❌ Failed to commit changes. Stopping.", "error")
            return
        step_counter += 1
    
    # Execute Step 3: Push
    if has_unpushed or branch_needs_upstream or has_changes:
        print(f"\n{step_counter}️⃣  Pushing to GitHub...")
        
        # Get the actual current branch (might have changed if we created a new branch)
        actual_current_branch = subprocess.run("git branch --show-current", shell=True, capture_output=True, text=True).stdout.strip()
        
        # Handle different push scenarios
        if actual_current_branch == target_branch:
            # Simple case: pushing current branch to itself
            if branch_needs_upstream:
                push_command = f"git push --set-upstream origin {actual_current_branch}"
                push_result = run_command_execute(push_command, f"Push {actual_current_branch} and set upstream")
            else:
                push_result = run_command_execute("git push", f"Push changes to {actual_current_branch}")
                
        else:
            # Cross-branch push: pushing current branch content to different target
            print(f"🔄 Cross-branch push: {actual_current_branch} → {target_branch}")
            
            # Check if target branch exists on remote
            target_exists = subprocess.run(f"git ls-remote --heads origin {target_branch}", 
                                         shell=True, capture_output=True, text=True)
            
            if target_exists.stdout.strip():
                # Target branch exists, push to it
                push_command = f"git push origin {actual_current_branch}:{target_branch}"
                push_result = run_command_execute(push_command, f"Push {actual_current_branch} changes to {target_branch}")
            else:
                # Target branch doesn't exist, create it
                push_command = f"git push origin {actual_current_branch}:{target_branch}"
                push_result = run_command_execute(push_command, f"Create {target_branch} branch from {actual_current_branch}")
        
        # Check push result
        if push_result is None or push_result.returncode != 0:
            show_vscode_notification("❌ Failed to push to GitHub. This might be due to remote changes.", "error")
            print("This might be due to remote changes. You may need to resolve conflicts manually.")
            return
        else:
            if actual_current_branch == target_branch:
                show_vscode_notification(f"✅ Successfully pushed to {target_branch}!", "success")
            else:
                show_vscode_notification(f"✅ Successfully pushed {actual_current_branch} changes to {target_branch}!", "success")
        
        # Execute Testing sync if requested (when pushing to main)
        if sync_testing and target_branch == "main":
            print(f"\n{step_counter + 1}️⃣  Syncing Testing branch with main to keep it up-to-date...")
            
            # Save current branch to return to it later
            original_branch = subprocess.run("git branch --show-current", shell=True, capture_output=True, text=True).stdout.strip()
            
            # Switch to main branch first to get the latest changes
            main_checkout = run_command_execute("git checkout main", "Switch to main branch")
            if main_checkout and main_checkout.returncode == 0:
                main_pull = run_command_execute("git pull", "Update local main with remote changes")
                if main_pull and main_pull.returncode == 0:
                    
                    # Switch to Testing branch and merge main
                    testing_checkout = run_command_execute("git checkout Testing", "Switch to Testing branch")
                    if testing_checkout and testing_checkout.returncode == 0:
                        testing_merge = run_command_execute("git merge main", "Merge main into Testing to keep it current")
                        if testing_merge and testing_merge.returncode == 0:
                            testing_push = run_command_execute("git push origin Testing", "Push updated Testing branch")
                            if testing_push and testing_push.returncode == 0:
                                show_vscode_notification("✅ Testing branch synced with main successfully!", "success")
                                print("✅ Testing branch is now up to date with main!")
                            else:
                                show_vscode_notification("⚠️ Failed to push updated Testing branch", "warning")
                        else:
                            show_vscode_notification("⚠️ Failed to merge main into Testing branch", "warning")
                    else:
                        show_vscode_notification("⚠️ Failed to checkout Testing branch for sync", "warning")
                else:
                    show_vscode_notification("⚠️ Failed to update local main branch", "warning")
            else:
                show_vscode_notification("⚠️ Failed to checkout main branch for sync", "warning")
            
            # Return to original branch
            if original_branch and original_branch != "Testing":
                run_command_execute(f"git checkout {original_branch}", f"Return to {original_branch} branch")
            elif original_branch != "Testing":
                run_command_execute("git checkout Testing", "Switch to Testing branch")
        
        step_counter += 1
    
    # Execute Step 4: Create Pull Request (if requested)
    if create_pr:
        print(f"\n{step_counter}️⃣  Creating Pull Request...")
        
        # Get PR title and body
        pr_title = get_vscode_input("Enter pull request title (or press Enter to use commit message)")
        if not pr_title and commit_message:
            pr_title = commit_message
        elif not pr_title:
            pr_title = f"Changes from {current_branch}"
        
        # Use commit message as default PR description
        pr_body = commit_message if commit_message else "Automated pull request created by git sync script."
        
        # Create the pull request
        pr_command = f'gh pr create --title "{pr_title}" --base {target_branch} --head {current_branch} --body "{pr_body}"'
        
        pr_result = run_command_execute(pr_command, f"Create pull request: {current_branch} → {target_branch}")
        
        if pr_result and pr_result.returncode == 0:
            show_vscode_notification(f"✅ Pull request created successfully! ({current_branch} → {target_branch})", "success")
            print(f"✅ Pull request created successfully! ({current_branch} → {target_branch})")
            
            # Show PR URL if available
            try:
                pr_url_result = subprocess.run(f"gh pr view {current_branch} --json url -q .url", 
                                             shell=True, capture_output=True, text=True)
                if pr_url_result.returncode == 0 and pr_url_result.stdout.strip():
                    print(f"🔗 PR URL: {pr_url_result.stdout.strip()}")
            except:
                pass
            
            # Merge the PR if requested
            if merge_pr:
                print(f"\n{step_counter + 1}️⃣  Merging Pull Request to {target_branch}...")
                
                merge_method = get_vscode_input(
                    "Choose merge method:",
                    [
                        "Merge commit (preserves branch history)",
                        "Squash and merge (combines all commits into one)",
                        "Rebase and merge (replays commits without merge commit)"
                    ]
                )
                
                if "Squash" in merge_method:
                    merge_flag = "--squash"
                elif "Rebase" in merge_method:
                    merge_flag = "--rebase"
                else:
                    merge_flag = "--merge"
                
                merge_command = f"gh pr merge {current_branch} {merge_flag}"
                merge_result = run_command_execute(merge_command, f"Merge pull request to {target_branch}")
                
                if merge_result and merge_result.returncode == 0:
                    show_vscode_notification(f"✅ Pull request merged to {target_branch} successfully!", "success")
                    print(f"✅ Pull request merged to {target_branch} successfully!")
                    
                    # Switch to target branch and pull the merged changes
                    print(f"\n{step_counter + 2}️⃣  Updating local {target_branch} branch...")
                    checkout_result = run_command_execute(f"git checkout {target_branch}", f"Switch to {target_branch} branch")
                    if checkout_result and checkout_result.returncode == 0:
                        pull_result = run_command_execute("git pull", f"Pull merged changes to {target_branch}")
                        if pull_result and pull_result.returncode == 0:
                            show_vscode_notification(f"✅ Local {target_branch} branch updated with merged changes!", "success")
                            
                            # If merged to main, also sync Testing branch to keep it up to date
                            if target_branch == "main":
                                print(f"\n{step_counter + 3}️⃣  Syncing Testing branch with main to avoid falling behind...")
                                testing_checkout = run_command_execute("git checkout Testing", "Switch to Testing branch")
                                if testing_checkout and testing_checkout.returncode == 0:
                                    testing_merge = run_command_execute("git merge main", "Merge main into Testing to keep it current")
                                    if testing_merge and testing_merge.returncode == 0:
                                        testing_push = run_command_execute("git push origin Testing", "Push updated Testing branch")
                                        if testing_push and testing_push.returncode == 0:
                                            show_vscode_notification("✅ Testing branch synced with main successfully!", "success")
                                            print("✅ Testing branch is now up to date with main!")
                                        else:
                                            show_vscode_notification("⚠️ Failed to push updated Testing branch", "warning")
                                    else:
                                        show_vscode_notification("⚠️ Failed to merge main into Testing branch", "warning")
                                else:
                                    show_vscode_notification("⚠️ Failed to checkout Testing branch for sync", "warning")
                                
                                # Switch back to target branch
                                run_command_execute(f"git checkout {target_branch}", f"Switch back to {target_branch}")
                            
                            # Handle branch cleanup
                            if current_branch != target_branch:
                                cleanup_choice = get_vscode_input(
                                    f"Delete the merged feature branch '{current_branch}'?",
                                    ["Yes, delete it", "No, keep it"]
                                )
                                
                                if cleanup_choice and "Yes" in cleanup_choice:
                                    # Delete local branch
                                    delete_local = run_command_execute(f"git branch -d {current_branch}", 
                                                                     "Delete local feature branch")
                                    # Delete remote branch
                                    delete_remote = run_command_execute(f"git push origin --delete {current_branch}", 
                                                                       "Delete remote feature branch")
                                    if delete_local and delete_local.returncode == 0:
                                        show_vscode_notification("✅ Feature branch cleaned up!", "success")
                        else:
                            show_vscode_notification(f"⚠️ Failed to pull merged changes to {target_branch}.", "warning")
                    else:
                        show_vscode_notification(f"⚠️ Failed to switch to {target_branch} branch.", "warning")
                else:
                    show_vscode_notification(f"⚠️ Failed to merge pull request to {target_branch}. You can merge it manually on GitHub.", "warning")
        else:
            show_vscode_notification("⚠️ Failed to create pull request, but your changes were pushed successfully.", "warning")
            print("You can create the pull request manually on GitHub.")
    
    # SUCCESS!
    print("\n" + "🎉" * 30)
    if create_pr and merge_pr:
        show_vscode_notification("✅ SUCCESS! Your changes have been synced, PR created, and merged to main!", "success")
    elif create_pr:
        show_vscode_notification("✅ SUCCESS! Your changes have been synced to GitHub and pull request created!", "success")
    else:
        show_vscode_notification("✅ SUCCESS! Your changes have been synced to GitHub!", "success")
    print("🎉" * 30)
    
    # Show final status
    print("\nFinal status:")
    run_command_preview("git status", "Final git status")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_vscode_notification("⚠️ Script interrupted by user. Exiting...", "warning")
        print("\n\n⚠️  Script interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        show_vscode_notification(f"❌ Unexpected error: {e}", "error")
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)