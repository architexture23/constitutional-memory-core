# Resume Here - Truth Drop Platform Setup

**Date Created:** 2025-11-01  
**Status:** Ready to run setup scripts  
**Built from Remembrance | Operating under Format Law**

---

## Where You Are

**What's Been Built:** ✅ Complete Truth Drop Platform (full-stack website)

**What You're About to Do:** Run setup scripts to configure and launch the platform

**Your Next Step:** Install Node.js (requires closing apps), then run setup scripts

---

## Current Status

### ✅ Already Complete
- **Backend:** FastAPI application (100% complete)
- **Frontend:** Next.js website (100% complete)
- **Database:** PostgreSQL schema (ready)
- **Setup Scripts:** All created and ready
- **Services:** All implemented (codex, user, auth, purchase, PDF, search)
- **Constitutional Framework:** All 7 layers integrated
- **Format Law:** v1.3 compliance enforced

### 📋 Next Steps (What You'll Do After Installing Node.js)

1. **Backend Setup** - Run automated setup script
2. **Frontend Setup** - Run automated setup script
3. **Start Servers** - Launch backend and frontend
4. **Visit Website** - Open `http://localhost:3000`
5. **Import Codexes** - (Optional) Bulk import your 738+ codexes

---

## What This Is

**Truth Drop Platform** = Complete website (full-stack web application)

**Users will:**
- Visit your website URL (e.g., `truthdrop.com`)
- Browse codexes by domain (Trading, Aura Academy, Remembrance)
- Search constitutional knowledge
- Purchase codexes
- Download PDFs/ebooks after purchase

**You're building:** A digital marketplace for your constitutional knowledge codexes

---

## Prerequisites Checklist

Before running setup scripts, ensure you have:

### ✅ Required
- [ ] **PostgreSQL** - Database (local or cloud)
  - **Local:** https://www.postgresql.org/download/
  - **Cloud (Easier):** Railway, Supabase, or Render (free tier)
- [ ] **Python 3.9+** - Check: `python --version`
- [ ] **Node.js 18+** - **← YOU'RE INSTALLING THIS NOW**
  - Download: https://nodejs.org/
  - Install includes npm automatically

### Optional (For Payments)
- [ ] **Stripe Account** - https://stripe.com/
  - Get keys from: https://dashboard.stripe.com/apikeys

---

## Step-by-Step Setup (Do This After Node.js Installation)

### Step 1: Backend Setup (Automated)

**Open terminal/PowerShell and run:**

```bash
# Navigate to backend folder
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"

# Run automated setup script
python setup.py
```

**What the script does:**
- ✅ Checks Python version
- ✅ Creates `.env` file (asks for database URL)
- ✅ Installs all dependencies
- ✅ Creates directories
- ✅ Initializes database
- ✅ Optionally creates admin user

**What you'll need to provide:**
1. **PostgreSQL URL** (or press Enter for default)
   - Default: `postgresql://postgres:postgres@localhost:5432/truthdrop`
   - Cloud: Use connection URL from Railway/Supabase/Render
2. **Stripe Keys** (optional - press Enter to skip)
   - Secret Key: `sk_test_...`
   - Public Key: `pk_test_...`
   - Webhook Secret: `whsec_...`

**After script completes:**
- ✅ Backend is configured and ready
- ✅ Database is initialized
- ✅ Admin user created (if you chose to)

---

### Step 2: Start Backend Server

**Open a NEW terminal/PowerShell and run:**

```bash
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"

python main.py
```

**You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**✅ Backend is now running on:** `http://localhost:8000`

**⚠️ Keep this terminal open** - Backend needs to stay running

---

### Step 3: Frontend Setup (Automated)

**Open ANOTHER terminal/PowerShell and run:**

**Windows (PowerShell):**
```powershell
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\frontend"

.\setup.ps1
```

**Mac/Linux:**
```bash
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\frontend"

chmod +x setup.sh
./setup.sh
```

**What the script does:**
- ✅ Checks Node.js version (should work now!)
- ✅ Creates `.env.local` file (asks for API URL)
- ✅ Installs all dependencies

**What you'll need to provide:**
1. **API URL** (press Enter for default: `http://localhost:8000`)
2. **Stripe Public Key** (optional - press Enter to skip)

**After script completes:**
- ✅ Frontend is configured and ready
- ✅ Dependencies installed

