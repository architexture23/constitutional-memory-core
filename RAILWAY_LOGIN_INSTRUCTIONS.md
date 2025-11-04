# Railway Login Instructions

**Date:** 2025-11-03  
**Status:** Ready for Railway CLI Authentication

---

## Step 1: Stop Backend Server (If Running)

If the backend is running and you can't type in the terminal:
1. **Press `Ctrl+C`** in the terminal where the backend is running
   - This will stop the server gracefully
2. **OR** close that terminal window and open a new one

---

## Step 2: Railway Login

After stopping the backend, run:

```powershell
cd TRUTH_DROP_PLATFORM\backend
railway login
```

This will:
- Open your browser
- Ask you to authenticate with Railway
- You'll need your Railway account credentials:
  - **Email:** `rdtiptoe2@gmail.com`
  - **Password:** (your Railway password)

---

## Step 3: If Railway Login Fails

### Option A: Wrong Password
If you forgot your Railway password:
1. Go to: https://railway.app/login
2. Click "Forgot Password"
3. Reset using `rdtiptoe2@gmail.com`
4. Then try `railway login` again

### Option B: Need to Create Railway Account
If you don't have a Railway account yet:
1. Go to: https://railway.app/signup
2. Sign up with `rdtiptoe2@gmail.com`
3. Then run `railway login`

### Option C: Account Already Created
We already created a Railway project via browser, so you should be logged in via web. The CLI might need separate authentication.

---

## Step 4: After Successful Login

Once `railway login` succeeds, run:

```powershell
railway link -p ce2ffc15-0e22-4b04-8632-27d70e72701b
railway up
```

---

## Current Railway Project Info:

- **Project ID:** `ce2ffc15-0e22-4b04-8632-27d70e72701b`
- **Project Name:** `resplendent-transformation`
- **Project URL:** https://railway.app/project/ce2ffc15-0e22-4b04-8632-27d70e72701b
- **Environment:** `production`

---

## Quick Command Sequence:

```powershell
# 1. Stop backend (if running) - Press Ctrl+C in backend terminal

# 2. Navigate to backend
cd TRUTH_DROP_PLATFORM\backend

# 3. Login to Railway
railway login

# 4. Link project (after login succeeds)
railway link -p ce2ffc15-0e22-4b04-8632-27d70e72701b

# 5. Set environment variables (optional - can do via web dashboard)
railway variables set DATABASE_URL=<from .env>
railway variables set FRONTEND_URL=https://frontend-csd4ftpzk-architexture23s-projects.vercel.app

# 6. Deploy
railway up
```

---

**Once you stop the backend and complete Railway login, I can help automate the rest!**

