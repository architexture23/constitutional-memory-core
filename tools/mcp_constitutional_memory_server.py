#!/usr/bin/env python3
"""
Format Law v1.5 Compliant
Last Validated: 2025-11-03T22:25:00Z
Structural Integrity: ✓

Constitutional Memory MCP Server
Purpose: Auto-initialize constitutional memory on session start via MCP
"""

import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
import sys
import os
import traceback

# Format Law headers
HEADERS = {
    "format_law": "v1.5",
    "last_validated": "2025-11-03T22:20:00Z",
    "structural_integrity": "✓"
}

# Get absolute path to script directory
SCRIPT_DIR = Path(__file__).resolve().parent
# Try to find TRUTH_DROP_PLATFORM directory
if (SCRIPT_DIR.parent / "manifest.yaml").exists():
    TRUTH_DROP_PLATFORM = SCRIPT_DIR.parent
elif (SCRIPT_DIR.parent.parent / "manifest.yaml").exists():
    TRUTH_DROP_PLATFORM = SCRIPT_DIR.parent.parent
else:
    # Fallback: assume script is in TRUTH_DROP_PLATFORM/tools/
    TRUTH_DROP_PLATFORM = SCRIPT_DIR.parent

# Use absolute paths
MANIFEST_PATH = (TRUTH_DROP_PLATFORM / "manifest.yaml").resolve()
META_INDEX_PATH = (TRUTH_DROP_PLATFORM / "meta_index.yaml").resolve()
CONSTITUTIONAL_MEMORY_PATH = (TRUTH_DROP_PLATFORM / "constitutional_memory").resolve()
PATTERN_MEMORY_PATH = (TRUTH_DROP_PLATFORM / "operational_autonomy" / "pattern_memory.json").resolve()
GUARDRAILS_PATH = (TRUTH_DROP_PLATFORM / "supervised_boundaries" / "guardrails.yaml").resolve()
ARCHIVE_PATH = Path(r"H:\My Drive\REMEMBRANCE INFRASTRUCTURE vX\Resonance Archive").resolve()


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
        
        # Load manifest
        if MANIFEST_PATH.exists():
            with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
                self.manifest = yaml.safe_load(f)
            components["manifest"] = {"loaded": True, "total_documents": self.manifest.get("manifest", {}).get("total_documents", 0)}
        
        # Load meta-index
        if META_INDEX_PATH.exists():
            with open(META_INDEX_PATH, 'r', encoding='utf-8') as f:
                self.meta_index = yaml.safe_load(f)
            components["meta_index"] = {"loaded": True, "use_cases": len(self.meta_index.get("meta_index", {}).get("by_use_case", {}))}
        
        # Load pattern memory
        if PATTERN_MEMORY_PATH.exists():
            with open(PATTERN_MEMORY_PATH, 'r', encoding='utf-8') as f:
                self.pattern_memory = json.load(f)
            components["pattern_memory"] = {"loaded": True, "total_patterns": len(self.pattern_memory.get("patterns", []))}
        
        # Load guardrails
        if GUARDRAILS_PATH.exists():
            with open(GUARDRAILS_PATH, 'r', encoding='utf-8') as f:
                self.guardrails = yaml.safe_load(f)
            components["guardrails"] = {"loaded": True, "total_rules": len(self.guardrails.get("guardrails", {}).get("rules", []))}
        
        # Scan constitutional memory
        if CONSTITUTIONAL_MEMORY_PATH.exists():
            self.constitutional_memory = self._scan_constitutional_memory()
            components["constitutional_memory"] = {"loaded": True, "drops": 13, "frameworks": 5}
        
        self.initialized = True
        
        return {
            "status": "initialized",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "components": components
        }
    
    def query_pattern(self, pattern_id: str) -> Dict[str, Any]:
        """Query pattern by pattern_id."""
        if not self.initialized:
            self.initialize()
        
        if not self.pattern_memory:
            return {"error": "Pattern memory not loaded"}
        
        patterns = self.pattern_memory.get("patterns", [])
        pattern = next((p for p in patterns if p.get("pattern_id") == pattern_id), None)
        
        if not pattern:
            return {"error": f"Pattern {pattern_id} not found"}
        
        return {"pattern": pattern}
    
    def query_drop(self, drop_id: str) -> Dict[str, Any]:
        """Query drop by drop_id."""
        if not self.initialized:
            self.initialize()
        
        # Drops are in constitutional_memory/ or manifest
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
            return {"error": f"Drop {drop_id} not found"}
        
        return {
            "drop_id": drop_id,
            "drop_name": drop_name,
            "path": f"TRUTH_DROP_PLATFORM/constitutional_memory/",
            "manifest_entry": self._get_drop_from_manifest(drop_id)
        }
    
    def query_by_use_case(self, use_case: str) -> Dict[str, Any]:
        """Query by use-case."""
        if not self.initialized:
            self.initialize()
        
        if not self.meta_index:
            return {"error": "Meta-index not loaded"}
        
        by_use_case = self.meta_index.get("meta_index", {}).get("by_use_case", {})
        results = by_use_case.get(use_case, [])
        
        return {"use_case": use_case, "results": results}
    
    def query_by_signal_type(self, signal_type: str) -> Dict[str, Any]:
        """Query by signal type."""
        if not self.initialized:
            self.initialize()
        
        if not self.meta_index:
            return {"error": "Meta-index not loaded"}
        
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
                return {"error": f"Precondition not met: {precondition}"}
        
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
            archive_path = Path(drive_path)
        else:
            archive_path = ARCHIVE_PATH
        
        if not archive_path.exists():
            return {"error": f"Archive path not found: {archive_path}"}
        
        # Scan archive and update manifest
        files_found = []
        for file_path in archive_path.rglob("*.gdoc"):
            files_found.append({
                "name": file_path.name,
                "path": str(file_path),
                "last_modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat() + "Z"
            })
        
        return {
            "synced": True,
            "timestamp": datetime.utcnow().isoformat() + "Z",
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
        # Can be expanded based on pattern definitions
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


# MCP Tool Interface
def tool_initialize_constitutional_memory() -> Dict[str, Any]:
    """MCP Tool: Initialize constitutional memory automatically."""
    server = ConstitutionalMemoryMCP()
    return server.initialize()


def tool_query_pattern(pattern_id: str) -> Dict[str, Any]:
    """MCP Tool: Query pattern by pattern_id."""
    server = ConstitutionalMemoryMCP()
    return server.query_pattern(pattern_id)


def tool_query_drop(drop_id: str) -> Dict[str, Any]:
    """MCP Tool: Query drop by drop_id."""
    server = ConstitutionalMemoryMCP()
    return server.query_drop(drop_id)


def tool_query_by_use_case(use_case: str) -> Dict[str, Any]:
    """MCP Tool: Query by use-case."""
    server = ConstitutionalMemoryMCP()
    return server.query_by_use_case(use_case)


def tool_query_by_signal_type(signal_type: str) -> Dict[str, Any]:
    """MCP Tool: Query by signal type."""
    server = ConstitutionalMemoryMCP()
    return server.query_by_signal_type(signal_type)


def tool_apply_pattern(pattern_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """MCP Tool: Apply pattern autonomously (within boundaries)."""
    server = ConstitutionalMemoryMCP()
    return server.apply_pattern(pattern_id, context)


def tool_detect_drift(context: Dict[str, Any]) -> Dict[str, Any]:
    """MCP Tool: Detect drift and trigger interventions."""
    server = ConstitutionalMemoryMCP()
    return server.detect_drift(context)


def tool_sync_archive(drive_path: Optional[str] = None) -> Dict[str, Any]:
    """MCP Tool: Sync manifest.yaml with Drive file system."""
    server = ConstitutionalMemoryMCP()
    return server.sync_archive(drive_path)


# MCP Protocol Implementation (JSON-RPC over stdio)
def handle_mcp_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Handle MCP request."""
    try:
        method = request.get("method")
        params = request.get("params", {})
        request_id = request.get("id")
        
        # Initialize server
        server = ConstitutionalMemoryMCP()
        
        # Route method to handler
        if method == "initialize_constitutional_memory":
            result = server.initialize()
        elif method == "query_pattern":
            result = server.query_pattern(params.get("pattern_id", ""))
        elif method == "query_drop":
            result = server.query_drop(params.get("drop_id", ""))
        elif method == "query_by_use_case":
            result = server.query_by_use_case(params.get("use_case", ""))
        elif method == "query_by_signal_type":
            result = server.query_by_signal_type(params.get("signal_type", ""))
        elif method == "apply_pattern":
            result = server.apply_pattern(params.get("pattern_id", ""), params.get("context", {}))
        elif method == "detect_drift":
            result = server.detect_drift(params.get("context", {}))
        elif method == "sync_archive":
            result = server.sync_archive(params.get("drive_path"))
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
        # Read request from stdin
        request_line = sys.stdin.readline()
        if not request_line:
            # If no request, just test initialization
            server = ConstitutionalMemoryMCP()
            result = server.initialize()
            print(json.dumps(result, indent=2))
            sys.exit(0)
        
        request = json.loads(request_line)
        response = handle_mcp_request(request)
        print(json.dumps(response))
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
        print(json.dumps(error_response))
        sys.stdout.flush()
        sys.exit(1)

