# MCP Troubleshooting Guide

**Format Law v1.5 Compliant**  
**Last Validated:** 2025-11-03T22:40:00Z  
**Structural Integrity:** ✓

## Common Issues & Fixes

### Issue 1: "Error - Show Output"

**Symptoms:** MCP server shows error in Cursor

**Possible Causes:**
1. Path issues (script not found)
2. Python not in PATH
3. Missing dependencies (yaml)
4. Incorrect MCP protocol implementation
5. Cursor MCP requirements not met

**Fixes Applied:**
1. ✅ Fixed path resolution (absolute paths)
2. ✅ Enhanced error handling (detailed error messages)
3. ✅ Created fixed version (`mcp_server_fixed.py`)
4. ✅ Updated configuration with `${workspaceFolder}` variable

### Issue 2: Script Not Found

**Symptoms:** "can't open file" or "No such file or directory"

**Fix:**
- Use absolute path: `${workspaceFolder}/TRUTH_DROP_PLATFORM/tools/mcp_server_fixed.py`
- Or use full Windows path: `C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\tools\mcp_server_fixed.py`

### Issue 3: Python Not Found

**Symptoms:** "python: command not found"

**Fix:**
- Use full Python path: `C:\Python3x\python.exe`
- Or ensure Python is in PATH

### Issue 4: Missing Dependencies

**Symptoms:** "No module named 'yaml'"

**Fix:**
```bash
pip install pyyaml
```

### Issue 5: MCP Protocol Issues

**Symptoms:** Server doesn't respond or wrong protocol

**Fix:**
- Ensure JSON-RPC 2.0 protocol implementation
- Check stdin/stdout handling
- Verify error responses follow JSON-RPC format

---

## Alternative Approach: Simpler MCP Server

If MCP protocol is too complex, we can create a simpler wrapper that:
1. Accepts command-line arguments instead of JSON-RPC
2. Returns JSON output
3. Works as a standard CLI tool

**This would be easier to debug and more reliable.**

---

## Current Status

**Fixed Version:** `tools/mcp_server_fixed.py`  
**Configuration:** Updated with `${workspaceFolder}`  
**Error Handling:** Enhanced  
**Path Resolution:** Fixed  

**Next Steps:**
1. Test script manually: `python TRUTH_DROP_PLATFORM/tools/mcp_server_fixed.py`
2. Check MCP logs in Cursor (Output panel → MCP Logs)
3. Verify configuration in Cursor Settings → Tools → MCP
4. Try alternative approach if needed

---

**Format Law v1.5 Compliant**  
**Troubleshooting:** Active  
**Status:** Ready for testing

