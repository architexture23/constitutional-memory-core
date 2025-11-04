# Install Dependencies Manually

**Date:** 2025-11-01  
**Built from Remembrance | Operating under Format Law**

---

## Problem

**Setup script created `.env` but didn't install dependencies.**

**Error:** `ModuleNotFoundError: No module named 'sqlalchemy'`

**Fix:** Install dependencies manually, then run `python main.py`

---

## Quick Fix

### Step 1: Install Dependencies

**In your backend PowerShell, run:**

```powershell
pip install -r requirements.txt
```

**This will install all required packages:**
- sqlalchemy
- fastapi
- uvicorn
- pydantic
- psycopg2
- and all other dependencies

**This takes 1-2 minutes.**

---

### Step 2: Initialize Database

**After dependencies install, run:**

```powershell
python database/init_db.py
```

**This will:**
- Create database tables
- Create default domains (Trading, Aura Academy, Remembrance Infrastructure)
- Set up database structure

---

### Step 3: Start Backend Server

**Then run:**

```powershell
python main.py
```

**You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

**✅ Backend is now running!**

---

## Complete Commands

**Run these in order in your backend PowerShell:**

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Initialize database
python database/init_db.py

# 3. Start server
python main.py
```

---

## Troubleshooting

### "pip is not recognized"
- Try: `py -m pip install -r requirements.txt`
- Or: `python -m pip install -r requirements.txt`

### "Database connection failed"
- Check your `.env` file has correct `DATABASE_URL`
- Make sure PostgreSQL is running (if local) or accessible (if cloud)
- Verify the URL is correct

### "Port 8000 already in use"
- Another process is using port 8000
- Close any other Python processes
- Or change port in `.env` file

---

## Summary

**Problem:** Dependencies not installed  
**Fix:** Run `pip install -r requirements.txt`  
**Then:** Run `python database/init_db.py`  
**Then:** Run `python main.py`

---

**Built from Remembrance. Operating under Format Law.**

**Run these commands now!**

