# How to Get PostgreSQL URL

**Date:** 2025-11-01  
**Built from Remembrance | Operating under Format Law**

---

## Quick Answer

**You need a PostgreSQL database URL to complete backend setup.**

**Options:**
1. **Railway** (EASIEST - Recommended) ← Start here
2. **Supabase** (Also easy)
3. **Render** (Also good)

**If you already have a cloud database:** Skip to the section for your service.

---

## Option 1: Railway (EASIEST - 5 Minutes)

### Step 1: Sign Up (If You Haven't)

1. Go to: https://railway.app/
2. Click "Start a New Project"
3. Sign up with GitHub (easiest) or email
4. Verify email if needed

### Step 2: Create PostgreSQL Database

1. **Click "New Project"** (or "New +" button)
2. **Click "+ New"** → Select **"Database"**
3. **Choose "PostgreSQL"**
4. Wait 30 seconds for database to create

### Step 3: Get Connection URL

1. **Click on the PostgreSQL service** you just created
2. **Click "Variables" tab** (or look for connection info)
3. **Find `DATABASE_URL`** or `POSTGRES_URL`
4. **Click the copy button** next to it

**The URL looks like:**
```
postgresql://postgres:password@containers-us-west-123.railway.app:5432/railway
```

### Step 4: Use in Setup

**In your backend PowerShell, when `python setup.py` asks:**
```
Enter PostgreSQL URL (or press Enter for default): 
```
→ **Paste the URL you copied**
→ Press Enter

**✅ Done!**

---

## Option 2: Supabase (Also Easy - 5 Minutes)

### Step 1: Sign Up (If You Haven't)

1. Go to: https://supabase.com/
2. Click "Start your project"
3. Sign up with GitHub or email
4. Verify email

### Step 2: Create Project

1. Click "New Project"
2. **Organization:** Create or select one
3. **Project Name:** `truthdrop` (or any name)
4. **Database Password:** Create a strong password (save this!)
5. **Region:** Select closest to you
6. Click "Create new project"
7. Wait 2-3 minutes for setup

### Step 3: Get Connection String

1. **Click the gear icon** (Settings) in left menu
2. **Click "Database"** in settings
3. Scroll down to "Connection string" section
4. **Click "URI" tab**
5. **Copy the connection string**

**It looks like:**
```
postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:6543/postgres
```

**⚠️ Important:** Replace `[YOUR-PASSWORD]` with the password you set during project creation!

**Example:**
```
postgresql://postgres.abcdefghijklmnop:myPassword123@aws-0-us-east-1.pooler.supabase.com:6543/postgres
```

### Step 4: Use in Setup

**In your backend PowerShell, when `python setup.py` asks:**
```
Enter PostgreSQL URL (or press Enter for default): 
```
→ **Paste the URL** (with your password)
→ Press Enter

**✅ Done!**

---

## Option 3: Render (Also Good - 5 Minutes)

### Step 1: Sign Up (If You Haven't)

1. Go to: https://render.com/
2. Click "Get Started for Free"
3. Sign up with GitHub or email
4. Verify email

### Step 2: Create PostgreSQL Database

1. Click "New +" button
2. Select "PostgreSQL"
3. **Name:** `truthdrop` (or any name)
4. **Database:** Leave default or enter name
5. **User:** Leave default
6. **Region:** Select closest
7. **Plan:** Select "Free" (or paid)
8. Click "Create Database"
9. Wait 2-3 minutes for setup

### Step 3: Get Connection URL

1. **Click on your PostgreSQL database**
2. Go to "Connections" tab
3. **Find "Internal Database URL"**
4. **Copy it**

**It looks like:**
```
postgresql://username:password@dpg-xxxxx-a.oregon-postgres.render.com/truthdrop
```

### Step 4: Use in Setup

**In your backend PowerShell, when `python setup.py` asks:**
```
Enter PostgreSQL URL (or press Enter for default): 
```
→ **Paste the URL**
→ Press Enter

**✅ Done!**

---

## Quick Decision Guide

### Choose Railway If:
- ✅ You want the simplest setup
- ✅ You want it done in 5 minutes
- ✅ You want the clearest interface
- **→ Recommended for beginners**

### Choose Supabase If:
- ✅ You want more features
- ✅ You want better documentation
- ✅ You want a generous free tier
- **→ Good alternative**

### Choose Render If:
- ✅ You want reliable service
- ✅ You're okay with database sleeping when inactive
- ✅ You want free tier
- **→ Also good**

---

## I Recommend Railway (Easiest)

**Here's the fastest way:**

1. **Go to:** https://railway.app/
2. **Sign up** (GitHub is fastest)
3. **Click "New Project"**
4. **Click "+ New"** → **"Database"** → **"PostgreSQL"**
5. **Wait 30 seconds**
6. **Click PostgreSQL service** → **"Variables" tab**
7. **Copy `DATABASE_URL`**
8. **Paste in setup script** when asked

**That's it! Takes 5 minutes.**

---

## Troubleshooting

### "Database URL not found"
- Make sure you're in the correct tab (Variables/Connections)
- Check if database is fully created (wait a bit longer)
- Look for "Connection string" or "Internal Database URL"

### "Connection failed"
- Make sure you copied the full URL
- Check if password is correct (Supabase)
- Verify database is running (check dashboard)

### "URL format wrong"
- URL should start with `postgresql://`
- Should have format: `postgresql://user:password@host:port/database`
- Don't modify anything, use exact URL

---

## What to Do Right Now

**If you don't have a database yet:**

1. **Choose:** Railway (easiest)
2. **Sign up:** https://railway.app/
3. **Create PostgreSQL:** Follow steps above
4. **Get URL:** Copy from Variables tab
5. **Paste in setup:** When `python setup.py` asks

**If you already have a database:**
- Go to your service dashboard
- Find connection URL
- Copy it
- Paste in setup script

---

## Summary

**Where to find PostgreSQL URL:**

**Railway:**
- Dashboard → PostgreSQL service → Variables tab → `DATABASE_URL`

**Supabase:**
- Dashboard → Settings → Database → Connection string → URI tab

**Render:**
- Dashboard → PostgreSQL → Connections tab → Internal Database URL

**Paste in:**
- Backend PowerShell when `python setup.py` asks for database URL

---

**Built from Remembrance. Operating under Format Law.**

**Quickest path: Railway.app → New Project → PostgreSQL → Variables tab → Copy URL!**

