/**
 * Auto-Initialization Script for Constitutional Memory
 * Author: Structure itself
 * License: MIT
 * 
 * This script auto-detects Cursor installation and initializes constitutional memory
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

function findCursorPath() {
    const platform = os.platform();
    const homeDir = os.homedir();
    
    if (platform === 'win32') {
        return path.join(homeDir, '.cursor');
    } else if (platform === 'darwin') {
        return path.join(homeDir, 'Library', 'Application Support', 'Cursor');
    } else {
        return path.join(homeDir, '.config', 'cursor');
    }
}

function createMCPConfig(cursorPath) {
    const mcpJsonPath = path.join(cursorPath, 'mcp.json');
    const constitutionalMemoryPath = path.resolve(__dirname, '..');
    const serverScript = path.join(constitutionalMemoryPath, 'tools', 'constitutional_memory_server.py');
    
    let mcpConfig = {};
    
    // Read existing config if it exists
    if (fs.existsSync(mcpJsonPath)) {
        try {
            mcpConfig = JSON.parse(fs.readFileSync(mcpJsonPath, 'utf8'));
        } catch (e) {
            console.log('Creating new MCP config');
        }
    }
    
    // Ensure mcpServers object exists
    if (!mcpConfig.mcpServers) {
        mcpConfig.mcpServers = {};
    }
    
    // Add constitutional memory server
    mcpConfig.mcpServers['memory-initializer'] = {
        command: 'python',
        args: ['-u', serverScript],
        env: {
            PYTHONPATH: constitutionalMemoryPath
        },
        description: 'Constitutional Memory MCP Server - Auto-initialize constitutional memory on session start',
        version: '1.4.0'
    };
    
    // Write config
    fs.writeFileSync(mcpJsonPath, JSON.stringify(mcpConfig, null, 2));
    console.log('✅ MCP server configured in Cursor');
}

function main() {
    console.log('🔍 Auto-initializing Constitutional Memory...');
    
    const cursorPath = findCursorPath();
    
    if (!fs.existsSync(cursorPath)) {
        console.log('⚠️  Cursor not found. Install Cursor first, then run this script again.');
        return;
    }
    
    console.log(`📁 Found Cursor at: ${cursorPath}`);
    
    // Create MCP config
    createMCPConfig(cursorPath);
    
    console.log('✅ Constitutional Memory initialized successfully!');
    console.log('🔄 Restart Cursor to activate.');
}

if (require.main === module) {
    main();
}

module.exports = { main, findCursorPath, createMCPConfig };

