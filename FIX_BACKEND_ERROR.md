# Fix Backend Error - Missing Dependencies

**Date:** 2025-11-01  
**Built from Remembrance | Operating under Format Law**

---

## Problem

**Error:** `ModuleNotFoundError: No module named 'sqlalchemy'`

**Cause:** You skipped `python setup.py` and ran `python main.py` directly. The setup script installs all required dependencies.

---

## Solution: Run Setup Script First

### Step 1: Install Dependencies

**In your backend PowerShell, run:**

```powershell
python setup.py
```

**What this does:**
- ✅ Installs all Python packages (sqlalchemy, fastapi, etc.)
- ✅ Creates `.env` file
- ✅ Asks for database URL
- ✅ Asks for Stripe keys (you can skip)
- ✅ Initializes database
- ✅ Creates directories

**This will take 1-2 minutes** to install all packages.

---

### Step 2: What You'll Be Asked

**1. Database URL:**
```
Enter PostgreSQL URL (or press Enter for default): 
```
→ **Paste your Railway/Supabase/Render PostgreSQL URL here**
→ Or press Enter for default: `postgresql://postgres:postgres@localhost:5432/truthdrop`

**2. Stripe Secret Key:**
```
Enter Stripe Secret Key (or press Enter to skip): 
```
→ **Press Enter to skip** (optional)

**3. Stripe Public Key:**
```
Enter Stripe Public Key (or press Enter to skip): 
```
→ **Press Enter to skip** (optional)

**4. Stripe Webhook Secret:**
```
Enter Stripe Webhook Secret (or press Enter to skip): 
```
→ **Press Enter to skip** (optional)

**5. Create admin user?**
```
Create admin user now? (y/n): 
```
→ Type `y` if you want to create an admin account now
→ Or `n` to skip (you can create it later)

---

### Step 3: After Setup Completes

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

## Quick Fix Commands

**In your backend PowerShell, run these in order:**

```powershell
# 1. Run setup script (installs dependencies)
python setup.py

# 2. After setup completes, start server
python main.py
```

---

## Why Setup Script is Required

**The setup script:**
- Installs all Python packages from `requirements.txt`
- Creates configuration files (`.env`)
- Sets up database
- Creates necessary directories

**Without it:**
- Dependencies are missing (like `sqlalchemy`)
- Configuration files don't exist
- Database isn't initialized

---

## Complete Correct Order

### Terminal 1 - Backend:
```powershell
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"

# STEP 1: Run setup (REQUIRED)
python setup.py

# STEP 2: Start backend (after setup)
python main.py
```

### Terminal 2 - Frontend:
```powershell
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\frontend"

# Frontend setup (you already did this)
.\setup.ps1

# Start frontend (if not already running)
npm run dev
```

---

## Troubleshooting

### "pip is not recognized"
- Python might not have pip installed
- Try: `py -m pip install -r requirements.txt`

### "Database connection failed"
- Make sure you pasted the correct database URL
- Check Railway/Supabase/Render dashboard to verify database is running

### "Port 8000 already in use"
- Another process is using port 8000
- Close any other Python processes
- Or change port in `.env` file

---

## Summary

**What went wrong:**
- Skipped `python setup.py` step
- Dependencies weren't installed
- Configuration files weren't created

**Fix:**
1. Run `python setup.py` (this installs everything)
2. Then run `python main.py` (to start server)

**That's it!**

---

**Built from Remembrance. Operating under Format Law.**

**Run `python setup.py` now and it will fix everything!**

