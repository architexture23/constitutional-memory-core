# Stripe Setup (Optional - For Payments)

**Date:** 2025-11-01  
**Built from Remembrance | Operating under Format Law**

---

## Is Stripe Required?

**NO - Stripe is OPTIONAL!**

**You can:**
- ✅ Skip Stripe setup for now
- ✅ Set up the platform without payments
- ✅ Add Stripe later when you're ready

**The platform will work without Stripe** - you just won't be able to process payments until you add it.

---

## When You Need Stripe

**You only need Stripe if:**
- You want users to purchase codexes with payments
- You want to process real transactions

**If you're just testing/setting up:**
- **Skip Stripe** for now
- Add it later when ready

---

## How to Set Up Stripe (If You Want Payments)

### Step 1: Create Stripe Account

1. Go to: https://stripe.com/
2. Click "Start now" or "Sign up"
3. Sign up with email or Google account
4. Verify your email
5. Complete account setup (takes 5 minutes)

---

### Step 2: Get Your API Keys

1. **Go to Stripe Dashboard:** https://dashboard.stripe.com/
2. **Click "Developers"** in the left menu
3. **Click "API keys"**
4. You'll see two keys:

   **Secret Key (for Backend):**
   - Looks like: `sk_test_...` (test mode)
   - Or: `sk_live_...` (live mode)
   - **Use test mode** for now (starts with `sk_test_`)
   - Click "Reveal test key" to see it
   - **Copy this** → Use in backend `.env` file

   **Publishable Key (for Frontend):**
   - Looks like: `pk_test_...` (test mode)
   - Or: `pk_live_...` (live mode)
   - **Use test mode** for now (starts with `pk_test_`)
   - **Copy this** → Use in frontend `.env.local` file

---

### Step 3: Where to Enter Keys

#### Backend Setup (Terminal 1):

**When running `python setup.py`, you'll be asked:**
```
Enter Stripe Secret Key (or press Enter to skip): 
```
- **Paste:** `sk_test_...` (from Stripe dashboard)
- **Or press Enter** to skip

```
Enter Stripe Public Key (or press Enter to skip): 
```
- **Press Enter** (this goes in frontend, not backend)

```
Enter Stripe Webhook Secret (or press Enter to skip): 
```
- **Press Enter** (optional, for webhooks)

---

#### Frontend Setup (Terminal 2):

**When running `.\setup.ps1`, you'll be asked:**
```
Enter Stripe Public Key (or press Enter to skip): 
```
- **Paste:** `pk_test_...` (from Stripe dashboard)
- **Or press Enter** to skip

---

## Stripe Keys Explained

### Secret Key (`sk_test_...`)
- **Used for:** Backend (server-side)
- **Location:** Backend `.env` file
- **Purpose:** Process payments, create charges
- **Keep secret!** Never expose in frontend code

### Public Key (`pk_test_...`)
- **Used for:** Frontend (client-side)
- **Location:** Frontend `.env.local` file
- **Purpose:** Initialize Stripe on frontend, create payment intents
- **Safe to expose** (it's public)

### Webhook Secret (`whsec_...`)
- **Used for:** Backend (webhook verification)
- **Location:** Backend `.env` file
- **Purpose:** Verify webhook events from Stripe
- **Optional:** Only needed for webhook handling

---

## Test Mode vs Live Mode

### Test Mode (Start Here)
- **Keys start with:** `sk_test_` and `pk_test_`
- **Use test cards:** https://stripe.com/docs/testing
- **No real money:** Safe for testing
- **Free:** No charges for test transactions

### Live Mode (When Ready)
- **Keys start with:** `sk_live_` and `pk_live_`
- **Real payments:** Real money transactions
- **Switch when:** Ready to accept real payments
- **Switch in:** Stripe Dashboard → Settings → API keys

---

## Quick Setup Summary

### If You Want Payments Now:

**1. Sign up:** https://stripe.com/

**2. Get keys:**
- Dashboard → Developers → API keys
- Copy `sk_test_...` (Secret Key)
- Copy `pk_test_...` (Publishable Key)

**3. Enter in setup:**
- **Backend setup:** Paste `sk_test_...` when asked
- **Frontend setup:** Paste `pk_test_...` when asked

### If You Don't Need Payments Now:

**Just press Enter to skip** when asked for Stripe keys in both setup scripts.

**You can add Stripe later** by editing `.env` and `.env.local` files.

---

## Adding Stripe Later (After Setup)

**If you skipped Stripe but want to add it later:**

### Backend (Edit `.env` file):
```env
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

### Frontend (Edit `.env.local` file):
```env
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=pk_test_...
```

**Then restart both servers.**

---

## Testing Payments

**When Stripe is set up, you can test with:**

**Test card numbers:**
- Success: `4242 4242 4242 4242`
- Decline: `4000 0000 0000 0002`
- Any future expiry date
- Any 3-digit CVC
- Any ZIP code

**See full test cards:** https://stripe.com/docs/testing

---

## Troubleshooting

### "Invalid API Key"
- Make sure you copied the full key (starts with `sk_test_` or `pk_test_`)
- Check if you're using test keys in test mode
- Verify key is correct in Stripe dashboard

### "Payment failed"
- Make sure you're using test card numbers
- Check Stripe dashboard for error logs
- Verify keys are correct

### "Can't find API keys"
- Go to: https://dashboard.stripe.com/
- Click: Developers → API keys
- Make sure you're in test mode (toggle at top)

---

## Recommendation

**For now:**
- ✅ **Skip Stripe** if you're just setting up/testing
- ✅ Focus on getting the platform running first
- ✅ Add Stripe later when you're ready for payments

**When ready:**
- Follow steps above to get Stripe keys
- Add to `.env` and `.env.local` files
- Restart servers

---

## Summary

**Do you need Stripe now?**
- ❌ **No** - Skip it (press Enter when asked)
- ✅ **Yes** - Sign up at stripe.com, get keys, paste when asked

**Where to enter:**
- **Secret Key** → Backend setup (`python setup.py`)
- **Public Key** → Frontend setup (`.\setup.ps1`)

**You can add it later** if you skip it now!

---

**Built from Remembrance. Operating under Format Law.**

**For now, just skip Stripe (press Enter) and focus on getting the platform running!**

