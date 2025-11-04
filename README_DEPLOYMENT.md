# Truth Drop Platform - Going Live Guide

## 🎯 Current Status: READY FOR DEPLOYMENT

Your platform is fully functional locally. All core features are working:
- ✅ Purchase flow (tested with free codex)
- ✅ Download functionality
- ✅ Purchase confirmation pages
- ✅ Secure access tokens

## 📋 Simple 3-Step Deployment

### Step 1: Deploy Backend (10 minutes)
**Railway.app (Easiest)**
1. Go to https://railway.app
2. Sign up/login
3. Click "New Project"
4. Select "Deploy from GitHub repo" OR "Empty Project"
5. If empty: Add PostgreSQL service first
6. Add Python service
7. Connect your repo OR upload backend folder
8. Set environment variables (see below)
9. Deploy

**Your backend URL will be:** `https://your-app-name.railway.app`

### Step 2: Deploy Frontend (5 minutes)
**Vercel (Recommended)**
1. Go to https://vercel.com
2. Sign up/login (can use GitHub account)
3. Click "Add New Project"
4. Import your GitHub repo OR upload frontend folder
5. Set Root Directory to: `frontend`
6. Add Environment Variable:
   - Key: `NEXT_PUBLIC_API_URL`
   - Value: Your Railway backend URL (from Step 1)
7. Deploy

**Your frontend URL will be:** `https://your-app-name.vercel.app`

### Step 3: Configure Production
1. Get production Stripe keys (live mode)
2. Add to Railway environment variables
3. Create Stripe webhook pointing to your backend
4. Add webhook secret to Railway env vars
5. Test purchase with real test card

## 🔑 Environment Variables Needed

### Railway (Backend)
```
DATABASE_URL=<your-railway-postgres-url>
STRIPE_SECRET_KEY=sk_live_...
STRIPE_PUBLIC_KEY=pk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
CORS_ORIGINS=["https://your-frontend.vercel.app"]
FRONTEND_URL=https://your-frontend.vercel.app
```

### Vercel (Frontend)
```
NEXT_PUBLIC_API_URL=https://your-backend.railway.app
```

## ✅ What I've Already Created For You

1. ✅ `DEPLOYMENT_CHECKLIST.md` - Complete deployment guide
2. ✅ `vercel.json` - Frontend deployment config
3. ✅ `railway.json` - Backend deployment config  
4. ✅ `Procfile` - For platforms like Heroku/Render
5. ✅ `runtime.txt` - Python version specification

## 🚀 Quick Deploy Commands

**Test locally first:**
```powershell
# Backend
cd backend
python main.py

# Frontend (new terminal)
cd frontend
npm run dev
```

**Build for production:**
```powershell
# Frontend only (backend doesn't need build)
cd frontend
npm run build
```

## 🎉 After Deployment

Once both are live:
1. Test purchase flow with Stripe test card
2. Verify download works
3. Check email notifications (if configured)
4. Share your platform!

## 💡 Pro Tips

- **Railway** and **Vercel** both provide free tiers
- Both automatically handle HTTPS/SSL
- Both auto-deploy on git push (if connected to GitHub)
- Railway PostgreSQL is included free tier

## ❓ Need Help?

If you hit any issues during deployment, share the error and I'll help fix it!

