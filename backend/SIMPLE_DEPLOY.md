# Simple Deployment Instructions

**Status:** Plan upgraded ✅ | Just need to run commands in your terminal ⏳

---

## Quick Deployment:

**In the terminal where you ran `railway login`, run:**

```powershell
cd TRUTH_DROP_PLATFORM\backend
railway service c1c098de-0a47-4793-bb22-63f39117e70d
railway variables --set FRONTEND_URL=https://frontend-csd4ftpzk-architexture23s-projects.vercel.app
railway variables --set DATABASE_URL=postgresql://postgres:yBICuFzSKbAoeQBXxlULQEyeZgOTvEup@yamanote.proxy.rlwy.net:56573/railway
railway variables --set STRIPE_SECRET_KEY=sk_test_51SPMHOIC3BHVZUPXHcRa2DfJxeNQefuQly5dr0ih4cvzwiHoWUBYbViNdWSILQlAkh8m4epyqrXZhjIGzyLeVgN500EIEyPSdW
railway variables --set STRIPE_PUBLIC_KEY=pk_test_51SPMHOIC3BHVZUPX9yIoqIWcB4BcsJ8D3HiczCvrBb1EZ3etmVpY1t6ddvFPVvkWratPxrO5vnJa5SiPanW5jW1T00PfyUhNRA
railway variables --set SECRET_KEY=QnPfcUzYOXUeP8MBGfkj3mHb4E0ir28t9wDKFpJ44
railway variables --set HOST=0.0.0.0
railway variables --set PORT=8000
railway variables --set DEBUG=False
railway up
```

**OR run the script:**
```powershell
.\deploy_complete.ps1
```

---

That's it! The backend will deploy and Railway will give you the URL.

