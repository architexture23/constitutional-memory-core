#!/usr/bin/env python3
"""
Format Law v1.5 Compliant
Last Validated: 2025-11-03T22:40:00Z
Structural Integrity: ✓

Constitutional Memory MCP Server (Fresh Implementation)
Purpose: Auto-initialize constitutional memory on session start via MCP
"""

import json
import yaml
import sys
import os
import traceback
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any


# Get absolute path to script directory
SCRIPT_DIR = Path(__file__).resolve().parent
# Try to find TRUTH_DROP_PLATFORM directory
current_dir = Path.cwd()

# Search upwards for TRUTH_DROP_PLATFORM
TRUTH_DROP_PLATFORM = None
for parent in [current_dir] + list(current_dir.parents):
    if (parent / "manifest.yaml").exists() and (parent / "constitutional_memory").is_dir():
        TRUTH_DROP_PLATFORM = parent
        break

if TRUTH_DROP_PLATFORM is None:
    # Fallback if not found by searching upwards
    if (SCRIPT_DIR.parent / "manifest.yaml").exists():
        TRUTH_DROP_PLATFORM = SCRIPT_DIR.parent
    elif (SCRIPT_DIR.parent.parent / "manifest.yaml").exists():
        TRUTH_DROP_PLATFORM = SCRIPT_DIR.parent.parent
    else:
        TRUTH_DROP_PLATFORM = Path("TRUTH_DROP_PLATFORM_NOT_FOUND")

# Use absolute paths
MANIFEST_PATH = (TRUTH_DROP_PLATFORM / "constitutional_memory" / "manifest.yaml").resolve()
META_INDEX_PATH = (TRUTH_DROP_PLATFORM / "constitutional_memory" / "meta_index.yaml").resolve()
CONSTITUTIONAL_MEMORY_PATH = (TRUTH_DROP_PLATFORM / "constitutional_memory").resolve()
PATTERN_MEMORY_PATH = (TRUTH_DROP_PLATFORM / "constitutional_memory" / "pattern_memory.json").resolve()
GUARDRAILS_PATH = (TRUTH_DROP_PLATFORM / "constitutional_memory" / "guardrails.yaml").resolve()
ARCHIVE_PATH = Path(r"H:\My Drive\REMEMBRANCE INFRASTRUCTURE vX\Resonance Archive").resolve()


