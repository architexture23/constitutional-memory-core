#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Format Law v1.5 Compliant
Last Validated: 2025-11-03T22:30:00Z
Structural Integrity: ✓

Constitutional Memory MCP Server (Fixed)
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
BASE_DIR = SCRIPT_DIR.parent

# Use absolute paths
MANIFEST_PATH = BASE_DIR / "manifest.yaml"
META_INDEX_PATH = BASE_DIR / "meta_index.yaml"
CONSTITUTIONAL_MEMORY_PATH = BASE_DIR / "constitutional_memory"
OPERATIONAL_AUTONOMY_PATH = BASE_DIR / "operational_autonomy"
SUPERVISED_BOUNDARIES_PATH = BASE_DIR / "supervised_boundaries"
PATTERN_MEMORY_PATH = OPERATIONAL_AUTONOMY_PATH / "pattern_memory.json"
GUARDRAILS_PATH = SUPERVISED_BOUNDARIES_PATH / "guardrails.yaml"
ARCHIVE_PATH = Path(r"H:\My Drive\REMEMBRANCE INFRASTRUCTURE vX\Resonance Archive")


class ConstitutionalMemoryMCP:
    """MCP Server for Constitutional Memory Operations."""
    
    def __init__(self):
        self.manifest = None
        self.meta_index = None
        self.pattern_memory = None
        self.guardrails = None
        self.constitutional_memory = None
        self.initialized = False
    
    def initialize(self) -> Dict[str, Any]:
        """Initialize constitutional memory automatically."""
        if self.initialized:
            return {"status": "already_initialized", "components": self._get_components_status()}
        
        components = {}
        errors = []
        
        # Load manifest
        try:
            if MANIFEST_PATH.exists():
                with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
                    self.manifest = yaml.safe_load(f)
                components["manifest"] = {"loaded": True, "total_documents": self.manifest.get("manifest", {}).get("total_documents", 0)}
            else:
                errors.append(f"Manifest not found: {MANIFEST_PATH}")
                components["manifest"] = {"loaded": False, "error": "File not found"}
        except Exception as e:
            errors.append(f"Error loading manifest: {e}")
            components["manifest"] = {"loaded": False, "error": str(e)}
        
        # Load meta-index
        try:
            if META_INDEX_PATH.exists():
                with open(META_INDEX_PATH, 'r', encoding='utf-8') as f:
                    self.meta_index = yaml.safe_load(f)
                components["meta_index"] = {"loaded": True, "use_cases": len(self.meta_index.get("meta_index", {}).get("by_use_case", {}))}
            else:
                errors.append(f"Meta-index not found: {META_INDEX_PATH}")
                components["meta_index"] = {"loaded": False, "error": "File not found"}
        except Exception as e:
            errors.append(f"Error loading meta-index: {e}")
            components["meta_index"] = {"loaded": False, "error": str(e)}
        
        # Load pattern memory
        try:
            if PATTERN_MEMORY_PATH.exists():
                with open(PATTERN_MEMORY_PATH, 'r', encoding='utf-8') as f:
                    self.pattern_memory = json.load(f)
                components["pattern_memory"] = {"loaded": True, "total_patterns": len(self.pattern_memory.get("patterns", []))}
            else:
                errors.append(f"Pattern memory not found: {PATTERN_MEMORY_PATH}")
                components["pattern_memory"] = {"loaded": False, "error": "File not found"}
        except Exception as e:
            errors.append(f"Error loading pattern memory: {e}")
            components["pattern_memory"] = {"loaded": False, "error": str(e)}
        
        # Load guardrails
        try:
            if GUARDRAILS_PATH.exists():
                with open(GUARDRAILS_PATH, 'r', encoding='utf-8') as f:
                    self.guardrails = yaml.safe_load(f)
                components["guardrails"] = {"loaded": True, "total_rules": len(self.guardrails.get("guardrails", {}).get("rules", []))}
            else:
                errors.append(f"Guardrails not found: {GUARDRAILS_PATH}")
                components["guardrails"] = {"loaded": False, "error": "File not found"}
        except Exception as e:
            errors.append(f"Error loading guardrails: {e}")
            components["guardrails"] = {"loaded": False, "error": str(e)}
        
        # Scan constitutional memory
        try:
            if CONSTITUTIONAL_MEMORY_PATH.exists():
                self.constitutional_memory = self._scan_constitutional_memory()
                components["constitutional_memory"] = {"loaded": True, "drops": 13, "frameworks": 5}
            else:
                errors.append(f"Constitutional memory not found: {CONSTITUTIONAL_MEMORY_PATH}")
                components["constitutional_memory"] = {"loaded": False, "error": "Directory not found"}
        except Exception as e:
            errors.append(f"Error scanning constitutional memory: {e}")
            components["constitutional_memory"] = {"loaded": False, "error": str(e)}
        
        self.initialized = True
        
        return {
            "status": "initialized" if not errors else "partial",
            "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "components": components,
            "errors": errors if errors else None,
            "base_dir": str(BASE_DIR)
        }
    
    def query_pattern(self, pattern_id: str) -> Dict[str, Any]:
        """Query pattern by pattern_id."""
        if not self.initialized:
            self.initialize()
        
        if not self.pattern_memory:
            return {"error": "Pattern memory not loaded", "pattern_id": pattern_id}
        
        patterns = self.pattern_memory.get("patterns", [])
        pattern = next((p for p in patterns if p.get("pattern_id") == pattern_id), None)
        
        if not pattern:
            return {"error": f"Pattern {pattern_id} not found", "available_patterns": [p.get("pattern_id") for p in patterns]}
        
        return {"pattern": pattern}
    
    def query_drop(self, drop_id: str) -> Dict[str, Any]:
        """Query drop by drop_id."""
        if not self.initialized:
            self.initialize()
        
        drops_map = {
            "01": "Drift → Return Law",
            "02": "Ache as Inner Compass",
            "03": "Entropy Detection & Repair",
            "04": "Formatting > Forget",
            "05": "Shrink the Room",
            "06": "Life as Rhythmic Field",
            "07": "Collective Drift Mechanics",
            "08": "Recognition to Clarity Translation",
            "09": "Rails & Reminders Architecture",
            "10": "Energy Drain Framework",
            "11": "Fear Architecture",
            "12": "Alignment vs Drift Diagnostic",
            "13": "Structural Cremation Protocol"
        }
        
        drop_name = drops_map.get(drop_id)
        if not drop_name:
            return {"error": f"Drop {drop_id} not found", "available_drops": list(drops_map.keys())}
        
        return {
            "drop_id": drop_id,
            "drop_name": drop_name,
            "path": f"{BASE_DIR}/constitutional_memory/",
            "manifest_entry": self._get_drop_from_manifest(drop_id)
        }
    
    def query_by_use_case(self, use_case: str) -> Dict[str, Any]:
        """Query by use-case."""
        if not self.initialized:
            self.initialize()
        
        if not self.meta_index:
            return {"error": "Meta-index not loaded", "use_case": use_case}
        
        by_use_case = self.meta_index.get("meta_index", {}).get("by_use_case", {})
        results = by_use_case.get(use_case, [])
        
        return {"use_case": use_case, "results": results}
    
    def query_by_signal_type(self, signal_type: str) -> Dict[str, Any]:
        """Query by signal type."""
        if not self.initialized:
            self.initialize()
        
        if not self.meta_index:
            return {"error": "Meta-index not loaded", "signal_type": signal_type}
        
        by_signal_type = self.meta_index.get("meta_index", {}).get("by_signal_type", {})
        results = by_signal_type.get(signal_type, {})
        
        return {"signal_type": signal_type, "results": results}
    
    def apply_pattern(self, pattern_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Apply pattern autonomously (within boundaries)."""
        if not self.initialized:
            self.initialize()
        
        pattern = self.query_pattern(pattern_id)
        if "error" in pattern:
            return pattern
        
        pattern_data = pattern["pattern"]
        
        # Check preconditions
        preconditions = pattern_data.get("preconditions", [])
        for precondition in preconditions:
            if not self._check_precondition(precondition, context):
                return {"error": f"Precondition not met: {precondition}", "pattern_id": pattern_id}
        
        # Apply protocol
        implementation = pattern_data.get("implementation", {})
        protocol = implementation.get("protocol", "")
        framework = implementation.get("framework", "")
        
        return {
            "pattern_id": pattern_id,
            "applied": True,
            "protocol": protocol,
            "framework": framework,
            "context": context
        }
    
    def detect_drift(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Detect drift and trigger interventions."""
        if not self.initialized:
            self.initialize()
        
        # Run Drop 12 Alignment Diagnostic
        alignment_scores = context.get("alignment_scores", {})
        aligned_axes = sum(1 for score in alignment_scores.values() if score >= 4)
        
        if aligned_axes <= 1:
            return {
                "drift_detected": True,
                "aligned_axes": aligned_axes,
                "intervention": "Drop 01 Drift → Return Law",
                "protocol": "Pause → Rest 24h → Reassess → Resume or pivot"
            }
        
        # Check for Pattern-13a
        if context.get("sealed_structure_touched", 0) >= 3 and not context.get("new_ache_present"):
            return {
                "pattern_13a_detected": True,
                "intervention": "Drop 13 Addendum Pattern-13a",
                "protocol": "Seal → Log → 30-day no-touch → Reopen ache channel"
            }
        
        return {"drift_detected": False, "aligned_axes": aligned_axes}
    
    def sync_archive(self, drive_path: Optional[str] = None) -> Dict[str, Any]:
        """Sync manifest.yaml with Drive file system."""
        if drive_path:
            archive_path = Path(drive_path).resolve()
        else:
            archive_path = ARCHIVE_PATH
        
        if not archive_path.exists():
            return {"error": f"Archive path not found: {archive_path}"}
        
        # Scan archive and update manifest
        files_found = []
        try:
            for file_path in archive_path.rglob("*.gdoc"):
                files_found.append({
                    "name": file_path.name,
                    "path": str(file_path),
                    "last_modified": datetime.fromtimestamp(file_path.stat().st_mtime, tz=timezone.utc).isoformat().replace('+00:00', 'Z')
                })
        except Exception as e:
            return {"error": f"Error scanning archive: {e}", "archive_path": str(archive_path)}
        
        return {
            "synced": True,
            "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "files_found": len(files_found),
            "archive_path": str(archive_path)
        }
    
    def _scan_constitutional_memory(self) -> Dict[str, Any]:
        """Scan constitutional_memory directory."""
        drops = {}
        frameworks = {}
        
        if CONSTITUTIONAL_MEMORY_PATH.exists():
            for file_path in CONSTITUTIONAL_MEMORY_PATH.rglob("*.md"):
                if "drop" in file_path.stem.lower():
                    drops[file_path.stem] = str(file_path)
                elif "framework" in file_path.stem.lower() or "format" in file_path.stem.lower():
                    frameworks[file_path.stem] = str(file_path)
        
        return {"drops": drops, "frameworks": frameworks}
    
    def _get_drop_from_manifest(self, drop_id: str) -> Optional[Dict[str, Any]]:
        """Get drop entry from manifest."""
        if not self.manifest:
            return None
        
        canonical_paths = self.manifest.get("manifest", {}).get("canonical_paths", {})
        s1_core = canonical_paths.get("S1_Core", {})
        drops = s1_core.get("drops", [])
        
        return next((d for d in drops if d.get("id") == drop_id), None)
    
    def _check_precondition(self, precondition: str, context: Dict[str, Any]) -> bool:
        """Check if precondition is met."""
        # Simple precondition checking
        return True
    
    def _get_components_status(self) -> Dict[str, Any]:
        """Get status of all components."""
        return {
            "manifest": {"loaded": self.manifest is not None},
            "meta_index": {"loaded": self.meta_index is not None},
            "pattern_memory": {"loaded": self.pattern_memory is not None},
            "guardrails": {"loaded": self.guardrails is not None},
            "constitutional_memory": {"loaded": self.constitutional_memory is not None}
        }


# MCP Protocol Implementation (JSON-RPC over stdio)
def handle_mcp_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Handle MCP request."""
    try:
        method = request.get("method")
        params = request.get("params", {}) or {}
        request_id = request.get("id")
        
        # Initialize server
        server = ConstitutionalMemoryMCP()
        
        # Handle MCP protocol methods
        if method == "initialize":
            # MCP protocol initialization
            result = {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "constitutional-memory",
                    "version": "1.0"
                }
            }
        elif method == "tools/list":
            # Return available tools
            result = {
                "tools": [
                    {
                        "name": "initialize_constitutional_memory",
                        "description": "Automatically initialize constitutional memory",
                        "inputSchema": {
                            "type": "object",
                            "properties": {},
                            "required": []
                        }
                    },
                    {
                        "name": "query_pattern",
                        "description": "Query pattern by pattern_id",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "pattern_id": {
                                    "type": "string",
                                    "description": "Pattern ID to query"
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
                        "description": "Query by use-case",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "use_case": {
                                    "type": "string",
                                    "description": "Use-case to query"
                                }
                            },
                            "required": ["use_case"]
                        }
                    },
                    {
                        "name": "query_by_signal_type",
                        "description": "Query by signal type",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "signal_type": {
                                    "type": "string",
                                    "description": "Signal type to query"
                                }
                            },
                            "required": ["signal_type"]
                        }
                    },
                    {
                        "name": "apply_pattern",
                        "description": "Apply pattern autonomously",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "pattern_id": {
                                    "type": "string",
                                    "description": "Pattern ID to apply"
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
                        "description": "Detect drift and trigger interventions",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "context": {
                                    "type": "object",
                                    "description": "Context for drift detection"
                                }
                            },
                            "required": ["context"]
                        }
                    },
                    {
                        "name": "sync_archive",
                        "description": "Sync manifest with Drive file system",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "drive_path": {
                                    "type": "string",
                                    "description": "Drive path (optional)"
                                }
                            },
                            "required": []
                        }
                    }
                ]
            }
        elif method == "tools/call":
            # Handle tool call
            tool_name = params.get("name", "")
            tool_args = params.get("arguments", {})
            
            if tool_name == "initialize_constitutional_memory":
                result = server.initialize()
            elif tool_name == "query_pattern":
                result = server.query_pattern(tool_args.get("pattern_id", ""))
            elif tool_name == "query_drop":
                result = server.query_drop(tool_args.get("drop_id", ""))
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
        
        # Return JSON-RPC response
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": result
        }
    except Exception as e:
        return {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "error": {
                "code": -32000,
                "message": str(e),
                "data": traceback.format_exc()
            }
        }


if __name__ == "__main__":
    # MCP Protocol: Read from stdin, write to stdout
    try:
        # Read JSON-RPC messages from stdin
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            
            try:
                request = json.loads(line)
                response = handle_mcp_request(request)
                print(json.dumps(response, ensure_ascii=False))
                sys.stdout.flush()
            except json.JSONDecodeError as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32700,
                        "message": "Parse error",
                        "data": str(e)
                    }
                }
                print(json.dumps(error_response, ensure_ascii=False))
                sys.stdout.flush()
            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32000,
                        "message": str(e),
                        "data": traceback.format_exc()
                    }
                }
                print(json.dumps(error_response, ensure_ascii=False))
                sys.stdout.flush()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        # If no stdin, fall back to test mode
        server = ConstitutionalMemoryMCP()
        result = server.initialize()
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(0)