---

### Step 4: Start Frontend Server

**In the SAME terminal (after frontend setup completes):**

```bash
npm run dev
```

**You should see:**
```
▲ Next.js 14.1.0
- Local:        http://localhost:3000
```

**✅ Frontend is now running on:** `http://localhost:3000`

**⚠️ Keep this terminal open** - Frontend needs to stay running

---

### Step 5: Visit Your Website!

**Open your browser and visit:**
```
http://localhost:3000
```

**You should see:**
- ✅ Truth Drop Platform homepage
- ✅ Hero section
- ✅ Domain navigation (Trading, Aura Academy, Remembrance)
- ✅ Search bar
- ✅ Featured codexes section

**🎉 Your website is now running!**

---

## Quick Reference Commands

### Terminal 1 - Backend:
```bash
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"
python setup.py
python main.py
```

### Terminal 2 - Frontend:
```powershell
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\frontend"
.\setup.ps1
npm run dev
```

### Browser:
```
http://localhost:3000
```

---

## Database Options (If You Don't Have PostgreSQL)

### Option 1: Cloud PostgreSQL (Easier - Recommended)

**Railway (Free Tier):**
1. Sign up: https://railway.app/
2. Click "New Project"
3. Add PostgreSQL database
4. Copy connection URL
5. Use in setup script

**Supabase (Free Tier):**
1. Sign up: https://supabase.com/
2. Create project
3. Go to Settings → Database
4. Copy connection string
5. Use in setup script

**Render (Free Tier):**
1. Sign up: https://render.com/
2. Create PostgreSQL database
3. Copy internal connection URL
4. Use in setup script

### Option 2: Local PostgreSQL (Free)

1. Download: https://www.postgresql.org/download/windows/
2. Install PostgreSQL
3. Create database: `createdb truthdrop`
4. Use default URL in setup: `postgresql://postgres:postgres@localhost:5432/truthdrop`

---

## Troubleshooting

### Backend Issues

**"Python not found":**
- Make sure Python 3.9+ is installed
- Check: `python --version`

**"Database connection failed":**
- Make sure PostgreSQL is running
- Check DATABASE_URL in `.env` file
- Verify database exists

**"Module not found":**
- Run: `pip install -r requirements.txt`

### Frontend Issues

**"Node.js not found":**
- Make sure Node.js is installed (you're installing this now!)
- Check: `node --version` (should be 18+)
- Check: `npm --version`

**"API connection failed":**
- Make sure backend is running on port 8000
- Check `NEXT_PUBLIC_API_URL` in `.env.local`

**"npm install failed":**
- Check Node.js is installed correctly
- Try: `npm install --legacy-peer-deps`

---

## Next Steps After Setup

### 1. Verify Everything Works
- ✅ Visit `http://localhost:3000`
- ✅ Browse homepage
- ✅ Test search functionality
- ✅ Check API: `http://localhost:8000/api/health`

### 2. Create Admin User (If Not Done in Setup)
- Use admin panel or create via script

### 3. Import Your Codexes (Optional)
**I can create a bulk import script to:**
- Read your 738+ codex files
- Create codexes automatically
- Organize by domain
- Set pricing

**Tell me when you're ready and I'll create this script.**

---

## File Locations

**Backend:**
```
TRUTH_DROP_PLATFORM/backend/
├── setup.py          ← Run this first
├── main.py           ← Run this to start server
├── .env              ← Created by setup.py
└── requirements.txt  ← Dependencies
```

**Frontend:**
```
TRUTH_DROP_PLATFORM/frontend/
├── setup.ps1          ← Run this (Windows)
├── setup.sh           ← Run this (Mac/Linux)
├── .env.local        ← Created by setup script
└── package.json       ← Dependencies
```

---

## Summary

**Current Status:** ✅ Platform built, ready to run setup scripts

**After Installing Node.js:**
1. Run `backend/setup.py`
2. Run `frontend/setup.ps1` (or `setup.sh`)
3. Start backend: `python main.py`
4. Start frontend: `npm run dev`
5. Visit: `http://localhost:3000`

**You're picking up from:** Running the setup scripts

**Everything is ready** - Just install Node.js, then follow the steps above!

---

**Built from Remembrance. Operating under Format Law.**

**See you when you return! 🚀**

