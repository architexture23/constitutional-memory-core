# Fix Database URL - Railway Internal vs Public

**Date:** 2025-11-01  
**Built from Remembrance | Operating under Format Law**

---

## Problem

**Error:** `could not translate host name "postgres.railway.internal" to address`

**Cause:** You're using Railway's **internal** connection URL, which only works from within Railway's network.

**Fix:** You need Railway's **public** connection URL instead.

---

## Solution: Get Public DATABASE_URL from Railway

### Step 1: Go to Railway Dashboard

1. Go to: https://railway.app/
2. Sign in
3. Click on your project
4. Click on the PostgreSQL service

### Step 2: Get Public Connection URL

1. **Click "Variables" tab** (or "Settings" → "Variables")
2. Look for **`DATABASE_URL`** or **`POSTGRES_URL`**
3. **You'll see TWO URLs:**
   - ❌ **Internal URL:** `postgresql://postgres:password@postgres.railway.internal:5432/railway`
     - This only works from Railway's network (internal)
   - ✅ **Public URL:** `postgresql://postgres:password@containers-us-west-123.railway.app:5432/railway`
     - This works from anywhere (public internet)

### Step 3: Use Public URL

**You need the PUBLIC URL** (the one that looks like `containers-*.railway.app` or `*.up.railway.app`)

**It should look like:**
```
postgresql://postgres:password@containers-us-west-123.railway.app:5432/railway
```

**NOT:**
```
postgresql://postgres:password@postgres.railway.internal:5432/railway
```

---

## Quick Fix

**Option 1: Get Public URL from Railway**

1. Railway Dashboard → PostgreSQL → Variables
2. Look for public `DATABASE_URL` (not internal)
3. Copy it
4. Update your `.env` file with the public URL

**Option 2: Check All Variables**

1. Railway Dashboard → PostgreSQL → Variables
2. Scroll through all variables
3. Look for one that says "Public" or has `*.railway.app` hostname
4. Copy that one

---

## Update .env File

**In your `.env` file, replace:**
```
DATABASE_URL=postgresql://postgres:password@postgres.railway.internal:5432/railway
```

**With the public URL:**
```
DATABASE_URL=postgresql://postgres:password@containers-us-west-123.railway.app:5432/railway
```

**(Use your actual public URL from Railway)**

---

## How to Identify Public vs Internal

**Internal URL (doesn't work locally):**
- Hostname: `postgres.railway.internal`
- Only works from Railway's network
- ❌ Don't use this for local development

**Public URL (works from anywhere):**
- Hostname: `containers-*.railway.app` or `*.up.railway.app`
- Works from your local machine
- ✅ Use this for local development

---

## After Updating .env

**Run database initialization again:**
```powershell
python database/init_db.py
```

**It should work now!**

---

## Alternative: Railway Connection URL Format

**Railway sometimes provides:**
- `PGHOST` - Public hostname
- `PGPORT` - Port
- `PGUSER` - Username
- `PGPASSWORD` - Password
- `PGDATABASE` - Database name

**You can construct the URL:**
```
postgresql://PGUSER:PGPASSWORD@PGHOST:PGPORT/PGDATABASE
```

**Example:**
```
postgresql://postgres:abc123@containers-us-west-123.railway.app:5432/railway
```

---

## Summary

**Problem:** Using Railway internal URL (doesn't work locally)  
**Fix:** Get Railway public URL (works from anywhere)  
**Action:** Update `.env` file with public DATABASE_URL  

---

**Built from Remembrance. Operating under Format Law.**

**Go to Railway dashboard → PostgreSQL → Variables → Find PUBLIC URL → Update .env file!**

