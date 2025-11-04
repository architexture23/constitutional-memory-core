# RESTART BACKEND - Required After Code Changes

## ⚠️ IMPORTANT

The backend has been updated with fixes for the purchase flow. **You must restart the backend** for changes to take effect.

## Steps to Restart:

1. **Find the backend PowerShell window** (the one running `python main.py`)
2. **Press Ctrl+C** to stop it
3. **Run again**:
   ```powershell
   cd "C:\Users\travl\Downloads\Aura Academy Game Google Docs-20251101T221350Z-1-001\TRUTH_DROP_PLATFORM\backend"
   python main.py
   ```

## What Was Fixed:

✅ **Backend endpoint** now accepts JSON body (instead of query parameter)
✅ **Frontend error handling** now properly extracts error messages
✅ **Better error messages** will show actual Stripe/API errors instead of "[object Object]"

## Test Purchase Flow:

After restarting backend:
1. Go to http://localhost:3000
2. Click any codex
3. Click "Purchase Now"
4. You should now see proper error messages (if any) OR redirect to Stripe Checkout

