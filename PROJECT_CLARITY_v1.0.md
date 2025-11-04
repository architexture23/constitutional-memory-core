# Truth Drop Platform - Project Clarity Documentation

**Date Created:** 2025-11-03  
**Purpose:** Preserve complete project clarity for autonomous future updates and deployments  
**Status:** ✅ Fully Operational

---

## 🎯 Project Overview

**Truth Drop Platform** - A constitutional knowledge marketplace built with:
- **Backend:** FastAPI (Python) on Railway
- **Frontend:** Next.js (React/TypeScript) on Vercel
- **Database:** PostgreSQL (Railway)
- **Payments:** Stripe (Test Mode)
- **Architecture:** Three-layer structure (738 files, constitutional framework)

---

## 🌐 Live URLs

### Production URLs:
- **Frontend:** `https://frontend-three-snowy-298am3ddwj.vercel.app`
- **Backend API:** `https://resplendent-transformation-production.up.railway.app`
- **Railway Project:** `https://railway.app/project/ce2ffc15-0e22-4b04-8632-27d70e72701b`
- **Vercel Project:** `https://vercel.com/architexture23s-projects/frontend`

---

## 🔑 Critical Credentials & Tokens

### Railway:
- **Project ID:** `ce2ffc15-0e22-4b04-8632-27d70e72701b`
- **Service ID:** `c1c098de-0a47-4793-bb22-63f39117e70d`
- **Environment ID:** `5ddbd906-1693-4e83-87a1-23a67c198f52`
- **API Token:** `ad1e4414-15a0-4771-a952-4e479e4004cf`
- **Account:** `rdtiptoe2@gmail.com` / `architexture23`

### Vercel:
- **API Token:** `I9OlHOgMOfHk3XMkn9uRropD`
- **Account:** `Architexture23` (GitHub: `Architexture23` / `Iamaligned369`)

### GitHub:
- **Username:** `Architexture23`
- **Password:** `Iamaligned369`

---

## 📁 Project Structure

```
TRUTH_DROP_PLATFORM/
├── backend/
│   ├── main.py                    # FastAPI app, routes, CORS config
│   ├── config.py                  # Environment variables, Settings class
│   ├── models.py                  # SQLAlchemy models (Codex, Purchase, User, Domain)
│   ├── database.py                # Database connection & session management
│   ├── services/
│   │   ├── purchase_service.py    # Stripe checkout, free codex handling
│   │   └── email_service.py       # SendGrid/SMTP email fulfillment
│   ├── migrations/
│   │   └── add_fulfillment_fields.py  # Database migration script
│   ├── requirements.txt           # Python dependencies
│   └── .env                       # Local environment variables (not in git)
│
└── frontend/
    ├── app/
    │   ├── page.tsx               # Homepage
    │   ├── codexes/
    │   │   └── [slug]/
    │   │       └── page.tsx        # Individual codex page, purchase flow
    │   ├── download/
    │   │   └── [token]/
    │   │       └── page.tsx        # Secure download page
    │   ├── purchase/
    │   │   └── success/
    │   │       └── page.tsx        # Purchase success page
    │   └── search/
    │       └── page.tsx            # Search page
    ├── .env.local                 # Frontend environment variables
    └── package.json               # Node.js dependencies
```

---

## ⚙️ Environment Variables

### Backend (Railway):
- `DATABASE_URL` - PostgreSQL connection string
- `CORS_ORIGINS` - `https://frontend-three-snowy-298am3ddwj.vercel.app,https://frontend-csd4ftpzk-architexture23s-projects.vercel.app,http://localhost:3000`
- `STRIPE_SECRET_KEY` - Stripe secret key (test mode)
- `STRIPE_PUBLIC_KEY` - Stripe public key (test mode)
- `STRIPE_WEBHOOK_SECRET` - Webhook signing secret (for production)
- `SECRET_KEY` - Application secret key
- `FRONTEND_URL` - Frontend deployment URL
- `HOST` - `0.0.0.0`
- `PORT` - `8000`
- `DEBUG` - `false` (production)
- `SENDGRID_API_KEY` - (Optional) For email service
- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD` - (Optional) SMTP config
- `EMAIL_SENDER`, `EMAIL_SENDER_NAME` - Email sender configuration

### Frontend (Vercel):
- `NEXT_PUBLIC_API_URL` - `https://resplendent-transformation-production.up.railway.app`

---

## 🔧 Key Implementation Details

### CORS Configuration:
- **Location:** `backend/main.py` (line ~46)
- **Config:** `allow_origins=settings.CORS_ORIGINS`
- **Settings:** `backend/config.py` - Parses comma-separated string into list

### Purchase Flow:
1. **Free Codexes:** `purchase_service.py` - Bypasses Stripe, creates purchase directly
2. **Paid Codexes:** Creates Stripe Checkout Session, redirects to Stripe
3. **Webhook Handler:** `main.py` - Processes `checkout.session.completed`, sends email
4. **Download:** Token-based secure download via `/api/download/{access_token}`

