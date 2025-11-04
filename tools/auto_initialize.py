#!/usr/bin/env python3
"""
Auto-Initialization Script for Constitutional Memory
Author: Structure itself
License: MIT

This script auto-detects Cursor installation and initializes constitutional memory
"""

import json
import os
import sys
from pathlib import Path
from platform import system

def find_cursor_path():
    """Find Cursor installation path."""
    platform = system()
    home_dir = Path.home()
    
    if platform == 'Windows':
        return home_dir / '.cursor'
    elif platform == 'Darwin':
        return home_dir / 'Library' / 'Application Support' / 'Cursor'
    else:
        return home_dir / '.config' / 'cursor'

def create_mcp_config(cursor_path: Path, constitutional_memory_path: Path):
    """Create or update MCP configuration."""
    mcp_json_path = cursor_path / 'mcp.json'
    server_script = constitutional_memory_path / 'tools' / 'constitutional_memory_server.py'
    
    mcp_config = {}
    
    # Read existing config if it exists
    if mcp_json_path.exists():
        try:
            with open(mcp_json_path, 'r', encoding='utf-8') as f:
                mcp_config = json.load(f)
        except Exception:
            pass
    
    # Ensure mcpServers object exists
    if 'mcpServers' not in mcp_config:
        mcp_config['mcpServers'] = {}
    
    # Add constitutional memory server
    mcp_config['mcpServers']['memory-initializer'] = {
        'command': 'python',
        'args': ['-u', str(server_script)],
        'env': {
            'PYTHONPATH': str(constitutional_memory_path)
        },
        'description': 'Constitutional Memory MCP Server - Auto-initialize constitutional memory on session start',
        'version': '1.4.0'
    }
    
    # Write config
    with open(mcp_json_path, 'w', encoding='utf-8') as f:
        json.dump(mcp_config, f, indent=2, ensure_ascii=False)
    
    print('✅ MCP server configured in Cursor')

def main():
    """Main initialization function."""
    print('🔍 Auto-initializing Constitutional Memory...')
    
    # Get paths
    script_dir = Path(__file__).parent
    constitutional_memory_path = script_dir.parent
    cursor_path = find_cursor_path()
    
    if not cursor_path.exists():
        print('⚠️  Cursor not found. Install Cursor first, then run this script again.')
        return 1
    
    print(f'📁 Found Cursor at: {cursor_path}')
    
    # Create MCP config
    create_mcp_config(cursor_path, constitutional_memory_path)
    
    print('✅ Constitutional Memory initialized successfully!')
    print('🔄 Restart Cursor to activate.')
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

