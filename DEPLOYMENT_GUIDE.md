# 🚀 DEPLOYMENT GUIDE - Make Platform Public

## Overview

To make your Truth Drop Platform public, you need to:
1. **Deploy Backend** (Railway recommended - you're already using it for database)
2. **Deploy Frontend** (Vercel - free, easy)
3. **Configure Stripe Webhooks** (for automatic fulfillment)
4. **Update Environment Variables** (with public URLs)

---

## 📋 STEP 1: Deploy Backend to Railway

### Option A: Deploy from GitHub (Recommended)

1. **Push code to GitHub**:
   ```bash
   cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"
   git init
   git add .
   git commit -m "Initial backend deployment"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy on Railway**:
   - Go to https://railway.app
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your backend repository
   - Railway will auto-detect Python and deploy

3. **Configure Environment Variables in Railway**:
   - Go to your Railway project → Variables tab
   - Add all variables from `backend/.env`:
     - `DATABASE_URL` (already set from your existing Railway DB)
     - `STRIPE_SECRET_KEY`
     - `STRIPE_PUBLIC_KEY`
     - `STRIPE_WEBHOOK_SECRET` (get this after webhook setup - see Step 3)
     - `CORS_ORIGINS` (set to your frontend URL, e.g., `https://your-app.vercel.app`)
     - `FRONTEND_URL` (set to your frontend URL)

4. **Get your backend URL**:
   - Railway gives you a URL like: `https://your-backend.railway.app`
   - Save this - you'll need it for frontend and Stripe webhook

### Option B: Deploy from Local (Alternative)

1. Install Railway CLI:
   ```powershell
   npm install -g @railway/cli
   railway login
   ```

2. Deploy:
   ```powershell
   cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"
   railway init
   railway up
   ```

---

## 📋 STEP 2: Deploy Frontend to Vercel

### Quick Deploy (5 minutes)

1. **Install Vercel CLI**:
   ```powershell
   npm install -g vercel
   ```

2. **Deploy**:
   ```powershell
   cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\frontend"
   vercel login
   vercel
   ```

3. **Configure Environment Variables in Vercel**:
   - After deployment, go to Vercel dashboard → Your Project → Settings → Environment Variables
   - Add:
     - `NEXT_PUBLIC_API_URL` = `https://your-backend.railway.app` (your Railway backend URL)
     - `NEXT_PUBLIC_STRIPE_PUBLIC_KEY` = `pk_test_...` (your Stripe public key)

4. **Redeploy** (to apply env vars):
   ```powershell
   vercel --prod
   ```

### Alternative: Deploy from GitHub

1. Push frontend to GitHub
2. Go to https://vercel.com
3. Import your GitHub repository
4. Configure environment variables (same as above)
5. Deploy

---

## 📋 STEP 3: Configure Stripe Webhook (For Automatic Fulfillment)

### Setup Webhook in Stripe Dashboard

1. **Go to Stripe Dashboard**: https://dashboard.stripe.com/test/webhooks
2. **Click "Add endpoint"**
3. **Enter endpoint URL**:
   ```
   https://your-backend.railway.app/api/stripe-webhook
   ```
   (Replace with your actual Railway backend URL)

4. **Select events to listen to**:
   - `checkout.session.completed` ✅ (most important)
   - Optionally: `payment_intent.succeeded`, `charge.succeeded`

5. **Copy the Signing Secret**:
   - After creating webhook, click on it
   - Copy the "Signing secret" (starts with `whsec_`)

6. **Add to Railway Environment Variables**:
   - Go to Railway → Your Backend → Variables
   - Add: `STRIPE_WEBHOOK_SECRET` = `whsec_...`
   - Redeploy backend (Railway auto-redeploys when vars change)

---

## 📋 STEP 4: Test Everything

1. **Test Purchase Flow**:
   - Go to your public frontend URL
   - Click "Purchase Now" on a codex
   - Complete test payment with card: `4242 4242 4242 4242`
   - Verify redirect to success page

2. **Check Stripe Dashboard**:
   - Go to Stripe → Payments
   - You should see the test payment
   - Check webhook logs to see if events are received

3. **Check Backend Logs**:
   - Railway dashboard → Your Backend → Deployments → View Logs
   - Should see webhook events being processed

---

## 🎯 ENVIRONMENT VARIABLES SUMMARY

### Backend (Railway):
```
DATABASE_URL=postgresql://... (from Railway DB)
STRIPE_SECRET_KEY=sk_test_... or sk_live_... (when ready)
STRIPE_PUBLIC_KEY=pk_test_... or pk_live_... (when ready)
STRIPE_WEBHOOK_SECRET=whsec_... (from Stripe webhook)
CORS_ORIGINS=https://your-app.vercel.app
FRONTEND_URL=https://your-app.vercel.app
```

### Frontend (Vercel):
```
NEXT_PUBLIC_API_URL=https://your-backend.railway.app
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=pk_test_... or pk_live_...
```

---

## ⚠️ IMPORTANT NOTES

1. **Test Mode vs Live Mode**:
   - Currently using Stripe **test keys** (`sk_test_`, `pk_test_`)
   - When ready for real payments, switch to **live keys** in Stripe dashboard
   - Update environment variables with live keys

2. **Database**:
   - You're already using Railway PostgreSQL ✅
   - Just make sure `DATABASE_URL` is set correctly

3. **CORS**:
   - Make sure `CORS_ORIGINS` includes your frontend URL
   - No trailing slash!

---

## 🚀 QUICK START (TL;DR)

```powershell
# 1. Deploy Backend (Railway)
# - Push to GitHub, connect to Railway, set env vars

# 2. Deploy Frontend (Vercel)
cd frontend
vercel login
vercel

# 3. Set Vercel env vars
# NEXT_PUBLIC_API_URL = your Railway URL
# NEXT_PUBLIC_STRIPE_PUBLIC_KEY = your Stripe key

# 4. Configure Stripe Webhook
# - Add endpoint in Stripe dashboard
# - Copy webhook secret
# - Add to Railway env vars

# 5. Test!
```

**Done! Your platform is now public!** 🎉

