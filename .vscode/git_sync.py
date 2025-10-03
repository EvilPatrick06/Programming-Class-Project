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
import json
import readline

# Configure readline for better editing experience
readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode emacs")  # Enable emacs-style editing (arrow keys, Ctrl+A, Ctrl+E, etc.)
readline.parse_and_bind("set completion-ignore-case on")

def create_vscode_dialog_html(title, message, options):
    """Create an HTML file for VS Code dialog simulation"""
    # Create options HTML
    options_html = "".join([f'<button class="option {"secondary" if i > 0 else ""}" onclick="selectOption({i})">{opt}</button>' for i, opt in enumerate(options)])
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 20px; background: #1e1e1e; color: #cccccc; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
        .dialog {{ background: #2d2d30; border: 1px solid #3e3e42; border-radius: 6px; padding: 24px; max-width: 500px; width: 100%; box-shadow: 0 8px 32px rgba(0,0,0,0.3); }}
        .title {{ font-size: 18px; font-weight: 600; margin-bottom: 16px; color: #ffffff; }}
        .message {{ margin-bottom: 24px; line-height: 1.5; white-space: pre-wrap; }}
        .options {{ display: flex; flex-direction: column; gap: 8px; }}
        .option {{ background: #0e639c; color: white; border: none; padding: 12px 16px; border-radius: 4px; cursor: pointer; font-size: 14px; transition: background-color 0.2s; }}
        .option:hover {{ background: #1177bb; }}
        .option.secondary {{ background: #5a5a5a; }}
        .option.secondary:hover {{ background: #6a6a6a; }}
        .instructions {{ margin-top: 16px; font-size: 12px; color: #999999; text-align: center; }}
    </style>
</head>
<body>
    <div class="dialog">
        <div class="title">{title}</div>
        <div class="message">{message}</div>
        <div class="options">{options_html}</div>
        <div class="instructions">Click an option above or respond in the terminal with the number (1-{len(options)})</div>
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
</html>"""
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
    # Create HTML file for potential viewing - use context manager for proper cleanup
    html_content = create_vscode_dialog_html(title, message, options)
    
    # Create temp file in .vscode/tmp directory for better organization
    os.makedirs('.vscode/tmp', exist_ok=True)
    html_file = f".vscode/tmp/.tmp_dialog_{int(time.time())}.html"
    with open(html_file, 'w') as f:
        f.write(html_content)
    
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
    
    # Note: We don't open in VS Code browser to avoid leftover tabs with weird URLs
    # The terminal-based dialog is sufficient and cleaner
    
    return html_file

def get_vscode_input(prompt, options=None, default_value=None):
    """Get user input through VS Code-style dialog interface"""
    html_file = None
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
                            return options[idx]
                    print("Invalid choice. Please try again.")
                except (EOFError, KeyboardInterrupt):
                    return None
        else:
            # Simple text input with nice formatting
            print("\n" + "="*60)
            print(f"📝 {prompt}")
            if default_value:
                print(f"(Use arrow keys to edit, Enter to confirm, Ctrl+C to cancel)")
            print("="*60)
            try:
                if default_value:
                    # Pre-fill the input with the default value for editing
                    def prefill_input():
                        try:
                            readline.insert_text(default_value)
                            readline.redisplay()
                        except:
                            pass  # Fallback gracefully if readline fails
                    
                    try:
                        # Set up readline to pre-fill the input
                        readline.set_pre_input_hook(prefill_input)
                        user_input = input("> ").strip()
                        # Clear the pre-input hook
                        readline.set_pre_input_hook(None)
                        
                        return user_input if user_input else default_value
                    except:
                        # Fallback to simple input if readline fails
                        readline.set_pre_input_hook(None)
                        print(f"Default: {default_value}")
                        user_input = input("> ").strip()
                        return user_input if user_input else default_value
                else:
                    user_input = input("> ").strip()
                    return user_input
            except (EOFError, KeyboardInterrupt):
                # Make sure to clear the pre-input hook on interrupt
                try:
                    readline.set_pre_input_hook(None)
                except:
                    pass
                return None
    except Exception as e:
        print(f"Error getting input: {e}")
        # Fallback to simple terminal input
        try:
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
                if default_value:
                    # Pre-fill the input with the default value for editing
                    def prefill_input():
                        readline.insert_text(default_value)
                        readline.redisplay()
                    
                    readline.set_pre_input_hook(prefill_input)
                    user_input = input(f"{prompt}: ").strip()
                    readline.set_pre_input_hook(None)
                    return user_input if user_input else default_value
                else:
                    return input(f"{prompt}: ").strip()
        except (EOFError, KeyboardInterrupt):
            return None
    finally:
        # Always clean up HTML file, regardless of how the function exits
        if html_file and os.path.exists(html_file):
            try:
                os.unlink(html_file)
            except:
                pass

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

def generate_copilot_commit_message():
    """Generate a commit message using GitHub Copilot based on git diff"""
    try:
        print("🤖 Attempting to generate commit message using GitHub Copilot...")
        
        # Get a simple summary of changes quickly
        status_result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True, timeout=5)
        changes_summary = status_result.stdout.strip()
        
        if not changes_summary:
            return None, "No changes detected to generate commit message from."
            
        # First try to use GitHub Copilot CLI
        prompt = f"Write a git commit message for these file changes: {changes_summary}"
        
        # Use GitHub Copilot with correct git target flag
        copilot_result = subprocess.run(
            ["gh", "copilot", "suggest", "-t", "git", prompt],
            capture_output=True, text=True, timeout=30
        )
        
        # Check for authentication or other errors
        if copilot_result.returncode != 0:
            error_msg = copilot_result.stderr.strip() if copilot_result.stderr else "Unknown error"
            print(f"⚠️ GitHub Copilot CLI failed: {error_msg}")
            
            # Fallback to intelligent rule-based generation
            return generate_smart_commit_message(changes_summary)
        
        if copilot_result.returncode == 0 and copilot_result.stdout.strip():
            # Extract the commit message from Copilot's response
            response = copilot_result.stdout.strip()
            lines = response.split('\n')
            
            # Look for a line that contains git commit command
            for line in lines:
                line = line.strip()
                if 'git commit -m' in line:
                    # Extract message from git commit -m "message"
                    start = line.find('"') + 1
                    end = line.rfind('"')
                    if start > 0 and end > start:
                        commit_msg = line[start:end]
                        if commit_msg and len(commit_msg) > 5:
                            return commit_msg, None
                            
            # Fallback: look for any substantial line that might be a commit message
            for line in lines:
                line = line.strip()
                if line and not line.startswith('$') and not line.startswith('#') and len(line) > 10:
                    # Clean up common prefixes
                    commit_msg = line.replace('git commit -m ', '').replace('"', '').strip()
                    if commit_msg and len(commit_msg) > 5:
                        return commit_msg, None
        
        # If Copilot didn't provide a good response, use smart fallback
        return generate_smart_commit_message(changes_summary)
        
    except subprocess.TimeoutExpired:
        print("⚠️ GitHub Copilot timed out, using smart generation...")
        return generate_smart_commit_message(changes_summary)
    except Exception as e:
        print(f"⚠️ GitHub Copilot error: {str(e)}, using smart generation...")
        return generate_smart_commit_message(changes_summary)

def generate_smart_commit_message(changes_summary):
    """Generate an intelligent, human-readable commit message based on actual file changes"""
    try:
        if not changes_summary:
            return None, "No changes detected."
        
        # Get detailed diff information for better analysis
        try:
            diff_result = subprocess.run("git diff HEAD --numstat", shell=True, capture_output=True, text=True, timeout=10)
            diff_lines = diff_result.stdout.strip().split('\n') if diff_result.stdout.strip() else []
        except:
            diff_lines = []
        
        # Get specific file changes with context
        file_changes = {}
        for line in diff_lines:
            if line.strip():
                parts = line.split('\t')
                if len(parts) >= 3:
                    added = parts[0] if parts[0] != '-' else '0'
                    deleted = parts[1] if parts[1] != '-' else '0'
                    filename = parts[2]
                    file_changes[filename] = {'added': added, 'deleted': deleted}
        
        # Parse basic file operations
        lines = changes_summary.strip().split('\n')
        modified_files = []
        added_files = []
        deleted_files = []
        
        for line in lines:
            if line.startswith(' M '):
                modified_files.append(line[3:])
            elif line.startswith(' A ') or line.startswith('A '):
                added_files.append(line[3:])
            elif line.startswith(' D ') or line.startswith('D '):
                deleted_files.append(line[3:])
        
        # Generate human-readable, specific commit message based on actual changes
        specific_changes = []
        
        # Analyze each modified file in detail
        for filename in modified_files:
            try:
                # Get specific changes for this file
                file_info = file_changes.get(filename, {})
                added = file_info.get('added', '0')
                deleted = file_info.get('deleted', '0')
                
                # Generate specific descriptions based on file type and changes
                if filename == '.vscode/git_sync.py':
                    if int(added) > 100:  # Major changes
                        specific_changes.append(f"Enhanced git_sync.py with {added} line improvements for better PR and commit message generation")
                    else:
                        specific_changes.append(f"Updated git_sync.py with {added} line improvements")
                elif filename == '.vscode/auto_sync.py':
                    specific_changes.append(f"Improved auto_sync.py with {added} new lines for better automation")
                elif filename == '.vscode/sync-repo.sh':
                    specific_changes.append(f"Updated sync-repo.sh script with better temporary file handling")
                elif 'Documentation/' in filename:
                    if 'Collaboration-Process' in filename:
                        specific_changes.append(f"Updated collaboration process documentation in {os.path.basename(filename)}")
                    else:
                        specific_changes.append(f"Updated {os.path.basename(filename)} documentation")
                elif filename.endswith('.py'):
                    specific_changes.append(f"Improved {os.path.basename(filename)} Python script")
                elif filename.endswith('.md'):
                    specific_changes.append(f"Updated {os.path.basename(filename)} documentation")
                else:
                    specific_changes.append(f"Modified {os.path.basename(filename)}")
                    
            except:
                specific_changes.append(f"Updated {os.path.basename(filename)}")
        
        # Handle added files
        for filename in added_files:
            if '.vscode/tmp/' in filename and 'tmp_dialog' in filename:
                continue  # Skip temporary dialog files in description
            else:
                specific_changes.append(f"Added new file {os.path.basename(filename)}")
        
        # Handle deleted files  
        temp_deletions = [f for f in deleted_files if 'tmp_dialog' in f or '.tmp' in f]
        regular_deletions = [f for f in deleted_files if f not in temp_deletions]
        
        if temp_deletions:
            specific_changes.append(f"Cleaned up {len(temp_deletions)} temporary dialog files")
        
        for filename in regular_deletions:
            specific_changes.append(f"Removed {os.path.basename(filename)}")
        
        # Create final human-readable commit message
        if not specific_changes:
            return "Updated project files with minor changes", None
            
        if len(specific_changes) == 1:
            commit_msg = specific_changes[0].capitalize()
        elif len(specific_changes) == 2:
            commit_msg = f"{specific_changes[0].capitalize()} and {specific_changes[1]}"
        else:
            # For multiple changes, create a summary
            main_change = specific_changes[0].capitalize()
            other_count = len(specific_changes) - 1
            commit_msg = f"{main_change} and {other_count} other improvements"
        
        return commit_msg, None
        
    except Exception as e:
        return "chore: update files", None

def generate_copilot_pr_details(commit_message=None):
    """Generate PR title and description using GitHub Copilot"""
    try:
        print("🤖 Generating PR title and description using GitHub Copilot...")
        
        # Get detailed diff for better context
        try:
            diff_result = subprocess.run("git diff --cached --stat", shell=True, capture_output=True, text=True, timeout=10)
            diff_summary = diff_result.stdout.strip()
            
            # Get file changes list
            status_result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True, timeout=5)
            changes_summary = status_result.stdout.strip()
        except:
            diff_summary = ""
            changes_summary = ""
        
        # Try to generate both title and description separately
        pr_title = None
        pr_description = None
        
        # Generate title first - should be concise
        if commit_message:
            title_context = f"Generate a concise PR title (max 60 chars) for this commit: {commit_message}"
        else:
            title_context = f"Generate a concise PR title for changes: {changes_summary[:200]}"
        
        try:
            title_result = subprocess.run(
                ["gh", "copilot", "suggest", "-t", "gh", title_context],
                capture_output=True, text=True, timeout=20
            )
            
            if title_result.returncode == 0 and title_result.stdout.strip():
                lines = title_result.stdout.strip().split('\n')
                for line in lines:
                    if 'gh pr create' in line and '--title' in line:
                        parts = line.split('--title')
                        if len(parts) > 1:
                            title_part = parts[1].strip()
                            if title_part.startswith('"'):
                                end_quote = title_part.find('"', 1)
                                if end_quote > 0:
                                    pr_title = title_part[1:end_quote]
                                    break
        except:
            pass
        
        # Generate description - should be detailed
        if diff_summary or changes_summary:
            desc_context = f"Generate a detailed PR description explaining these changes:\n{diff_summary}\nFiles changed: {changes_summary}"
        elif commit_message:
            desc_context = f"Generate a detailed PR description explaining the changes in this commit: {commit_message}"
        else:
            desc_context = "Generate a PR description for code changes"
        
        try:
            desc_result = subprocess.run(
                ["gh", "copilot", "suggest", "-t", "shell", desc_context],
                capture_output=True, text=True, timeout=20
            )
            
            if desc_result.returncode == 0 and desc_result.stdout.strip():
                # Extract meaningful description from response
                desc_lines = desc_result.stdout.strip().split('\n')
                description_parts = []
                for line in desc_lines:
                    line = line.strip()
                    if line and not line.startswith('$') and not line.startswith('#') and len(line) > 10:
                        # Skip command suggestions, keep descriptive text
                        if not any(cmd in line.lower() for cmd in ['git', 'gh ', 'echo', 'cat', 'ls']):
                            description_parts.append(line)
                
                if description_parts:
                    pr_description = '\n'.join(description_parts[:3])  # Take first few good lines
        except:
            pass
        
        # Fallbacks with smart generation
        if not pr_title:
            if commit_message:
                # Extract first part of commit message for title
                pr_title = commit_message.split('\n')[0][:60]  # Limit to 60 chars
            else:
                pr_title = generate_smart_pr_title(changes_summary)
        
        if not pr_description or pr_description == pr_title:
            pr_description = generate_smart_pr_description(changes_summary, diff_summary, commit_message)
        
        return pr_title, pr_description, None
        
    except subprocess.TimeoutExpired:
        return None, None, "Copilot request timed out. Using manual input."
    except Exception as e:
        return None, None, f"Error generating PR details with Copilot: {str(e)}"

def generate_smart_pr_title(changes_summary):
    """Generate a specific, human-readable PR title based on actual file changes"""
    if not changes_summary:
        return "Update project files"
    
    # Get detailed diff information
    try:
        diff_result = subprocess.run("git diff HEAD --numstat", shell=True, capture_output=True, text=True, timeout=10)
        diff_lines = diff_result.stdout.strip().split('\n') if diff_result.stdout.strip() else []
        
        file_changes = {}
        for line in diff_lines:
            if line.strip():
                parts = line.split('\t')
                if len(parts) >= 3:
                    added = parts[0] if parts[0] != '-' else '0'
                    filename = parts[2]
                    file_changes[filename] = {'added': int(added) if added.isdigit() else 0}
    except:
        file_changes = {}
    
    lines = changes_summary.strip().split('\n')
    modified_files = []
    added_files = []
    deleted_files = []
    
    for line in lines:
        if line.startswith(' M '):
            modified_files.append(line[3:])
        elif line.startswith(' A ') or line.startswith('A '):
            added_files.append(line[3:])
        elif line.startswith(' D ') or line.startswith('D '):
            deleted_files.append(line[3:])
    
    # Generate specific, human-readable title
    main_changes = []
    
    # Analyze major changes first
    for filename in modified_files:
        file_info = file_changes.get(filename, {})
        added_lines = file_info.get('added', 0)
        
        if filename == '.vscode/git_sync.py' and added_lines > 100:
            main_changes.append("Improve GitHub sync script with better PR generation")
        elif filename == '.vscode/git_sync.py':
            main_changes.append("Update git_sync.py script")
        elif filename == '.vscode/auto_sync.py':
            main_changes.append("Enhance auto_sync.py automation")
        elif filename == '.vscode/sync-repo.sh':
            main_changes.append("Update sync-repo.sh script")
        elif 'Documentation/' in filename:
            if 'Collaboration-Process' in filename:
                main_changes.append("Update collaboration process documentation")
            else:
                main_changes.append(f"Update {os.path.basename(filename)} documentation")
        elif filename.endswith('.py'):
            main_changes.append(f"Improve {os.path.basename(filename)} script")
        elif filename.endswith('.md'):
            main_changes.append(f"Update {os.path.basename(filename)}")
    
    # Handle file operations
    if deleted_files:
        temp_files = [f for f in deleted_files if 'tmp_dialog' in f or '.tmp' in f]
        if temp_files and not main_changes:
            main_changes.append("Clean up temporary files")
    
    if not main_changes and added_files:
        main_changes.append(f"Add {len(added_files)} new files")
    
    # Create concise title
    if not main_changes:
        return "Update project files"
    elif len(main_changes) == 1:
        return main_changes[0]
    else:
        # Priority: major script changes first
        primary = main_changes[0]
        if len(main_changes) == 2:
            return f"{primary} and {main_changes[1].lower()}"
        else:
            return f"{primary} and {len(main_changes)-1} other updates"

def generate_smart_pr_description(changes_summary, diff_summary, commit_message):
    """Generate a detailed, human-readable PR description based on actual changes"""
    description_parts = []
    
    # Get detailed diff for better analysis
    try:
        diff_result = subprocess.run("git diff HEAD --numstat", shell=True, capture_output=True, text=True, timeout=10)
        diff_lines = diff_result.stdout.strip().split('\n') if diff_result.stdout.strip() else []
        
        file_changes = {}
        for line in diff_lines:
            if line.strip():
                parts = line.split('\t')
                if len(parts) >= 3:
                    added = parts[0] if parts[0] != '-' else '0'
                    deleted = parts[1] if parts[1] != '-' else '0'
                    filename = parts[2]
                    file_changes[filename] = {
                        'added': int(added) if added.isdigit() else 0,
                        'deleted': int(deleted) if deleted.isdigit() else 0
                    }
    except:
        file_changes = {}
    
    # Add summary
    if commit_message:
        description_parts.append(f"## What Changed\n{commit_message}")
    
    if changes_summary:
        lines = changes_summary.strip().split('\n')
        modified_files = []
        added_files = []
        deleted_files = []
        
        for line in lines:
            if line.startswith(' M '):
                modified_files.append(line[3:])
            elif line.startswith(' A ') or line.startswith('A '):
                added_files.append(line[3:])
            elif line.startswith(' D ') or line.startswith('D '):
                deleted_files.append(line[3:])
        
        # Create detailed descriptions for each significant change
        if modified_files:
            description_parts.append("## Detailed Changes")
            
            for filename in modified_files:
                file_info = file_changes.get(filename, {})
                added_lines = file_info.get('added', 0)
                deleted_lines = file_info.get('deleted', 0)
                
                if filename == '.vscode/git_sync.py':
                    if added_lines > 100:
                        description_parts.append(f"### Enhanced git_sync.py (+{added_lines} lines)")
                        description_parts.append("- Completely rewrote PR title and description generation to be more specific and human-readable")
                        description_parts.append("- Improved commit message generation to analyze actual file changes instead of using generic templates")
                        description_parts.append("- Added detailed file analysis to create contextual descriptions")
                        description_parts.append("- Removed generic 'feat:' and 'docs:' prefixes in favor of natural language")
                    else:
                        description_parts.append(f"### Updated git_sync.py (+{added_lines} lines)")
                        description_parts.append("- Made improvements to the GitHub sync functionality")
                
                elif filename == '.vscode/auto_sync.py':
                    description_parts.append(f"### Enhanced auto_sync.py (+{added_lines} lines)")
                    description_parts.append("- Improved automation script functionality")
                    
                elif filename == '.vscode/sync-repo.sh':
                    description_parts.append(f"### Updated sync-repo.sh (+{added_lines} lines)")
                    description_parts.append("- Enhanced repository synchronization script")
                    
                elif 'Documentation/' in filename:
                    if 'Collaboration-Process' in filename:
                        description_parts.append(f"### Updated Collaboration-Process.md")
                        description_parts.append("- Made minor updates to the collaboration process documentation")
                    else:
                        description_parts.append(f"### Updated {os.path.basename(filename)}")
                        description_parts.append(f"- Made improvements to {os.path.basename(filename)} documentation")
                        
                elif filename.endswith('.py'):
                    description_parts.append(f"### Improved {os.path.basename(filename)} (+{added_lines} lines)")
                    description_parts.append(f"- Enhanced Python script functionality")
                    
                elif filename.endswith('.md'):
                    description_parts.append(f"### Updated {os.path.basename(filename)}")
                    description_parts.append(f"- Made updates to documentation")
        
        # Handle additions and deletions
        if added_files:
            non_temp_files = [f for f in added_files if '.vscode/tmp/' not in f or 'tmp_dialog' not in f]
            if non_temp_files:
                description_parts.append(f"### Added New Files ({len(non_temp_files)})")
                for file in non_temp_files[:5]:
                    description_parts.append(f"- `{file}`")
        
        if deleted_files:
            temp_files = [f for f in deleted_files if 'tmp_dialog' in f or '.tmp' in f]
            regular_files = [f for f in deleted_files if f not in temp_files]
            
            if temp_files:
                description_parts.append(f"### Cleanup")
                description_parts.append(f"- Removed {len(temp_files)} temporary dialog files to keep workspace clean")
            
            if regular_files:
                description_parts.append(f"### Removed Files")
                for file in regular_files:
                    description_parts.append(f"- `{file}`")
    
    # Add technical details if available
    if diff_summary and any(char.isdigit() for char in diff_summary):
        description_parts.append(f"## Technical Summary")
        description_parts.append(f"```\n{diff_summary}\n```")
    
    if not description_parts:
        return "This pull request includes various improvements and updates to the project files."
    
    return '\n'.join(description_parts)

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
        merge_pr = False
        pr_target = None
        
    elif "Push to main" in push_option:
        # Push to main branch via pull request (like the original script)
        print(f"🔄 Will push {current_branch} and create pull request to main")
        target_branch = current_branch  # Push to current branch first, then PR to main
        create_pr = True
        sync_testing = True
        pr_target = "main"  # Target for the PR
        
        # Ask about immediate merge (like the original script did)
        merge_response = get_vscode_input(
            f"Would you also like to merge the pull request to main immediately?",
            ["Yes, merge immediately", "No, leave for review"]
        )
        
        if merge_response and "Yes" in merge_response:
            merge_pr = True
            print("📋 Will create PR and merge to main, then sync Testing")
        else:
            merge_pr = False
            print("📋 Will create PR to main for review, then sync Testing")
            
    elif "Push to Testing" in push_option:
        # Push to Testing branch
        if current_branch == "Testing":
            print("🔄 Will push to Testing branch")
            target_branch = "Testing"
            create_pr = False
            sync_testing = False
            merge_pr = False
            pr_target = None
        else:
            print(f"🔄 Will push {current_branch} changes to Testing branch")
            target_branch = "Testing"
            create_pr = False
            sync_testing = False
            merge_pr = False
            pr_target = None
            
    elif "Create pull request" in push_option:
        # Create PR workflow
        print(f"🔄 Will push {current_branch} and create pull request")
        create_pr = True
        sync_testing = False
        pr_target = None
        
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
        # Use Copilot to generate commit message directly
        generated_msg, error = generate_copilot_commit_message()
        
        if generated_msg:
            # Show the commit message in the dialog prompt
            dialog_message = f"Would you like to use this Copilot-generated commit message?\n\nCommit message: \"{generated_msg}\""
            
            copilot_choice = get_vscode_input(
                dialog_message,
                ["Yes, use this message", "No, let me edit it", "No, write manually instead"]
            )
            
            if copilot_choice and "Yes" in copilot_choice:
                commit_message = generated_msg
            elif copilot_choice and "edit" in copilot_choice:
                print(f"Edit the Copilot suggestion:")
                edited_message = get_vscode_input("Commit message (edit as needed)", None, generated_msg)
                final_message = edited_message if edited_message else generated_msg
                
                # Show confirmation dialog with the edited message
                confirm_edit = get_vscode_input(
                    f"Is this commit message correct?\n\nCommit message: \"{final_message}\"",
                    ["Yes, use this message", "No, let me edit it again", "No, write manually instead"]
                )
                
                if confirm_edit and "Yes" in confirm_edit:
                    commit_message = final_message
                elif confirm_edit and "edit it again" in confirm_edit:
                    # Allow editing again
                    re_edited_message = get_vscode_input("Commit message (edit again)", None, final_message)
                    commit_message = re_edited_message if re_edited_message else final_message
                else:
                    # Manual entry with confirmation
                    manual_message = get_vscode_input("Enter your commit message manually")
                    
                    if manual_message:
                        # Show confirmation dialog with the manual message
                        confirm_manual = get_vscode_input(
                            f"Is this commit message correct?\n\nCommit message: \"{manual_message}\"",
                            ["Yes, use this message", "No, let me edit it", "Use the auto-generated one instead"]
                        )
                        
                        if confirm_manual and "Yes" in confirm_manual:
                            commit_message = manual_message
                        elif confirm_manual and "edit" in confirm_manual:
                            # Allow editing the manual message
                            edited_manual = get_vscode_input("Commit message (edit as needed)", None, manual_message)
                            commit_message = edited_manual if edited_manual else manual_message
                        elif confirm_manual and "auto-generated" in confirm_manual:
                            # Use the original Copilot suggestion
                            commit_message = generated_msg
                        else:
                            commit_message = manual_message
                    else:
                        # If no manual message entered, use Copilot suggestion
                        commit_message = generated_msg
            else:
                # Manual entry with confirmation
                manual_message = get_vscode_input("Enter your commit message manually")
                
                if manual_message:
                    # Show confirmation dialog with the manual message
                    confirm_manual = get_vscode_input(
                        f"Is this commit message correct?\n\nCommit message: \"{manual_message}\"",
                        ["Yes, use this message", "No, let me edit it", "Use the auto-generated one instead"]
                    )
                    
                    if confirm_manual and "Yes" in confirm_manual:
                        commit_message = manual_message
                    elif confirm_manual and "edit" in confirm_manual:
                        # Allow editing the manual message
                        edited_manual = get_vscode_input("Commit message (edit as needed)", None, manual_message)
                        commit_message = edited_manual if edited_manual else manual_message
                    elif confirm_manual and "auto-generated" in confirm_manual:
                        # Use the original Copilot suggestion
                        commit_message = generated_msg
                    else:
                        commit_message = manual_message
                else:
                    # If no manual message entered, use Copilot suggestion
                    commit_message = generated_msg
        else:
            show_vscode_notification(f"⚠️ Copilot generation failed: {error}", "warning")
            print(f"⚠️ Copilot generation failed: {error}")
            # Fall back to manual entry with confirmation
            manual_message = get_vscode_input("Enter your commit message manually")
            
            if manual_message:
                # Show confirmation dialog with the manual message
                confirm_manual = get_vscode_input(
                    f"Is this commit message correct?\n\nCommit message: \"{manual_message}\"",
                    ["Yes, use this message", "No, let me edit it"]
                )
                
                if confirm_manual and "Yes" in confirm_manual:
                    commit_message = manual_message
                else:
                    # Allow editing the manual message
                    edited_manual = get_vscode_input("Commit message (edit as needed)", None, manual_message)
                    commit_message = edited_manual if edited_manual else manual_message
            else:
                commit_message = "Update files"  # Default fallback
        
        if not commit_message:
            show_vscode_notification("❌ Commit message is required. Cancelling sync.", "error")
            return
        
        # Confirm commit message
        confirm_message = get_vscode_input(
            f"Is this commit message correct?\n\nCommit message: \"{commit_message}\"",
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
        
        # Use Copilot to generate PR details directly
        generated_title, generated_body, error = generate_copilot_pr_details(commit_message)
        
        pr_title = None
        pr_body = None
        
        if generated_title and generated_body:
            # Show the PR details in the dialog prompt
            dialog_message = f"Would you like to use these Copilot-generated PR details?\n\nTitle: \"{generated_title}\"\n\nDescription: \"{generated_body[:200]}{'...' if len(generated_body) > 200 else ''}\""
            
            copilot_pr_choice = get_vscode_input(
                dialog_message,
                ["Yes, use both title and description", "Yes, but let me edit them", "No, write manually"]
            )
            
            if copilot_pr_choice and "use both" in copilot_pr_choice:
                pr_title = generated_title
                pr_body = generated_body
            elif copilot_pr_choice and "edit" in copilot_pr_choice:
                # Allow editing of generated content
                print(f"Edit the Copilot-generated title:")
                edited_title = get_vscode_input("PR title (edit as needed)", None, generated_title)
                final_title = edited_title if edited_title else generated_title
                
                print(f"Edit the Copilot-generated description:")
                edited_body = get_vscode_input("PR description (edit as needed)", None, generated_body)
                final_body = edited_body if edited_body else generated_body
                
                # Show confirmation dialog with the edited PR details
                confirm_edit = get_vscode_input(
                    f"Are these PR details correct?\n\nTitle: \"{final_title}\"\n\nDescription: \"{final_body[:200]}{'...' if len(final_body) > 200 else ''}\"",
                    ["Yes, use these details", "No, let me edit them again", "No, write manually instead"]
                )
                
                if confirm_edit and "Yes" in confirm_edit:
                    pr_title = final_title
                    pr_body = final_body
                elif confirm_edit and "edit them again" in confirm_edit:
                    # Allow editing again
                    print(f"Edit the title again:")
                    re_edited_title = get_vscode_input("PR title (edit again)", None, final_title)
                    pr_title = re_edited_title if re_edited_title else final_title
                    
                    print(f"Edit the description again:")
                    re_edited_body = get_vscode_input("PR description (edit again)", None, final_body)
                    pr_body = re_edited_body if re_edited_body else final_body
                else:
                    # Manual entry with confirmation
                    manual_title = get_vscode_input("Enter pull request title (or press Enter to use commit message)")
                    manual_body = get_vscode_input("Enter pull request description (optional)")
                    
                    final_manual_title = manual_title if manual_title else (commit_message if commit_message else f"Changes from {current_branch}")
                    final_manual_body = manual_body if manual_body else (commit_message if commit_message else "Automated pull request created by git sync script.")
                    
                    # Show confirmation dialog
                    confirm_manual_pr = get_vscode_input(
                        f"Are these PR details correct?\n\nTitle: \"{final_manual_title}\"\n\nDescription: \"{final_manual_body[:200]}{'...' if len(final_manual_body) > 200 else ''}\"",
                        ["Yes, use these details", "No, let me edit them", "Use the auto-generated ones instead"]
                    )
                    
                    if confirm_manual_pr and "Yes" in confirm_manual_pr:
                        pr_title = final_manual_title
                        pr_body = final_manual_body
                    elif confirm_manual_pr and "edit" in confirm_manual_pr:
                        # Allow editing
                        edited_title = get_vscode_input("PR title (edit as needed)", None, final_manual_title)
                        edited_body = get_vscode_input("PR description (edit as needed)", None, final_manual_body)
                        pr_title = edited_title if edited_title else final_manual_title
                        pr_body = edited_body if edited_body else final_manual_body
                    elif confirm_manual_pr and "auto-generated" in confirm_manual_pr:
                        # Use the original Copilot suggestions
                        pr_title = generated_title
                        pr_body = generated_body
                    else:
                        pr_title = final_manual_title
                        pr_body = final_manual_body
            else:
                # Fall back to manual entry
                pr_title = get_vscode_input("Enter pull request title (or press Enter to use commit message)")
                pr_body = get_vscode_input("Enter pull request description (optional)")
        else:
            show_vscode_notification(f"⚠️ Copilot PR generation failed: {error}", "warning")
            print(f"⚠️ Copilot PR generation failed: {error}")
            # Fall back to manual entry with confirmation
            manual_title = get_vscode_input("Enter pull request title (or press Enter to use commit message)")
            manual_body = get_vscode_input("Enter pull request description (optional)")
            
            final_manual_title = manual_title if manual_title else (commit_message if commit_message else f"Changes from {current_branch}")
            final_manual_body = manual_body if manual_body else (commit_message if commit_message else "Automated pull request created by git sync script.")
            
            # Show confirmation dialog
            confirm_manual_pr = get_vscode_input(
                f"Are these PR details correct?\n\nTitle: \"{final_manual_title}\"\n\nDescription: \"{final_manual_body[:200]}{'...' if len(final_manual_body) > 200 else ''}\"",
                ["Yes, use these details", "No, let me edit them"]
            )
            
            if confirm_manual_pr and "Yes" in confirm_manual_pr:
                pr_title = final_manual_title
                pr_body = final_manual_body
            else:
                # Allow editing
                edited_title = get_vscode_input("PR title (edit as needed)", None, final_manual_title)
                edited_body = get_vscode_input("PR description (edit as needed)", None, final_manual_body)
                pr_title = edited_title if edited_title else final_manual_title
                pr_body = edited_body if edited_body else final_manual_body
        
        # Set defaults if nothing was provided
        if not pr_title and commit_message:
            pr_title = commit_message
        elif not pr_title:
            pr_title = f"Changes from {current_branch}"
        
        if not pr_body:
            pr_body = commit_message if commit_message else "Automated pull request created by git sync script."
        
        # Create the pull request - use pr_target if it exists, otherwise target_branch
        pr_base = pr_target if 'pr_target' in locals() else target_branch
        pr_command = f'gh pr create --title "{pr_title}" --base {pr_base} --head {current_branch} --body "{pr_body}"'
        
        pr_result = run_command_execute(pr_command, f"Create pull request: {current_branch} → {pr_base}")
        
        if pr_result and pr_result.returncode == 0:
            show_vscode_notification(f"✅ Pull request created successfully! ({current_branch} → {pr_base})", "success")
            print(f"✅ Pull request created successfully! ({current_branch} → {pr_base})")
            
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
                merge_result = run_command_execute(merge_command, f"Merge pull request to {pr_base}")
                
                if merge_result and merge_result.returncode == 0:
                    show_vscode_notification(f"✅ Pull request merged to {pr_base} successfully!", "success")
                    print(f"✅ Pull request merged to {pr_base} successfully!")
                    
                    # Switch to target branch and pull the merged changes
                    print(f"\n{step_counter + 2}️⃣  Updating local {pr_base} branch...")
                    checkout_result = run_command_execute(f"git checkout {pr_base}", f"Switch to {pr_base} branch")
                    if checkout_result and checkout_result.returncode == 0:
                        pull_result = run_command_execute("git pull", f"Pull merged changes to {pr_base}")
                        if pull_result and pull_result.returncode == 0:
                            show_vscode_notification(f"✅ Local {pr_base} branch updated with merged changes!", "success")
                            
                            # If merged to main, also sync Testing branch to keep it up to date
                            if pr_base == "main":
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
    
    # Clean up any temporary files
    cleanup_temp_files()

def cleanup_temp_files():
    """Clean up temporary HTML files created by the script"""
    try:
        # Clean up .vscode/tmp directory temp files
        tmp_dir = '.vscode/tmp'
        if os.path.exists(tmp_dir):
            for file in os.listdir(tmp_dir):
                if file.startswith('.tmp_dialog_') and file.endswith('.html'):
                    try:
                        print(f"🧹 Cleaning up temp file: {file}")
                        os.unlink(os.path.join(tmp_dir, file))
                    except:
                        pass
        
        # Clean up old temp files in current directory (for backward compatibility)
        for file in os.listdir('.'):
            if file.startswith('.tmp_dialog_') and file.endswith('.html'):
                try:
                    print(f"🧹 Cleaning up old temp file: {file}")
                    os.unlink(file)
                except:
                    pass
        
        # Clean up system temp directory HTML files (from older versions)
        import glob
        temp_pattern = os.path.join(tempfile.gettempdir(), 'tmp*.html')
        for html_file in glob.glob(temp_pattern):
            try:
                # Only delete files that are more than 10 minutes old to avoid conflicts
                if os.path.getmtime(html_file) < time.time() - 600:
                    print(f"🧹 Cleaning up old temp file: {os.path.basename(html_file)}")
                    os.unlink(html_file)
            except:
                pass
                
        # Note: We no longer open files in VS Code browser to avoid tab issues
            
    except Exception as e:
        # Don't fail the script for cleanup issues
        pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cleanup_temp_files()
        show_vscode_notification("⚠️ Script interrupted by user. Exiting...", "warning")
        print("\n\n⚠️  Script interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        cleanup_temp_files()
        show_vscode_notification(f"❌ Unexpected error: {e}", "error")
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)