# Truth Drop Platform - Deployment Checklist

## ✅ What's Complete (Local Development)
- [x] Backend API running on localhost:8000
- [x] Frontend running on localhost:3000
- [x] Database connected (Railway PostgreSQL)
- [x] Purchase flow working (free codex tested)
- [x] Download functionality working
- [x] Filename formatting correct (v1.0 with underscores)
- [x] Purchase confirmation page working

## 🚀 Next Steps: Going Live

### Step 1: Deploy Backend (Railway/Render)
**Option A: Railway (Recommended - Easy)**
1. Create account at railway.app
2. New Project → Deploy from GitHub repo
3. Add PostgreSQL service (or use existing Railway DB)
4. Set environment variables (see below)

**Option B: Render**
1. Create account at render.com
2. New Web Service → Connect GitHub repo
3. Build command: `cd backend && pip install -r requirements.txt`
4. Start command: `cd backend && python main.py`

### Step 2: Deploy Frontend (Vercel - Recommended)
1. Create account at vercel.com
2. New Project → Import GitHub repo
3. Root directory: `frontend`
4. Set environment variable: `NEXT_PUBLIC_API_URL` = your backend URL
5. Deploy

### Step 3: Environment Variables Setup

#### Backend (.env) - Production
```
DATABASE_URL=your_production_postgres_url
STRIPE_SECRET_KEY=sk_live_...
STRIPE_PUBLIC_KEY=pk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
CORS_ORIGINS=["https://yourdomain.com"]
FRONTEND_URL=https://yourdomain.com
EMAIL_SENDER=your@email.com
EMAIL_SENDER_NAME=Truth Drop Platform
```

#### Frontend (.env.local) - Production
```
NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app
```

### Step 4: Stripe Setup (Production)
1. Get live API keys from Stripe Dashboard
2. Create webhook endpoint: `https://your-backend-url.com/api/webhooks/stripe`
3. Set webhook secret in backend .env
4. Test with Stripe test cards first

### Step 5: Database Migration (Production)
1. Run migrations on production database
2. Seed initial data if needed
3. Verify all tables created

### Step 6: Final Testing
- [ ] Test purchase flow with test card
- [ ] Verify download works
- [ ] Check email notifications (if configured)
- [ ] Test on mobile devices
- [ ] Verify all links work

## 📋 Quick Start Commands

### Local Development
```powershell
# Backend
cd TRUTH_DROP_PLATFORM/backend
python main.py

# Frontend (new terminal)
cd TRUTH_DROP_PLATFORM/frontend
npm run dev
```

### Production Build
```powershell
# Backend - no build needed, just deploy

# Frontend
cd TRUTH_DROP_PLATFORM/frontend
npm run build
```

## 🔒 Security Checklist
- [ ] Use production database (not local)
- [ ] Use live Stripe keys (not test keys)
- [ ] CORS configured for your domain only
- [ ] Environment variables set in hosting platform
- [ ] Webhook secret configured
- [ ] HTTPS enabled (required for Stripe)

## 📝 Notes
- Railway provides HTTPS automatically
- Vercel provides HTTPS automatically
- Both platforms handle SSL certificates
- No need for separate SSL setup

