# Deployment Quick Reference

**Last Updated:** 2025-11-03

## 🚀 Quick Deploy Commands

### Backend (Railway):
```powershell
cd TRUTH_DROP_PLATFORM\backend
railway service c1c098de-0a47-4793-bb22-63f39117e70d
railway up
```

### Frontend (Vercel):
```powershell
cd TRUTH_DROP_PLATFORM\frontend
vercel --prod --yes
```

## 🔑 Authentication

### Railway:
- Token: `ad1e4414-15a0-4771-a952-4e479e4004cf`
- Or: `railway login` (interactive)

### Vercel:
- Token: `I9OlHOgMOfHk3XMkn9uRropD`
- Or: `vercel login` (interactive)

## 🌐 URLs

- **Frontend:** https://frontend-three-snowy-298am3ddwj.vercel.app
- **Backend:** https://resplendent-transformation-production.up.railway.app

## 🔧 Common Fixes

### CORS Issues:
1. Railway Dashboard → Variables → `CORS_ORIGINS`
2. Edit to include frontend URL
3. Click "Deploy" button

### Environment Variable Updates:
1. Update in Railway/Vercel dashboard
2. Trigger redeployment (required for changes to take effect)

---

**For full details, see `PROJECT_CLARITY_v1.0.md`**

