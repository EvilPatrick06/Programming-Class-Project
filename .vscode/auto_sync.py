#!/usr/bin/env python3
"""
Codespace Auto-Sync Script
Updates your codespace with the latest code FROM GitHub (main or Testing branch)
Shows VS Code dialogs and notifications instead of terminal prompts

Purpose: Pull/sync FROM GitHub TO your codespace
Note: To push your changes TO GitHub, use git_sync.py instead
"""

import subprocess
import sys
import os
import json
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
            // This would ideally communicate back to the Python script
            // For now, we'll just highlight the selection
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
    # Create a colorful notification in the terminal
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
    print(f"{color}{icon} VS Code Auto-Sync Notification{reset}")
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
            html_file = show_vscode_dialog("Repository Auto-Sync", prompt, options)
            
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

def check_git_status():
    """Check if there are any uncommitted changes or unpushed commits"""
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
        
        return has_changes, has_unpushed
    except Exception:
        return False, False

def sync_repository():
    """Main sync function with VS Code dialogs - focuses on syncing FROM GitHub"""
    
    # Show welcome message
    show_vscode_notification("🚀 Codespace Auto-Sync Started! Updating from GitHub...", "info")
    
    print("🚀 Codespace Auto-Sync Script")
    print("=" * 50)
    print("📥 This script updates your codespace with the latest code from GitHub")
    print("📤 To push your changes TO GitHub, use the git_sync.py script instead")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        show_vscode_notification("❌ Not in a git repository!", "error")
        return
    
    # Get current branch
    try:
        current_branch = subprocess.run("git branch --show-current", 
                                      shell=True, capture_output=True, text=True).stdout.strip()
    except:
        current_branch = "unknown"
    
    print(f"Current branch: {current_branch}")
    
    # Auto-switch to Testing branch if we're on main and Testing exists
    if current_branch == "main":
        print("💡 Codespace prefers Testing branch for development work...")
        
        # Check if Testing branch exists locally
        testing_exists_local = subprocess.run("git branch --list Testing", 
                                            shell=True, capture_output=True, text=True)
        
        # Check if Testing branch exists on remote
        testing_exists_remote = subprocess.run("git ls-remote --heads origin Testing", 
                                             shell=True, capture_output=True, text=True)
        
        if testing_exists_local.stdout.strip():
            # Testing branch exists locally, switch to it
            print("🔄 Switching to existing Testing branch...")
            switch_result = subprocess.run("git checkout Testing", shell=True, capture_output=True, text=True)
            if switch_result.returncode == 0:
                current_branch = "Testing"
                show_vscode_notification("✅ Auto-switched to Testing branch for development!", "success")
                print("✅ Switched to Testing branch!")
                # Pull latest changes
                subprocess.run("git pull origin Testing 2>/dev/null || true", shell=True)
        elif testing_exists_remote.stdout.strip():
            # Testing branch exists on remote, check it out
            print("🔄 Checking out Testing branch from remote...")
            checkout_result = subprocess.run("git checkout -b Testing origin/Testing", 
                                           shell=True, capture_output=True, text=True)
            if checkout_result.returncode == 0:
                current_branch = "Testing"
                show_vscode_notification("✅ Auto-switched to Testing branch from remote!", "success")
                print("✅ Checked out Testing branch from remote!")
        else:
            # No Testing branch exists, offer to create it
            create_testing = get_vscode_input(
                "No Testing branch found. Create Testing branch for development work?",
                ["Yes, create Testing branch", "No, stay on main"]
            )
            
            if create_testing and "Yes" in create_testing:
                print("🔄 Creating Testing branch...")
                create_result = subprocess.run("git checkout -b Testing", shell=True, capture_output=True, text=True)
                if create_result.returncode == 0:
                    current_branch = "Testing"
                    show_vscode_notification("✅ Created Testing branch for development!", "success")
                    print("✅ Created Testing branch!")
    
    # Check git status
    has_changes, has_unpushed = check_git_status()
    
    # If everything is clean, offer branch sync options
    if not has_changes and not has_unpushed:
        print("✅ No local changes found - ready to sync from GitHub!")
        
        action = get_vscode_input(
            "How would you like to update your codespace?",
            [
                "Sync fresh from GitHub main branch (replaces everything)",
                "Sync fresh from GitHub Testing branch (replaces everything)", 
                "Pull latest changes from current branch",
                "Switch to a different branch first",
                "Nothing - continue working"
            ]
        )
        
        if action is None:
            show_vscode_notification("❌ Sync cancelled by user", "warning")
            return
        
        if "main branch" in action:
            print("🔄 Syncing fresh from GitHub main branch...")
            print("⚠️  This will replace ALL local files with the latest from main!")
            result = subprocess.run(["/bin/bash", ".vscode/sync-repo.sh", "main"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                show_vscode_notification("✅ Successfully synced from main branch!", "success")
                print("✅ Codespace synced from main branch!")
                print("🔄 Reloading VS Code window to reflect changes...")
                # Optional: reload VS Code window
                try:
                    subprocess.run(["code", "--command", "workbench.action.reloadWindow"], 
                                 capture_output=True, timeout=2)
                except:
                    pass
            else:
                show_vscode_notification(f"❌ Sync failed: {result.stderr}", "error")
                print(f"❌ Sync failed: {result.stderr}")
        
        elif "Testing branch" in action:
            print("🔄 Syncing fresh from GitHub Testing branch...")
            print("⚠️  This will replace ALL local files with the latest from Testing!")
            result = subprocess.run(["/bin/bash", ".vscode/sync-repo.sh", "Testing"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                show_vscode_notification("✅ Successfully synced from Testing branch!", "success")
                print("✅ Codespace synced from Testing branch!")
                print("🔄 Reloading VS Code window to reflect changes...")
                # Optional: reload VS Code window
                try:
                    subprocess.run(["code", "--command", "workbench.action.reloadWindow"], 
                                 capture_output=True, timeout=2)
                except:
                    pass
            else:
                show_vscode_notification(f"❌ Sync failed: {result.stderr}", "error")
                print(f"❌ Sync failed: {result.stderr}")
        
        elif "Pull latest changes" in action:
            print("🔄 Pulling latest changes from current branch...")
            result = subprocess.run("git pull", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                show_vscode_notification("✅ Successfully pulled latest changes!", "success")
                print("✅ Successfully pulled latest changes!")
            else:
                show_vscode_notification(f"❌ Failed to pull changes: {result.stderr}", "error")
                print(f"❌ Failed: {result.stderr}")
        
        elif "Switch to a different branch" in action:
            # Get available branches
            try:
                branches_result = subprocess.run("git branch -r", shell=True, capture_output=True, text=True)
                if branches_result.returncode == 0:
                    branches = [b.strip().replace('origin/', '') for b in branches_result.stdout.split('\n') 
                              if b.strip() and 'origin/' in b and '->' not in b]
                    if branches:
                        selected_branch = get_vscode_input("Select branch to switch to:", branches)
                        if selected_branch:
                            print(f"🔄 Switching to branch: {selected_branch}")
                            result = subprocess.run(f"git checkout {selected_branch}", 
                                                  shell=True, capture_output=True, text=True)
                            if result.returncode == 0:
                                show_vscode_notification(f"✅ Switched to branch: {selected_branch}", "success")
                                # After switching, offer to pull latest changes
                                pull_after_switch = get_vscode_input(
                                    f"Pull latest changes from {selected_branch}?",
                                    ["Yes, pull latest changes", "No, stay as is"]
                                )
                                if pull_after_switch and "Yes" in pull_after_switch:
                                    subprocess.run("git pull", shell=True)
                                    show_vscode_notification(f"✅ Pulled latest changes from {selected_branch}!", "success")
                            else:
                                show_vscode_notification(f"❌ Failed to switch branch: {result.stderr}", "error")
                    else:
                        show_vscode_notification("No remote branches found", "warning")
            except Exception as e:
                show_vscode_notification(f"Error getting branches: {e}", "error")
        
        else:
            show_vscode_notification("✅ Codespace ready! Happy coding! 🎉", "success")
            print("✅ Continuing with current state. Happy coding!")
    
    else:
        # There are changes or unpushed commits - warn user
        status_msg = []
        if has_changes:
            status_msg.append("uncommitted changes")
        if has_unpushed:
            status_msg.append("unpushed commits")
        
        message = f"Found {' and '.join(status_msg)} in your codespace."
        print(f"⚠️  {message}")
        print("💡 Remember: This script is for syncing FROM GitHub, not pushing TO GitHub")
        
        action = get_vscode_input(
            f"You have {' and '.join(status_msg)}. What would you like to do?",
            [
                "View my changes first",
                "Discard my changes and sync fresh from GitHub",
                "Keep my changes and skip sync (I'll handle manually)",
                "Open git_sync.py script to push my changes"
            ]
        )
        
        if action is None:
            show_vscode_notification("❌ Sync cancelled by user", "warning")
            return
        
        if "View my changes" in action:
            print("� Showing your local changes...")
            print("\n📋 Git status:")
            subprocess.run("git status", shell=True)
            print("\n📋 Git diff (your changes):")
            subprocess.run("git diff", shell=True)
            
            # Ask what to do next
            next_action = get_vscode_input(
                "After reviewing your changes, what would you like to do?",
                [
                    "Keep my changes (skip sync)",
                    "Discard my changes and sync from GitHub",
                    "Push my changes first (open git_sync.py)"
                ]
            )
            
            if next_action and "Keep my changes" in next_action:
                show_vscode_notification("✅ Keeping your changes. Use git_sync.py to push them later.", "info")
            elif next_action and "Discard my changes" in next_action:
                confirm = get_vscode_input(
                    "⚠️  Are you sure you want to discard ALL your changes? This cannot be undone!",
                    ["Yes, discard all changes", "No, keep my changes"]
                )
                if confirm and "Yes" in confirm:
                    branch_choice = get_vscode_input(
                        "Which GitHub branch should we sync from?",
                        ["main", "Testing"]
                    )
                    if branch_choice:
                        print(f"🔄 Discarding changes and syncing fresh from {branch_choice}...")
                        subprocess.run("git reset --hard HEAD", shell=True)
                        subprocess.run("git clean -fd", shell=True)
                        result = subprocess.run(["/bin/bash", ".vscode/sync-repo.sh", branch_choice], 
                                              capture_output=True, text=True)
                        if result.returncode == 0:
                            show_vscode_notification(f"✅ Synced fresh from {branch_choice} branch!", "success")
                        else:
                            show_vscode_notification(f"❌ Sync failed: {result.stderr}", "error")
            elif next_action and "Push my changes" in next_action:
                print("🚀 Opening git_sync.py script to help you push your changes...")
                show_vscode_notification("💡 Running git_sync.py to help you push your changes to GitHub", "info")
                subprocess.run([sys.executable, ".vscode/git_sync.py"], capture_output=False)
        
        elif "Discard my changes" in action:
            confirm = get_vscode_input(
                "⚠️  Are you sure you want to discard ALL your changes and sync fresh? This cannot be undone!",
                ["Yes, discard and sync fresh", "No, keep my changes"]
            )
            
            if confirm and "Yes" in confirm:
                branch_choice = get_vscode_input(
                    "Which GitHub branch should we sync from?",
                    ["main", "Testing"]
                )
                
                if branch_choice:
                    print(f"🔄 Discarding all changes and syncing fresh from {branch_choice}...")
                    subprocess.run("git reset --hard HEAD", shell=True)
                    subprocess.run("git clean -fd", shell=True)
                    result = subprocess.run(["/bin/bash", ".vscode/sync-repo.sh", branch_choice], 
                                          capture_output=True, text=True)
                    if result.returncode == 0:
                        show_vscode_notification(f"✅ Synced fresh from {branch_choice} branch!", "success")
                    else:
                        show_vscode_notification(f"❌ Sync failed: {result.stderr}", "error")
        
        elif "git_sync.py script" in action:
            print("🚀 Opening git_sync.py script to help you push your changes...")
            show_vscode_notification("💡 Running git_sync.py to help you push your changes to GitHub", "info")
            subprocess.run([sys.executable, ".vscode/git_sync.py"], capture_output=False)
        
        else:
            show_vscode_notification("✅ Keeping your changes. Use git_sync.py when ready to push.", "info")
            print("✅ Keeping your changes. Use git_sync.py when you're ready to push to GitHub.")

def main():
    """Main function"""
    try:
        # Add a small delay to ensure VS Code is fully loaded
        time.sleep(2)
        
        # Check if this is likely a codespace environment
        if not (os.environ.get('CODESPACES') or os.environ.get('GITPOD_WORKSPACE_ID') or 
                os.path.exists('/workspaces')):
            print("This script is designed for codespace environments.")
            return
        
        sync_repository()
        
    except KeyboardInterrupt:
        show_vscode_notification("⚠️  Auto-sync interrupted by user", "warning")
        print("\n⚠️  Auto-sync interrupted by user")
    except Exception as e:
        show_vscode_notification(f"❌ Error during auto-sync: {e}", "error")
        print(f"❌ Error during auto-sync: {e}")

if __name__ == "__main__":
    main()