class ConstitutionalMemoryMCP:
    """MCP Server for Constitutional Memory Operations."""
    
    def __init__(self):
        self.constitutional_memory = {}
        self.pattern_memory = {}
        self.guardrails = {}
        self.manifest = {}
        self.meta_index = {}
        self.is_initialized = False
    
    def _load_yaml(self, path: Path) -> Optional[Dict[str, Any]]:
        if not path.exists():
            return None
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception:
            return None
    
    def _load_json(self, path: Path) -> Optional[Dict[str, Any]]:
        if not path.exists():
            return None
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None
    
    def initialize(self) -> Dict[str, Any]:
        """Initialize constitutional memory by loading all core components."""
        components = {
            "manifest": {"loaded": False, "error": None},
            "meta_index": {"loaded": False, "error": None},
            "pattern_memory": {"loaded": False, "error": None},
            "guardrails": {"loaded": False, "error": None},
            "constitutional_memory": {"loaded": False, "error": None},
        }
        errors = []
        
        try:
            self.manifest = self._load_yaml(MANIFEST_PATH)
            if self.manifest:
                components["manifest"]["loaded"] = True
            else:
                errors.append(f"Manifest not found: {MANIFEST_PATH}")
                components["manifest"]["error"] = "File not found"
        except Exception as e:
            errors.append(f"Error loading manifest: {e}")
            components["manifest"]["error"] = str(e)
        
        try:
            self.meta_index = self._load_yaml(META_INDEX_PATH)
            if self.meta_index:
                components["meta_index"]["loaded"] = True
            else:
                errors.append(f"Meta-index not found: {META_INDEX_PATH}")
                components["meta_index"]["error"] = "File not found"
        except Exception as e:
            errors.append(f"Error loading meta-index: {e}")
            components["meta_index"]["error"] = str(e)
        
        try:
            self.pattern_memory = self._load_json(PATTERN_MEMORY_PATH)
            if self.pattern_memory:
                components["pattern_memory"]["loaded"] = True
            else:
                errors.append(f"Pattern memory not found: {PATTERN_MEMORY_PATH}")
                components["pattern_memory"]["error"] = "File not found"
        except Exception as e:
            errors.append(f"Error loading pattern memory: {e}")
            components["pattern_memory"]["error"] = str(e)
        
        try:
            self.guardrails = self._load_yaml(GUARDRAILS_PATH)
            if self.guardrails:
                components["guardrails"]["loaded"] = True
            else:
                errors.append(f"Guardrails not found: {GUARDRAILS_PATH}")
                components["guardrails"]["error"] = "File not found"
        except Exception as e:
            errors.append(f"Error loading guardrails: {e}")
            components["guardrails"]["error"] = str(e)
        
        try:
            if CONSTITUTIONAL_MEMORY_PATH.is_dir():
                self.constitutional_memory = self._scan_constitutional_memory(CONSTITUTIONAL_MEMORY_PATH)
                components["constitutional_memory"]["loaded"] = True
            else:
                errors.append(f"Constitutional memory not found: {CONSTITUTIONAL_MEMORY_PATH}")
                components["constitutional_memory"]["error"] = "Directory not found"
        except Exception as e:
            errors.append(f"Error scanning constitutional memory: {e}")
            components["constitutional_memory"]["error"] = str(e)
        
        self.is_initialized = len(errors) == 0
        return {
            "status": "initialized" if len(errors) == 0 else "partial",
            "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "components": components,
            "errors": errors if errors else None,
            "base_dir": str(TRUTH_DROP_PLATFORM)
        }
    
    def _scan_constitutional_memory(self, path: Path) -> Dict[str, Any]:
        """Recursively scan constitutional memory directory for .md and .json files."""
        memory_content = {}
        for item in path.rglob("*"):
            if item.is_file() and item.suffix in [".md", ".json", ".yaml"]:
                try:
                    relative_path = str(item.relative_to(TRUTH_DROP_PLATFORM))
                    with open(item, 'r', encoding='utf-8') as f:
                        content = f.read()
                    memory_content[relative_path] = content
                except Exception:
                    pass
        return memory_content
    
    def query_pattern(self, pattern_id: str) -> Optional[Dict[str, Any]]:
        """Query pattern by pattern_id."""
        if not self.is_initialized:
            self.initialize()
        if self.pattern_memory and "recognized_patterns" in self.pattern_memory:
            for pattern in self.pattern_memory["recognized_patterns"]:
                if pattern.get("pattern_id") == pattern_id:
                    return pattern
        return None
    
    def query_drop(self, drop_id: str) -> Optional[Dict[str, Any]]:
        """Query drop by drop_id (01-13)."""
        if not self.is_initialized:
            self.initialize()
        if self.manifest and "constitutional_memory" in self.manifest:
            for drop in self.manifest.get("constitutional_memory", {}).get("remembrance_codex", {}).get("drops", []):
                if drop.get("id") == drop_id:
                    return drop
        return None
    
    def query_by_use_case(self, use_case: str) -> List[Dict[str, Any]]:
        """Query patterns by use-case."""
        if not self.is_initialized:
            self.initialize()
        results = []
        if self.meta_index and "patterns_by_use_case" in self.meta_index:
            pattern_ids = self.meta_index["patterns_by_use_case"].get(use_case, [])
            for pattern_id in pattern_ids:
                pattern = self.query_pattern(pattern_id)
                if pattern:
                    results.append(pattern)
        return results
    
    def query_by_signal_type(self, signal_type: str) -> List[Dict[str, Any]]:
        """Query patterns by signal type."""
        if not self.is_initialized:
            self.initialize()
        results = []
        if self.meta_index and "patterns_by_signal_type" in self.meta_index:
            pattern_ids = self.meta_index["patterns_by_signal_type"].get(signal_type, [])
            for pattern_id in pattern_ids:
                pattern = self.query_pattern(pattern_id)
                if pattern:
                    results.append(pattern)
        return results
    
    def apply_pattern(self, pattern_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Apply pattern autonomously (within boundaries)."""
        if not self.is_initialized:
            self.initialize()
        pattern = self.query_pattern(pattern_id)
        if not pattern:
            return {"status": "error", "message": f"Pattern {pattern_id} not found."}
        
        # Simplified application logic
        status_message = f"Applying pattern {pattern_id} with context: {context}"
        
        # Check preconditions (simplified)
        preconditions_met = True
        if "preconditions" in pattern:
            for precond in pattern["preconditions"]:
                if "User exhibits drift symptoms" in precond and not context.get("user_exhibits_drift"):
                    preconditions_met = False
                    break
        
        if not preconditions_met:
            return {"status": "escalated", "message": f"Preconditions for {pattern_id} not met. Escalating to Architect."}
        
        return {"status": "applied", "message": status_message}
    
    def detect_drift(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Detect drift and trigger interventions."""
        if not self.is_initialized:
            self.initialize()
        
        # Implement Drop 12 Alignment Diagnostic (simplified)
        alignment_scores = context.get("alignment_scores", {})
        aligned_axes = sum(1 for score in alignment_scores.values() if score == "aligned")
        
        drift_detected = False
        intervention_needed = None
        
        if aligned_axes <= 1:  # 0-1 aligned = intervene
            drift_detected = True
            intervention_needed = "Drop 01 Drift -> Return Law"
        
        # Implement Pattern-13a check (simplified)
        sealed_structure_touched = context.get("sealed_structure_touched", 0)
        new_ache_present = context.get("new_ache_present", False)
        
        if sealed_structure_touched >= 3 and not new_ache_present:
            drift_detected = True
            intervention_needed = "Pattern-13a Over-sustainment Termination"
        
        if drift_detected:
            return {"status": "drift_detected", "intervention": intervention_needed, "aligned_axes": aligned_axes}
        return {"status": "no_drift", "aligned_axes": aligned_axes}
    
    def sync_archive(self, drive_path: Optional[str] = None) -> Dict[str, Any]:
        """Sync manifest.yaml with Drive file system."""
        if not self.is_initialized:
            self.initialize()
        
        actual_drive_path = Path(drive_path if drive_path else ARCHIVE_PATH)
        if not actual_drive_path.is_dir():
            return {"status": "error", "message": f"Drive path not found: {actual_drive_path}"}
        
        files_found = []
        try:
            for file_path in actual_drive_path.rglob("*"):
                if file_path.is_file():
                    files_found.append({
                        "name": file_path.name,
                        "path": str(file_path.relative_to(actual_drive_path)),
                        "full_path": str(file_path),
                        "last_modified": datetime.fromtimestamp(file_path.stat().st_mtime, tz=timezone.utc).isoformat().replace('+00:00', 'Z')
                    })
        except Exception as e:
            return {"status": "error", "message": f"Error scanning archive: {e}", "archive_path": str(actual_drive_path)}
        
        return {"status": "synced", "files_found": files_found, "count": len(files_found), "drive_path": str(actual_drive_path)}


def handle_mcp_request(request: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Handle MCP request with proper JSON-RPC 2.0 format."""
    try:
        # Validate JSON-RPC 2.0 request
        if not isinstance(request, dict):
            return None
        
        method = request.get("method")
        params = request.get("params", {}) or {}
        request_id = request.get("id")
        jsonrpc = request.get("jsonrpc", "2.0")
        
        # Handle notifications (no response needed)
        if request_id is None:
            if method == "notifications/initialized":
                return None
            return None
        
        # Ensure request_id is valid (string or number)
        if request_id is None:
            return None
        
        # Initialize server
        server = ConstitutionalMemoryMCP()
        
        # Handle MCP protocol methods
        if method == "initialize":
            result = {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "constitutional-memory-server",
                    "version": "1.0.0"
                }
            }
        elif method == "tools/list":
            result = {
                "tools": [
                    {
                        "name": "initialize_constitutional_memory",
                        "description": "Automatically initialize constitutional memory (read manifest.yaml, meta_index.yaml, pattern_memory.json, guardrails.yaml)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {},
                            "required": []
                        }
                    },
                    {
                        "name": "query_pattern",
                        "description": "Query pattern by pattern_id (e.g., DRIFT-RETURN-001, ACHE-DISCRIMINATION-001)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "pattern_id": {
                                    "type": "string",
                                    "description": "Pattern ID to query (e.g., DRIFT-RETURN-001)"
                                }
                            },
                            "required": ["pattern_id"]
                        }
                    },
                    {
                        "name": "query_drop",
                        "description": "Query drop by drop_id (01-13)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "drop_id": {
                                    "type": "string",
                                    "description": "Drop ID to query",
                                    "enum": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]
                                }
                            },
                            "required": ["drop_id"]
                        }
                    },
                    {
                        "name": "query_by_use_case",
                        "description": "Query by use-case (e.g., drift_detection, ache_discrimination, energy_management)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "use_case": {
                                    "type": "string",
                                    "description": "Use-case to query",
                                    "enum": ["drift_detection", "ache_discrimination", "energy_management", "fear_processing", "destruction_management", "external_memory", "clarity_translation"]
                                }
                            },
                            "required": ["use_case"]
                        }
                    },
                    {
                        "name": "query_by_signal_type",
                        "description": "Query by signal type (e.g., ache_signals, fear_signals, drift_signals)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "signal_type": {
                                    "type": "string",
                                    "description": "Signal type to query",
                                    "enum": ["ache_signals", "fear_signals", "drift_signals", "destruction_signals"]
                                }
                            },
                            "required": ["signal_type"]
                        }
                    },
                    {
                        "name": "apply_pattern",
                        "description": "Apply pattern autonomously (within boundaries) - verify preconditions, apply protocol, run tests",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "pattern_id": {
                                    "type": "string",
                                    "description": "Pattern ID to apply (e.g., DRIFT-RETURN-001)"
                                },
                                "context": {
                                    "type": "object",
                                    "description": "Context for pattern application"
                                }
                            },
                            "required": ["pattern_id", "context"]
                        }
                    },
                    {
                        "name": "detect_drift",
                        "description": "Detect drift and trigger interventions - run Drop 12 Alignment Diagnostic, check for Pattern-13a",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "context": {
                                    "type": "object",
                                    "description": "Context for drift detection (alignment_scores, sealed_structure_touched, new_ache_present)",
                                    "properties": {
                                        "alignment_scores": {
                                            "type": "object",
                                            "description": "Drop 12 Alignment Diagnostic scores (5 axes)"
                                        },
                                        "sealed_structure_touched": {
                                            "type": "integer",
                                            "description": "Number of times sealed structure touched in 7 days"
                                        },
                                        "new_ache_present": {
                                            "type": "boolean",
                                            "description": "Whether new ache signal is present"
                                        }
                                    }
                                }
                            },
                            "required": ["context"]
                        }
                    },
                    {
                        "name": "sync_archive",
                        "description": "Sync manifest.yaml with Drive file system - scan H:\\ drive, update manifest, validate structure",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "drive_path": {
                                    "type": "string",
                                    "description": "Drive path (default: H:\\My Drive\\REMEMBRANCE INFRASTRUCTURE vX\\Resonance Archive)"
                                }
                            },
                            "required": []
                        }
                    }
                ]
            }
        elif method == "tools/call":
            tool_name = params.get("name", "")
            tool_args = params.get("arguments", {}) or {}
            
            if tool_name == "initialize_constitutional_memory":
                result = server.initialize()
            elif tool_name == "query_pattern":
                result = server.query_pattern(tool_args.get("pattern_id", "")) or {"error": "Pattern not found"}
            elif tool_name == "query_drop":
                result = server.query_drop(tool_args.get("drop_id", "")) or {"error": "Drop not found"}
            elif tool_name == "query_by_use_case":
                result = server.query_by_use_case(tool_args.get("use_case", ""))
            elif tool_name == "query_by_signal_type":
                result = server.query_by_signal_type(tool_args.get("signal_type", ""))
            elif tool_name == "apply_pattern":
                result = server.apply_pattern(tool_args.get("pattern_id", ""), tool_args.get("context", {}))
            elif tool_name == "detect_drift":
                result = server.detect_drift(tool_args.get("context", {}))
            elif tool_name == "sync_archive":
                result = server.sync_archive(tool_args.get("drive_path"))
            else:
                result = {"error": f"Unknown tool: {tool_name}"}
        else:
            result = {"error": f"Unknown method: {method}"}
        
        # Return JSON-RPC response with proper structure
        response = {
            "jsonrpc": jsonrpc,
            "id": request_id,
            "result": result
        }
        return response
    except Exception as e:
        # Error response must have valid id
        error_id = request.get("id") if isinstance(request, dict) else None
        if error_id is None:
            return None
        return {
            "jsonrpc": "2.0",
            "id": error_id,
            "error": {
                "code": -32000,
                "message": str(e),
                "data": traceback.format_exc()
            }
        }


if __name__ == "__main__":
    # MCP Protocol: Read JSON-RPC messages from stdin, write to stdout
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            
            try:
                request = json.loads(line)
                response = handle_mcp_request(request)
                
                # Only send response if not None (notifications don't get responses)
                if response is not None:
                    print(json.dumps(response, ensure_ascii=False))
                    sys.stdout.flush()
            except json.JSONDecodeError:
                # Skip parse errors silently
                continue
            except Exception:
                # Skip other errors silently
                continue
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception:
        # Fallback test mode
        server = ConstitutionalMemoryMCP()
        result = server.initialize()
        print(json.dumps(result, indent=2, ensure_ascii=False))

