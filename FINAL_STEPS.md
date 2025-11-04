# Final Deployment Steps

**Status:** Almost there! Just need two things:

---

## ✅ What's Done:
- ✅ Railway project created
- ✅ Project linked successfully
- ✅ Frontend deployed to Vercel

---

## ⏳ What's Left:

### 1. Link Service (In terminal where you logged in)
```powershell
railway service c1c098de-0a47-4793-bb22-63f39117e70d
```

### 2. Upgrade Railway Plan
- **Current:** Trial plan (only allows database deployments)
- **Needed:** Hobby plan ($5/month) to deploy code
- **Go to:** https://railway.app/workspace/plans
- **Click:** "Deploy with Hobby" button
- **Cost:** $5/month minimum (includes $5 usage credits)

### 3. Set Environment Variables (After service linked)
```powershell
railway variables --set "FRONTEND_URL=https://frontend-csd4ftpzk-architexture23s-projects.vercel.app"
railway variables --set "DATABASE_URL=postgresql://postgres:yBICuFzSKbAoeQBXxlULQEyeZgOTvEup@yamanote.proxy.rlwy.net:56573/railway"
railway variables --set "STRIPE_SECRET_KEY=<your-stripe-secret-key>"
railway variables --set "STRIPE_PUBLIC_KEY=<your-stripe-public-key>"
railway variables --set "SECRET_KEY=QnPfcUzYOXUeP8MBGfkj3mHb4E0ir28t9wDKFpJ44"
```

### 4. Deploy (After upgrade)
```powershell
railway up
```

---

## Quick Summary:

**In terminal:**
1. `railway service c1c098de-0a47-4793-bb22-63f39117e70d`
2. Set variables (commands above)
3. `railway up` (will work after plan upgrade)

**In browser:**
1. Go to: https://railway.app/workspace/plans
2. Click "Deploy with Hobby" ($5/month)
3. Complete payment setup

**Then:** Run `railway up` again - it will deploy!

---

The browser should now show the upgrade page. Complete the upgrade, then run the commands above.

