# Team Collaboration Process Guide

This document outlines our team's workflow for collaborating on code using GitHub, Codespaces, and Visual Studio Code.

## Repository Structure Overview

- **Repository (Repo)**: Contains our complete collection of project files
- **Main Branch**: Houses our current stable, working files
- **Testing Branch**: Contains files currently being tested or developed
- **Codespace**: Individual Linux virtual machines with development tools for creating, testing, and collaborating on files
  - Each codespace is personalized and isolated - team members cannot access each other's codespaces directly
  - Codespaces are separate Linux VMs with potentially different files and extensions, but can be synchronized

## Collaboration Tools

### Live Share Extension

The Visual Studio Code Live Share extension enables real-time collaboration by allowing you to invite team members to your VSC environment. Note that Live Share only works when the host has an active session running.

## Making Changes to the Repository

### Step 1: Synchronize Changes

Run `git_sync.py` and select the appropriate option based on your situation:

- **Testing Branch Only**: Choose this when working on features that aren't fully functional yet
- **Main Branch**: Select this when you're confident the current state is stable and nothing is broken
  - **Important**: You can still test after committing to main, but DO NOT delete the testing branch

## Remote Collaboration (When Direct Collaboration Isn't Possible)

Follow these steps when team members want to work together but the primary developer isn't available:

### Step 1: Set Up Codespace

1. Create or open a codespace under the Testing Branch
2. Follow the prompts in terminal when codespace is opened to update the vm, VSC extensions, and clone the repository

### Step 2: Configure Environment

1. Follow the prompts in terminal to set up the development environment
2. Launch Live Share
3. Share the Live Share link with team members

### Step 4: Collaborate and Commit

1. Work collaboratively through Live Share
2. When ready, make changes using the same process outlined in "Making Changes to the Repository"

## Best Practices

- Always ensure the main branch remains intact
- Communicate with team members before making changes to the main branch
- Use descriptive commit messages
- Test thoroughly before promoting code from testing to main branch
