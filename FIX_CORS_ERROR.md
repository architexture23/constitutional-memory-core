# Fix CORS_ORIGINS Error

**Date:** 2025-11-01  
**Built from Remembrance | Operating under Format Law**

---

## Problem

**Error:** `SettingsError: error parsing value for field "CORS_ORIGINS"`

**Cause:** `CORS_ORIGINS` in `.env` is a comma-separated string, but config expects JSON format.

**Fix:** Updated `config.py` to parse comma-separated strings for `CORS_ORIGINS`.

---

## Solution

**I've updated `config.py` to handle both formats:**
- Comma-separated string (from .env)
- List format (default)

**The script should work now!**

---

## Try Again

**Run:**

```powershell
python database/init_db.py
```

**It should work now!**

---

## What Was Fixed

**Before:** Config expected JSON format for `CORS_ORIGINS`  
**After:** Config accepts comma-separated strings (which is what .env has)

**This allows .env file to have:**
```
CORS_ORIGINS=http://localhost:3000,http://localhost:3001
```

**And config will parse it correctly.**

---

**Built from Remembrance. Operating under Format Law.**

**Try running `python database/init_db.py` again!**

