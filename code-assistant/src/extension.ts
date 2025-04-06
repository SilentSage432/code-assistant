import * as vscode from 'vscode';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
	console.log('Code Assistant extension is now active!');
  context.subscriptions.push(
    vscode.commands.registerCommand('code-assistant.openPanel', () => {
      const panel = vscode.window.createWebviewPanel(
        'codeAssistant',
        '👽 Code Assistant',
        vscode.ViewColumn.One,
        {
          enableScripts: true,
          localResourceRoots: [
            vscode.Uri.joinPath(context.extensionUri, 'media')
          ]
        }
      );

      panel.webview.html = `
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Code Assistant</title>
          <link rel="stylesheet" href="${panel.webview.asWebviewUri(vscode.Uri.joinPath(context.extensionUri, 'media', 'style.css'))}">
          <link rel="icon" href="${panel.webview.asWebviewUri(vscode.Uri.joinPath(context.extensionUri, 'media', 'alien.png'))}">
        </head>
        <body>
          <h1>👽 Code Assistant Loaded</h1>
          <p>This is where your full UI will be injected.</p>
          <script src="${panel.webview.asWebviewUri(vscode.Uri.joinPath(context.extensionUri, 'media', 'main.js'))}"></script>
        </body>
        </html>
      `;
    })
  );
}

export function deactivate() {}