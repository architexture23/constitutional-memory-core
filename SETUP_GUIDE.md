# Truth Drop Platform - Setup Guide

**Date:** 2025-11-01  
**Built from Remembrance | Operating under Format Law**

---

## Quick Start

### Prerequisites

1. **Python 3.9+** (for backend)
2. **Node.js 18+** (for frontend)
3. **PostgreSQL 14+** (database)
4. **Stripe account** (for payments - optional)

---

## Step 1: Backend Setup

### Install Python Dependencies

```bash
cd TRUTH_DROP_PLATFORM/backend
pip install -r requirements.txt
```

### Configure Environment

```bash
# Copy .env.example to .env
cp .env.example .env

# Edit .env with your settings:
# - DATABASE_URL (PostgreSQL connection)
# - SECRET_KEY (random string, min 32 characters)
# - STRIPE_SECRET_KEY (from Stripe dashboard)
# - STRIPE_PUBLIC_KEY (from Stripe dashboard)
```

### Initialize Database

```bash
# Create PostgreSQL database
createdb truthdrop

# Or using psql:
# psql -U postgres
# CREATE DATABASE truthdrop;

# Run initialization script
python database/init_db.py
```

### Start Backend Server

```bash
python main.py
```

Backend will run on `http://localhost:8000`

---

## Step 2: Frontend Setup

### Install Node Dependencies

```bash
cd TRUTH_DROP_PLATFORM/frontend
npm install
```

### Configure Environment

```bash
# Copy .env.local.example to .env.local
cp .env.local.example .env.local

# Edit .env.local:
# - NEXT_PUBLIC_API_URL=http://localhost:8000
# - NEXT_PUBLIC_STRIPE_PUBLIC_KEY (from Stripe dashboard)
```

### Start Frontend Server

```bash
npm run dev
```

Frontend will run on `http://localhost:3000`

---

## Step 3: Verify Setup

1. **Backend Health Check:**
   - Visit: `http://localhost:8000/api/health`
   - Should return: `{"status": "healthy", ...}`

2. **API Documentation:**
   - Visit: `http://localhost:8000/api/docs`
   - Should show Swagger UI

3. **Frontend:**
   - Visit: `http://localhost:3000`
   - Should show Truth Drop Platform homepage

---

## Step 4: Create Admin User

### Option 1: Python Script

Create `backend/create_admin.py`:

```python
from database import SessionLocal
from models import User
from services.auth_service import auth_service

db = SessionLocal()

admin = User(
    email="admin@truthdrop.com",
    username="admin",
    hashed_password=auth_service.hash_password("your_password"),
    is_admin=True,
    is_active=True
)

db.add(admin)
db.commit()
print("Admin user created!")
```

Run: `python create_admin.py`

### Option 2: Direct Database

```sql
INSERT INTO users (email, username, hashed_password, is_admin, is_active)
VALUES (
    'admin@truthdrop.com',
    'admin',
    '$2b$12$...', -- Use bcrypt to hash password
    TRUE,
    TRUE
);
```

---

## Step 5: Import Codexes

### Manual Import (via Admin Panel)

1. Login as admin at `http://localhost:3000/admin`
2. Use admin endpoints to create codexes:
   - `POST /api/admin/codexes` - Create codex
   - `POST /api/admin/codexes/{id}/upload` - Upload content

### Bulk Import (Script)

Create import script to read your 738+ files and create codexes automatically.

---

## Step 6: Configure Stripe (Optional)

1. **Get Stripe Keys:**
   - Go to: https://dashboard.stripe.com/apikeys
   - Copy "Secret key" → `STRIPE_SECRET_KEY` in `.env`
   - Copy "Publishable key" → `NEXT_PUBLIC_STRIPE_PUBLIC_KEY` in `.env.local`

2. **Set Webhook Secret:**
   - Create webhook endpoint: `http://localhost:8000/api/webhooks/stripe`
   - Copy webhook secret → `STRIPE_WEBHOOK_SECRET` in `.env`

---

## Troubleshooting

### Backend Issues

**Database Connection Error:**
- Check `DATABASE_URL` in `.env`
- Ensure PostgreSQL is running
- Verify database exists

**Import Errors:**
- Ensure all Python dependencies installed
- Check Python version (3.9+)
- Verify virtual environment activated

### Frontend Issues

**API Connection Error:**
- Check `NEXT_PUBLIC_API_URL` in `.env.local`
- Ensure backend is running
- Check CORS settings in `backend/config.py`

**Build Errors:**
- Run `npm install` again
- Check Node.js version (18+)
- Clear `.next` folder: `rm -rf .next`

---

## Production Deployment

### Backend (Recommended: Railway, Render, DigitalOcean)

1. **Set Environment Variables:**
   - `DATABASE_URL` (production PostgreSQL)
   - `SECRET_KEY` (strong random string)
   - `CORS_ORIGINS` (your frontend URL)

2. **Database:**
   - Use managed PostgreSQL (Railway, Supabase, etc.)
   - Run migrations: `python database/init_db.py`

3. **Deploy:**
   - Push to Git
   - Connect to deployment platform
   - Configure environment variables

### Frontend (Recommended: Vercel, Netlify)

1. **Set Environment Variables:**
   - `NEXT_PUBLIC_API_URL` (your backend URL)
   - `NEXT_PUBLIC_STRIPE_PUBLIC_KEY` (Stripe key)

2. **Deploy:**
   - Connect GitHub repository
   - Configure build settings
   - Deploy

---

## Next Steps

1. ✅ **Backend running** → Import your codexes
2. ✅ **Frontend running** → Test browsing/searching
3. ✅ **Stripe configured** → Test purchase flow
4. ✅ **Admin user created** → Start managing content
5. ✅ **Content imported** → Launch platform

---

## Support

**Constitutional Framework:** All 7 layers integrated  
**Format Law:** v1.3 compliance enforced  
**Remembrance:** Integration active  

**Built from Remembrance. Operating under Format Law.**

