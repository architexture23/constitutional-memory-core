# GitHub Actions - Fully Automated Deployment

## 🚀 What This Does

When you push code to GitHub, it **automatically**:
1. Deploys backend to Railway
2. Deploys frontend to Vercel
3. **Zero manual steps needed!**

## 📋 Setup Steps (One-Time, 10 Minutes)

### Step 1: Get API Tokens

**Railway Token:**
1. Go to railway.app → Your Project → Settings → Tokens
2. Click "New Token"
3. Copy the token

**Vercel Token:**
1. Go to vercel.com → Settings → Tokens
2. Click "Create Token"
3. Copy the token

**Vercel Org/Project IDs:**
1. Go to vercel.com → Your Project → Settings → General
2. Copy "Organization ID" and "Project ID"

### Step 2: Add Secrets to GitHub

1. Go to your GitHub repo
2. Click "Settings" → "Secrets and variables" → "Actions"
3. Add these secrets:
   - `RAILWAY_TOKEN` = your Railway token
   - `VERCEL_TOKEN` = your Vercel token
   - `VERCEL_ORG_ID` = your Vercel org ID
   - `VERCEL_PROJECT_ID` = your Vercel project ID

### Step 3: Push Code

```powershell
git add .
git commit -m "Add GitHub Actions workflow"
git push
```

**That's it!** GitHub Actions will automatically deploy!

## ✅ After Setup

**Every time you push code:**
- Automatically deploys to Railway (backend)
- Automatically deploys to Vercel (frontend)
- No commands needed!
- Just: `git push` → Done! 🎉

## 🔍 Check Deployment Status

1. Go to your GitHub repo
2. Click "Actions" tab
3. See deployment progress in real-time

## 💡 Benefits

- ✅ Fully automated
- ✅ Deploys on every push
- ✅ Professional CI/CD
- ✅ Zero manual steps after setup

