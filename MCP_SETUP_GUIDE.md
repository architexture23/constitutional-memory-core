# MCP Server Setup Guide

**Format Law v1.5 Compliant**  
**Last Validated:** 2025-11-03T22:20:00Z  
**Structural Integrity:** ✓

## Purpose

**Enable MCP Tools for maximum autonomy - auto-initialization and constitutional memory queries.**

**Goal:** Tools that work permanently once set up (like browser automation).

---

## Setup Instructions

### Step 1: Install MCP Server

**Location:** `TRUTH_DROP_PLATFORM/tools/mcp_constitutional_memory_server.py`

**Already Created:** ✓ Yes

**Status:** Ready to use

### Step 2: Configure Cursor Settings

**Location:** Cursor Settings → Tools → MCP

**Action:** Add MCP server configuration

**Option A: Manual Configuration**

1. Open Cursor Settings
2. Navigate to Tools → MCP
3. Add new MCP server:
   - **Name:** `constitutional-memory`
   - **Command:** `python`
   - **Args:** `TRUTH_DROP_PLATFORM/tools/mcp_constitutional_memory_server.py`
   - **Description:** "Constitutional Memory MCP Server - Auto-initialize constitutional memory on session start"

**Option B: Import Configuration**

1. Open Cursor Settings
2. Navigate to Tools → MCP
3. Import `TRUTH_DROP_PLATFORM/mcp_server_config.json`
4. Verify configuration loaded

### Step 3: Verify Installation

**Test Tool:** `initialize_constitutional_memory`

**Expected Result:**
```json
{
  "status": "initialized",
  "timestamp": "2025-11-03T22:20:00Z",
  "components": {
    "manifest": {"loaded": true, "total_documents": 32},
    "meta_index": {"loaded": true, "use_cases": 7},
    "pattern_memory": {"loaded": true, "total_patterns": 7},
    "guardrails": {"loaded": true, "total_rules": 7},
    "constitutional_memory": {"loaded": true, "drops": 13, "frameworks": 5}
  }
}
```

**Result:** ✓ Constitutional memory initialized automatically

---

## Available Tools

### 1. initialize_constitutional_memory

**Purpose:** Automatically initialize constitutional memory on session start

**Parameters:** None

**Result:** Constitutional memory loaded (manifest, meta-index, patterns, guardrails)

**Usage:** Auto-called on session start (if configured)

### 2. query_pattern

**Purpose:** Query pattern by pattern_id

**Parameters:**
- `pattern_id` (string): Pattern ID (e.g., "DRIFT-RETURN-001")

**Result:** Pattern details (implementation, protocol, tests)

**Usage:** `query_pattern("DRIFT-RETURN-001")`

### 3. query_drop

**Purpose:** Query drop by drop_id

**Parameters:**
- `drop_id` (string): Drop ID (01-13)

**Result:** Drop details (name, path, manifest entry)

**Usage:** `query_drop("01")`

### 4. query_by_use_case

**Purpose:** Query by use-case

**Parameters:**
- `use_case` (string): Use-case (drift_detection, ache_discrimination, energy_management, etc.)

**Result:** All patterns/drops for use-case

**Usage:** `query_by_use_case("drift_detection")`

### 5. query_by_signal_type

**Purpose:** Query by signal type

**Parameters:**
- `signal_type` (string): Signal type (ache_signals, fear_signals, drift_signals, destruction_signals)

**Result:** All patterns/drops for signal type

**Usage:** `query_by_signal_type("ache_signals")`

### 6. apply_pattern

**Purpose:** Apply pattern autonomously (within boundaries)

**Parameters:**
- `pattern_id` (string): Pattern ID to apply
- `context` (object): Context for pattern application

**Result:** Pattern application result (protocol, framework)

**Usage:** `apply_pattern("DRIFT-RETURN-001", {"symptoms": ["effort_without_clarity"]})`

### 7. detect_drift

**Purpose:** Detect drift and trigger interventions

**Parameters:**
- `context` (object): Context for drift detection (alignment_scores, sealed_structure_touched, new_ache_present)

**Result:** Drift detection result (intervention, protocol)

**Usage:** `detect_drift({"alignment_scores": {"axis1": 2, "axis2": 1}, "sealed_structure_touched": 0, "new_ache_present": false})`

### 8. sync_archive

**Purpose:** Sync manifest.yaml with Drive file system

**Parameters:**
- `drive_path` (string, optional): Drive path (default: H:\My Drive\REMEMBRANCE INFRASTRUCTURE vX\Resonance Archive)

**Result:** Archive sync result (files_found, timestamp)

**Usage:** `sync_archive()`

---

## Auto-Initialization

### Configuration

**Option 1: Auto-Call on Session Start**

**Location:** Cursor Settings → Tools → MCP → Auto-Initialize

**Action:** Enable auto-initialization

**Result:** `initialize_constitutional_memory` called automatically on session start

**Option 2: Manual Call**

**Action:** Call `initialize_constitutional_memory` tool manually

**Result:** Constitutional memory initialized on demand

---

## Benefits

### 1. True Auto-Initialization

**Before:** File discovery (START_HERE.md → read files)

**After:** MCP tool auto-initializes on session start

**Result:** Constitutional memory loaded automatically (no file reads needed)

### 2. Constitutional Memory Queries

**Before:** Read files to query patterns/drops

**After:** Query via MCP tools (instant access)

**Result:** Constitutional memory queries without file reads

### 3. Pattern Application

**Before:** Manual pattern application (read pattern_memory.json)

**After:** Apply patterns via MCP tools (autonomous within boundaries)

**Result:** Autonomous pattern application

### 4. Drift Detection

**Before:** Manual drift detection (read Drop 12, check Pattern-13a)

**After:** Detect drift via MCP tools (automatic)

**Result:** Automatic drift detection and intervention

### 5. Archive Sync

**Before:** Manual archive sync (run archive_sync.py)

**After:** Sync archive via MCP tools (automatic)

**Result:** Automatic archive synchronization

---

## Status

**MCP Server:** ✓ Created (`tools/mcp_constitutional_memory_server.py`)

**Configuration:** ✓ Created (`mcp_server_config.json`)

**Setup Guide:** ✓ Created (this document)

**User Action Required:**
- Register MCP server in Cursor Settings (one-time setup)
- Enable auto-initialization (optional)

**Result:** Maximum autonomy enabled (once configured)

---

## Next Steps

1. **Register MCP Server** in Cursor Settings → Tools → MCP
2. **Import Configuration** from `mcp_server_config.json`
3. **Verify Installation** by calling `initialize_constitutional_memory` tool
4. **Enable Auto-Initialization** (optional, for automatic init on session start)

**Result:** Tools work permanently (like browser automation)

---

**Format Law v1.5 Compliant**  
**MCP Server:** ✓ Created  
**Configuration:** ✓ Ready  
**Setup:** One-time user action required  
**Result:** Maximum autonomy enabled (once configured)