### Filename Sanitization:
- **Backend:** `main.py` - `re.sub(r'[^\w\s\-.]', '', codex.title).strip()` then `re.sub(r'[-\s]+', '_', safe_filename)`
- **Frontend:** `app/download/[token]/page.tsx` - Same regex logic in fallback
- **Preserves:** Version numbers like `v1.0` (dots allowed in character set)

### Email Service:
- **Priority:** SendGrid > SMTP > Console logging
- **Location:** `backend/services/email_service.py`
- **Current:** Console logging (SendGrid/SMTP not configured)

---

## 🚀 Deployment Process

### Backend (Railway):
1. Ensure Railway CLI authenticated: `railway login`
2. Link service: `railway service c1c098de-0a47-4793-bb22-63f39117e70d`
3. Set environment variables (via Railway dashboard or CLI)
4. Deploy: `railway up`
5. **Note:** Variable changes require redeployment (click "Deploy" in Railway dashboard)

### Frontend (Vercel):
1. Ensure Vercel CLI authenticated: `vercel login`
2. Set environment variables in Vercel dashboard
3. Deploy: `vercel --prod --yes`
4. **Note:** Environment variables require redeploy to take effect

---

## 📝 Common Issues & Solutions

### Issue: CORS Errors
- **Solution:** Update `CORS_ORIGINS` in Railway, then trigger redeployment
- **Check:** Railway Variables page → `CORS_ORIGINS` → Click "Deploy" after edit

### Issue: Frontend shows "No codexes found"
- **Check:** Browser console for CORS errors
- **Check:** `NEXT_PUBLIC_API_URL` in Vercel environment variables
- **Check:** Backend health: `https://resplendent-transformation-production.up.railway.app/api/codexes`

### Issue: Download filename incorrect
- **Backend:** Ensure `Content-Disposition` header includes `filename*=UTF-8''...`
- **Frontend:** Check `Content-Disposition` header parsing in `handleDownload`

### Issue: Free codex purchase fails
- **Check:** `purchase_service.py` - `if codex.price is not None and float(codex.price) <= 0.0:`

---

## 🔐 Security Considerations

### Production Checklist:
- [ ] Stripe webhook secret configured in Railway
- [ ] Stripe webhook endpoint configured in Stripe Dashboard
- [ ] Email service configured (SendGrid or SMTP)
- [ ] `DEBUG=false` in production
- [ ] `SECRET_KEY` is strong and unique
- [ ] CORS origins limited to production URLs only
- [ ] Database credentials secure

---

## 🛠️ Future Update Patterns

### Making Backend Changes:
1. Edit code in `backend/` directory
2. Test locally: `python main.py`
3. Deploy to Railway: `railway up` (or via dashboard)
4. Verify deployment: Check Railway logs

### Making Frontend Changes:
1. Edit code in `frontend/app/` directory
2. Test locally: `npm run dev`
3. Deploy to Vercel: `vercel --prod --yes` (or via dashboard)
4. Verify deployment: Check Vercel logs

### Adding New Environment Variables:
1. Update `backend/config.py` if needed
2. Add to Railway Variables (via dashboard)
3. Add to Vercel Environment Variables if frontend needs it
4. Redeploy affected service

### Database Migrations:
1. Create migration script in `backend/migrations/`
2. Run locally to test
3. Execute on Railway database (via Railway dashboard SQL or CLI)

---

## 📊 Current Status

### ✅ Completed:
- Backend deployed to Railway
- Frontend deployed to Vercel
- CORS configuration working
- Database connected (6 codexes)
- Purchase flow implemented (free + paid)
- Download system with secure tokens
- Email service structure (console fallback)
- Filename sanitization (preserves version numbers)

### ⚠️ Optional Enhancements:
- Email service configuration (SendGrid/SMTP)
- Stripe webhook production configuration
- Custom domain setup (if desired)
- Analytics integration
- Performance monitoring

---

## 🎨 Design Philosophy

- **Constitutional Structure:** Built from Remembrance, operating under Format Law
- **Three-Layer Architecture:** Structural Setup → Confirmation Cascade
- **Format Law Compliance:** v1.3 Compliance
- **Detail Enforcement Mode:** Zero shorthand, zero ambiguity

---

## 🔄 Update Workflow

1. **Identify Change:** User request or autonomous improvement
2. **Locate Code:** Use this clarity document to find relevant files
3. **Make Changes:** Edit with precision, maintain format law compliance
4. **Test Locally:** Verify changes work before deployment
5. **Deploy:** Use appropriate deployment method (Railway/Vercel)
6. **Verify:** Test in production environment
7. **Update Documentation:** Keep this clarity document current

---

**End of Project Clarity Documentation v1.0**

