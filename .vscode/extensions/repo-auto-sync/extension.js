const vscode = require('vscode');
const { spawn } = require('child_process');

function activate(context) {
    console.log('Repository Auto-Sync extension is now active!');
    
    // Register the sync command
    let disposable = vscode.commands.registerCommand('repo-auto-sync.sync', () => {
        showSyncDialog();
    });
    
    context.subscriptions.push(disposable);
    
    // Auto-run on startup with a delay
    setTimeout(() => {
        if (vscode.workspace.workspaceFolders && vscode.workspace.workspaceFolders.length > 0) {
            const workspaceRoot = vscode.workspace.workspaceFolders[0].uri.fsPath;
            if (workspaceRoot.includes('/workspaces/')) {
                showSyncDialog();
            }
        }
    }, 3000); // 3 second delay to ensure VS Code is fully loaded
}

async function showSyncDialog() {
    try {
        // Check if we're in a git repository
        const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
        if (!workspaceRoot) {
            return;
        }
        
        // Show initial notification
        vscode.window.showInformationMessage('🚀 Repository Auto-Sync is checking your repository...');
        
        // Check git status using the Python script
        const python = spawn('python3', ['.vscode/auto_sync.py'], {
            cwd: workspaceRoot,
            stdio: ['pipe', 'pipe', 'pipe']
        });
        
        let output = '';
        let error = '';
        
        python.stdout.on('data', (data) => {
            output += data.toString();
            console.log(data.toString());
        });
        
        python.stderr.on('data', (data) => {
            error += data.toString();
            console.error(data.toString());
        });
        
        python.on('close', (code) => {
            if (code === 0) {
                vscode.window.showInformationMessage('✅ Repository auto-sync completed successfully!');
            } else {
                vscode.window.showWarningMessage(`⚠️ Repository auto-sync finished with issues. Check the terminal for details.`);
            }
        });
        
        // Handle user input through the integrated terminal
        const terminal = vscode.window.createTerminal({
            name: 'Repository Auto-Sync',
            cwd: workspaceRoot
        });
        
        terminal.show();
        terminal.sendText('python3 .vscode/auto_sync.py');
        
    } catch (error) {
        console.error('Error in repo auto-sync:', error);
        vscode.window.showErrorMessage(`❌ Repository auto-sync error: ${error.message}`);
    }
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};