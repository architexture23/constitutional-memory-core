# Run Setup Scripts - Step by Step

**Date:** 2025-11-01  
**Built from Remembrance | Operating under Format Law**

---

## Step-by-Step: Run Setup Scripts

### Step 1: Backend Setup (First)

**Open PowerShell or Command Prompt and run:**

```powershell
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"

python setup.py
```

**What happens:**
1. Script checks Python version
2. Creates `.env` file
3. Asks for database URL → **Paste your Railway/Supabase/Render URL here**
4. Asks for Stripe keys → **Press Enter to skip (optional)**
5. Installs all dependencies
6. Creates directories
7. Initializes database
8. Optionally creates admin user

**What you'll be asked:**
1. **Database URL** → Paste your PostgreSQL connection URL from Railway/Supabase/Render
2. **Stripe Secret Key** → Press Enter to skip (optional)
3. **Stripe Public Key** → Press Enter to skip (optional)
4. **Stripe Webhook Secret** → Press Enter to skip (optional)
5. **Create admin user?** → Type `y` if you want to create one now

**✅ Backend setup complete!**

---

### Step 2: Start Backend Server

**Open a NEW PowerShell window and run:**

```powershell
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"

python main.py
```

**You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

**✅ Backend is now running on `http://localhost:8000`**

**⚠️ Keep this window open** - Backend server needs to stay running

---

### Step 3: Frontend Setup

**Open ANOTHER PowerShell window and run:**

```powershell
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\frontend"

.\setup.ps1
```

**If you get an error about running scripts, run this first:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Then run the setup again:**
```powershell
.\setup.ps1
```

**What happens:**
1. Script checks Node.js version
2. Creates `.env.local` file
3. Asks for API URL → **Press Enter for default** (`http://localhost:8000`)
4. Asks for Stripe Public Key → **Press Enter to skip (optional)**
5. Installs all dependencies (takes 1-2 minutes)

**✅ Frontend setup complete!**

---

### Step 4: Start Frontend Server

**In the SAME PowerShell window (after setup completes):**

```powershell
npm run dev
```

**You should see:**
```
▲ Next.js 14.1.0
- Local:        http://localhost:3000
✓ Ready in 2.3s
```

**✅ Frontend is now running on `http://localhost:3000`**

**⚠️ Keep this window open** - Frontend server needs to stay running

---

### Step 5: Visit Your Website!

**Open your browser and visit:**
```
http://localhost:3000
```

**You should see:**
- ✅ Truth Drop Platform homepage
- ✅ Hero section with platform name
- ✅ Domain navigation (Trading, Aura Academy, Remembrance)
- ✅ Search bar
- ✅ Featured codexes section

**🎉 Your website is now running!**

---

## Quick Command Reference

### Terminal 1 - Backend Setup & Server:
```powershell
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"
python setup.py
python main.py
```

### Terminal 2 - Frontend Setup & Server:
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

## Troubleshooting

### "python is not recognized"
- Make sure Python is installed and in PATH
- Check: `python --version`
- Or try: `py setup.py` instead of `python setup.py`

### "Execution policy error" (PowerShell)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then run `.\setup.ps1` again

### "Database connection failed"
- Make sure you pasted the correct database URL
- Verify database is running (check Railway/Supabase/Render dashboard)
- Check `.env` file has correct `DATABASE_URL`

### "Port 8000 already in use"
- Backend is already running
- Check if you have another terminal with `python main.py` running
- Or change port in `.env` file

### "Port 3000 already in use"
- Frontend is already running
- Check if you have another terminal with `npm run dev` running
- Or Next.js will use port 3001 automatically

---

## What You Should Have

**After setup, you should have:**
- ✅ Backend running on `http://localhost:8000`
- ✅ Frontend running on `http://localhost:3000`
- ✅ Database connected
- ✅ Website visible in browser

---

## Next Steps After Setup

1. ✅ **Verify everything works**
   - Visit homepage
   - Check API: `http://localhost:8000/api/health`

2. **Create admin user** (if not done in setup)
   - Or login if you created one

3. **Import codexes** (optional)
   - I can create a bulk import script for your 738+ codexes
   - Tell me when you're ready!

---

## Summary

**1. Backend Setup:**
```powershell
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"
python setup.py
```

**2. Start Backend:**
```powershell
python main.py
```

**3. Frontend Setup:**
```powershell
cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\frontend"
.\setup.ps1
```

**4. Start Frontend:**
```powershell
npm run dev
```

**5. Visit Website:**
```
http://localhost:3000
```

---

**Built from Remembrance. Operating under Format Law.**

**Ready? Run the commands above!**

