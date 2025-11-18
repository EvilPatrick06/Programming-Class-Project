# How to Add Folders to the Repository

This guide explains how to add new folders to the CtrlUno Arcade project repository.

## Understanding Git and Folders

Git tracks files, not empty folders. To add a folder to the repository, you must include at least one file in it.

## Steps to Add a New Folder

### Method 1: Using the Terminal/Command Line

1. **Navigate to the repository directory:**
   ```bash
   cd /path/to/Programming-Class-Project
   ```

2. **Create a new folder:**
   ```bash
   mkdir YourFolderName
   ```

3. **Add a file to the folder** (Git won't track empty folders):
   ```bash
   # Option A: Create a README file
   echo "# YourFolderName" > YourFolderName/README.md
   
   # Option B: Create a placeholder file
   touch YourFolderName/.gitkeep
   ```

4. **Add the folder to Git:**
   ```bash
   git add YourFolderName/
   ```

5. **Commit your changes:**
   ```bash
   git commit -m "Add YourFolderName folder"
   ```

6. **Push to GitHub:**
   ```bash
   git push
   ```

### Method 2: Using VS Code

1. **Open the repository in VS Code**
2. **Right-click in the Explorer panel**
3. **Select "New Folder"**
4. **Name your folder**
5. **Create a file inside the folder** (e.g., `README.md`)
6. **Use the Source Control panel to stage, commit, and push changes**

## Best Practices

- **Add a README.md**: Always include a README.md file in new folders to explain their purpose
- **Use meaningful names**: Choose descriptive folder names that clearly indicate their purpose
- **Follow project structure**: Match the existing folder organization pattern
- **Document changes**: Update relevant documentation when adding significant new folders

## Common Folder Types in This Project

- **Personal workspace folders**: Named after team members (e.g., Gavin, Jabriel, Joshua) for individual work
- **Backups**: For backup copies of important files
- **CtrUnoArcade**: Main project structure with Arcade and Documentation subfolders
- **test**: For test files and test data

## Example: Adding a Personal Workspace Folder

```bash
# Create folder
mkdir Joshua

# Add a README file
cat > Joshua/README.md << EOF
# Joshua's Personal Workspace

This folder contains Joshua Casey's personal work files for the CtrlUno Arcade project.
EOF

# Stage and commit
git add Joshua/
git commit -m "Add Joshua's personal workspace folder"

# Push to GitHub
git push
```

## Troubleshooting

**Q: My folder isn't showing up in Git**
- A: Make sure the folder contains at least one file. Git doesn't track empty folders.

**Q: Should I add build artifacts or dependencies?**
- A: No, use `.gitignore` to exclude folders like `node_modules`, `__pycache__`, or `dist`.

**Q: How do I know what folders to create?**
- A: Consult with your team and follow the existing project structure. Check the Collaboration-Process.md for team workflows.

## Related Documentation

- [Collaboration Process Guide](Collaboration-Process.md)
- [Git Sync Guide](Git-Sync-Guide.md)

---

For questions or issues, consult with your team members or refer to the GitHub documentation.
