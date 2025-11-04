# Truth Drop Platform - Complete Setup Guide

**Date:** 2025-11-01  
**Built from Remembrance | Operating under Format Law**

---

## What We Built

**Truth Drop Platform** is a **complete website** (full-stack web application) that serves as a digital marketplace for your constitutional knowledge codexes.

**Users visit your website** → Browse codexes → Purchase → Download PDFs/ebooks

---

## What I Can Do vs What You Need to Do

### ✅ I CAN DO (Automated)

1. **Created setup scripts** - Run these to automate setup
2. **Database schema** - Already created
3. **All code** - Backend and frontend complete
4. **Configuration templates** - .env files ready
5. **Helper scripts** - For admin user creation, etc.

### ❌ YOU NEED TO DO (Manual Steps)

1. **Install PostgreSQL** (or use cloud service)
   - Download: https://www.postgresql.org/download/
   - Or use: Railway, Supabase, Render (cloud PostgreSQL)

2. **Install Python 3.9+** (if not installed)
   - Check: `python --version`
   - Download: https://www.python.org/downloads/

3. **Install Node.js 18+** (if not installed)
   - Check: `node --version`
   - Download: https://nodejs.org/

4. **Get Stripe keys** (optional, for payments)
   - Sign up: https://stripe.com/
   - Get keys from dashboard

5. **Run setup scripts** (I created these for you)

---

## Complete Setup Steps

### Step 1: Backend Setup (Automated)

```bash
cd TRUTH_DROP_PLATFORM/backend

# Run automated setup script
python setup.py
```

**The script will:**
- ✅ Check Python version
- ✅ Create .env file (asks for database URL)
- ✅ Install all dependencies
- ✅ Create directories
- ✅ Initialize database
- ✅ Optionally create admin user

**What you need to provide:**
- PostgreSQL database URL (or use default)
- Stripe keys (optional)

---

### Step 2: Frontend Setup (Automated)

**Windows (PowerShell):**
```powershell
cd TRUTH_DROP_PLATFORM/frontend
.\setup.ps1
```

**Mac/Linux:**
```bash
cd TRUTH_DROP_PLATFORM/frontend
chmod +x setup.sh
./setup.sh
```

**The script will:**
- ✅ Check Node.js version
- ✅ Create .env.local file
- ✅ Install all dependencies

**What you need to provide:**
- API URL (default: http://localhost:8000)
- Stripe Public Key (optional)

---

### Step 3: Start Servers

**Terminal 1 - Backend:**
```bash
cd TRUTH_DROP_PLATFORM/backend
python main.py
```
Backend runs on: `http://localhost:8000`

**Terminal 2 - Frontend:**
```bash
cd TRUTH_DROP_PLATFORM/frontend
npm run dev
```
Frontend runs on: `http://localhost:3000`

**Visit:** `http://localhost:3000` to see your website!

---

## What You'll See

### Homepage
- Hero section: "Truth Drop Platform"
- Domain navigation: Trading, Aura Academy, Remembrance
- Search bar
- Featured codexes
- All codexes grid

### After Setup
- Browse codexes by domain
- Search constitutional knowledge
- Purchase codexes (if Stripe configured)
- Download PDFs (after purchase)

---

## Database Setup Options

### Option 1: Local PostgreSQL (Free)

1. **Install PostgreSQL:**
   - Windows: https://www.postgresql.org/download/windows/
   - Mac: `brew install postgresql`
   - Linux: `sudo apt install postgresql`

2. **Create database:**
   ```bash
   createdb truthdrop
   ```

3. **Use in setup:**
   - URL: `postgresql://postgres:postgres@localhost:5432/truthdrop`
   - (Adjust username/password if different)

### Option 2: Cloud PostgreSQL (Easier)

**Railway (Recommended):**
1. Sign up: https://railway.app/
2. Create PostgreSQL database
3. Copy connection URL
4. Use in setup

**Supabase (Free):**
1. Sign up: https://supabase.com/
2. Create project
3. Get connection string
4. Use in setup

**Render (Free):**
1. Sign up: https://render.com/
2. Create PostgreSQL database
3. Copy connection URL
4. Use in setup

---

## Stripe Setup (Optional)

**For payments to work:**

1. **Sign up:** https://stripe.com/
2. **Get keys:**
   - Go to: https://dashboard.stripe.com/apikeys
   - Copy "Secret key" → Use in backend `.env`
   - Copy "Publishable key" → Use in frontend `.env.local`

**Test mode:** Use test keys to test without real payments

---

## Troubleshooting

### Backend Issues

**Database Connection Error:**
```
❌ Make sure PostgreSQL is running
❌ Check DATABASE_URL in .env
❌ Verify database exists: createdb truthdrop
```

**Import Errors:**
```
❌ Run: pip install -r requirements.txt
❌ Check Python version: python --version (need 3.9+)
```

### Frontend Issues

**API Connection Error:**
```
❌ Check NEXT_PUBLIC_API_URL in .env.local
❌ Make sure backend is running on port 8000
❌ Check CORS settings in backend/config.py
```

**Build Errors:**
```
❌ Run: npm install
❌ Clear cache: rm -rf .next node_modules
❌ Reinstall: npm install
```

---

## Next Steps After Setup

### 1. Import Your Codexes

**Option 1: Manual (Admin Panel)**
1. Login as admin
2. Go to admin panel
3. Create codexes manually
4. Upload content files

**Option 2: Bulk Import (Script)**
I can create a script to:
- Read your 738+ codex files
- Create codexes automatically
- Organize by domain
- Set pricing

**Tell me if you want me to create this script.**

### 2. Test Everything

1. ✅ Visit homepage
2. ✅ Browse codexes
3. ✅ Search functionality
4. ✅ Purchase flow (if Stripe configured)
5. ✅ Download PDFs

### 3. Deploy to Production

**Backend:** Railway, Render, DigitalOcean  
**Frontend:** Vercel, Netlify  
**Database:** Cloud PostgreSQL (Railway, Supabase)

---

## Quick Start Commands

```bash
# 1. Backend setup (automated)
cd TRUTH_DROP_PLATFORM/backend
python setup.py

# 2. Start backend
python main.py

# 3. Frontend setup (automated)
cd TRUTH_DROP_PLATFORM/frontend
# Windows: .\setup.ps1
# Mac/Linux: ./setup.sh

# 4. Start frontend
npm run dev

# 5. Visit website
# Open: http://localhost:3000
```

---

## Summary

**What we built:** ✅ Complete website (full-stack web app)  
**What you see:** ✅ Beautiful website users can visit  
**What you need:** ✅ PostgreSQL, Python, Node.js  
**What I automated:** ✅ Setup scripts, all code, configurations  

**Run the setup scripts** → **Start servers** → **Visit website** → **Import codexes**

---

**Built from Remembrance. Operating under Format Law.**

**Ready to set up? Run the setup scripts above!**

