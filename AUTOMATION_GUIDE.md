# Truth Drop Platform - Automation Guide

## 🤖 What Can Be Automated?

### ✅ Fully Automated (I Can Do)
- Create deployment scripts
- Set up CI/CD pipelines (GitHub Actions)
- Generate configuration files
- Environment variable templates
- Database migration scripts

### ⚠️ Semi-Automated (Needs Your Keys/Login)
- Deploy to Railway (needs Railway CLI login once)
- Deploy to Vercel (needs Vercel CLI login once)
- Set environment variables (needs API keys)

### ❌ Manual (Security/Account Related)
- Sign up for Railway account (one-time)
- Sign up for Vercel account (one-time)
- Get Stripe API keys (one-time)
- Initial Railway/Vercel login (one-time)

## 🚀 Automated Deployment Scripts Created

### 1. PowerShell Script (Windows)
**File:** `deploy_automated.ps1`

**Usage:**
```powershell
cd TRUTH_DROP_PLATFORM
.\deploy_automated.ps1
```

**What it does:**
- Checks if Railway/Vercel CLI installed
- Automatically sets environment variables from .env
- Deploys backend and/or frontend

### 2. Bash Script (Linux/Mac)
**File:** `deploy_automated.sh`

**Usage:**
```bash
cd TRUTH_DROP_PLATFORM
chmod +x deploy_automated.sh
./deploy_automated.sh
```

### 3. Python Script (Cross-platform)
**File:** `backend/deploy_railway.py`

**Usage:**
```powershell
cd TRUTH_DROP_PLATFORM/backend
python deploy_railway.py
```

## 📋 Step-by-Step: First-Time Setup (One-Time Manual Steps)

### Step 1: Install CLIs (One-Time)
```powershell
# Railway CLI
npm install -g @railway/cli

# Vercel CLI
npm install -g vercel
```

### Step 2: Login to Services (One-Time)
```powershell
# Railway (opens browser)
railway login

# Vercel (opens browser)
vercel login
```

### Step 3: Create Railway Project (One-Time)
```powershell
cd TRUTH_DROP_PLATFORM/backend
railway init
# Follow prompts to create project
```

### Step 4: Create Vercel Project (One-Time)
```powershell
cd TRUTH_DROP_PLATFORM/frontend
vercel
# Follow prompts to create project
```

### Step 5: Link Existing Projects (If Already Created)
```powershell
# Railway
cd TRUTH_DROP_PLATFORM/backend
railway link

# Vercel
cd TRUTH_DROP_PLATFORM/frontend
vercel link
```

## ⚡ After First-Time Setup: Fully Automated!

Once set up, you can deploy with **ONE COMMAND**:

```powershell
cd TRUTH_DROP_PLATFORM
.\deploy_automated.ps1
```

**That's it!** The script will:
1. Check prerequisites
2. Set environment variables from .env
3. Deploy backend to Railway
4. Deploy frontend to Vercel
5. Done! 🎉

## 🔄 GitHub Actions (Full CI/CD - Most Automated)

I can also create GitHub Actions that automatically deploy when you push code!

**File:** `.github/workflows/deploy.yml`

**What it does:**
- Automatically deploys on every git push
- Runs tests
- Deploys to Railway (backend)
- Deploys to Vercel (frontend)
- Zero commands needed - just push code!

## 📝 What I Need From You

For full automation, I need:
1. **Railway API Token** (from Railway Dashboard → Settings → Tokens)
2. **Vercel API Token** (from Vercel Dashboard → Settings → Tokens)
3. **Stripe API Keys** (from Stripe Dashboard)

Once I have these, I can create a script that:
- Automatically deploys on every push
- Sets all environment variables
- No manual steps needed!

## 🎯 Current PostgreSQL Service

Your current PostgreSQL is likely on **Railway.app**.

**Check your DATABASE_URL:**
It probably looks like:
```
postgresql://postgres:password@yamanote.proxy.rlwy.net:port/railway
```

The `yamanote.proxy.rlwy.net` indicates Railway's proxy service.

**To find it:**
1. Go to railway.app
2. Open your project
3. Click on PostgreSQL service
4. Click "Connect" tab
5. Copy the Connection URL

## 💡 Recommendation

**Best Option:** GitHub Actions (most automated)
- Push code → Auto-deploy
- No manual steps after initial setup
- Professional CI/CD pipeline

Would you like me to create the GitHub Actions workflow for you?

