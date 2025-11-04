# Stripe Setup Guide - Business Information

**Built from Remembrance | Operating under Format Law**

## Business Name for Stripe

### Recommended Options:

**Option 1: "Truth Drop Platform"** (Recommended)
- Matches your platform name
- Professional and clear
- Easy for customers to recognize

**Option 2: "Constitutional Knowledge Platform"**
- Descriptive of what you sell
- Professional

**Option 3: "Truth Drop"**
- Shorter, simpler
- Still recognizable

**Option 4: Your Personal/Company Name**
- Use your legal business name
- If you have LLC/Corporation, use that

### What Stripe Uses It For:
- Customer billing statements
- Email receipts
- Customer support
- Legal/tax purposes

**Recommendation:** Use **"Truth Drop Platform"** - it matches your brand and is professional.

## Business Website - Do You Need It Now?

### Short Answer: **No, you can add it later**

### What Stripe Asks For:
1. **Business Name** (required)
2. **Business Type** (Individual/Sole Proprietor, LLC, Corporation, etc.)
3. **Business Website** (can be added later)
4. **Business Address** (required)
5. **Tax ID/SSN** (required for tax reporting)
6. **Bank Account** (required for payouts)

### Website Options:

**If You Have a Domain:**
- Add it now: e.g., `https://truthdrop.com`
- Better for customer trust
- Shows professionalism

**If You Don't Have a Domain Yet:**
- **Use: `http://localhost:3000` for testing** (Stripe Test Mode)
- **For production:** Add real domain when you get one
- You can update Stripe settings anytime

**Stripe Requirements:**
- Website URL is **not required** for account activation
- You can start in **Test Mode** without a website
- **Live Mode** may require website for some business types

### For Testing (Now):
1. Create Stripe account
2. Use "Truth Drop Platform" as business name
3. Website: Can skip or use `http://localhost:3000` temporarily
4. Add real domain later when ready

### For Production (Later):
1. Get domain: e.g., `truthdrop.com` or `truthdropplatform.com`
2. Update Stripe dashboard settings
3. Update website URL in Stripe
4. Switch to Live Mode

## Step-by-Step Stripe Setup

### 1. Create Account
- Go to: https://stripe.com
- Click "Start now"
- Use email and create password

### 2. Business Information
- **Business Name:** "Truth Drop Platform"
- **Business Type:** 
  - Individual/Sole Proprietor (if just you)
  - LLC (if you have one)
  - Corporation (if incorporated)
- **Website:** 
  - Testing: `http://localhost:3000` or skip
  - Production: Add real domain later

### 3. Get API Keys
- **Test Mode Keys** (for development):
  - Go to: https://dashboard.stripe.com/test/apikeys
  - Copy `Secret key` → `STRIPE_SECRET_KEY`
  - Copy `Publishable key` → `STRIPE_PUBLIC_KEY`

### 4. Set Up Webhook (For Payment Confirmation)
- Go to: https://dashboard.stripe.com/test/webhooks
- Add endpoint: `http://your-domain.com/api/stripe/webhook`
- Copy webhook secret → `STRIPE_WEBHOOK_SECRET`
- **For now:** Can set up later when you have domain

### 5. Connect Bank Account
- Required for payouts
- Stripe will verify your bank account
- Takes 1-2 business days

## What You Can Do Right Now (Test Mode)

**Complete Setup:**
- ✅ Business name: "Truth Drop Platform"
- ✅ Test Mode API keys (start here)
- ✅ Test bank account (use test account number)
- ⚠️ Website: Skip or use localhost (you can add later)
- ⚠️ Webhook: Set up when you have production domain

**Test Mode Features:**
- Use test credit cards (4242 4242 4242 4242)
- No real money transactions
- Test full payment flow
- All API keys work for testing

## When to Switch to Live Mode

**Requirements:**
1. Real domain name (website URL)
2. Business verification complete
3. Bank account connected
4. All business information verified

**Recommendation:**
- Start in **Test Mode** now
- Build and test payment flow
- Switch to **Live Mode** when ready to accept real payments

## Summary

**Business Name:** Use **"Truth Drop Platform"**

**Website:**
- **Now (Testing):** Skip or use `http://localhost:3000`
- **Later (Production):** Add real domain when you get one
- **You can update Stripe settings anytime**

**Next Steps:**
1. Create Stripe account
2. Use "Truth Drop Platform" as business name
3. Get Test Mode API keys
4. Add to `.env` file
5. Test payment flow
6. Add real domain when ready for production

**You don't need to wait for a website - you can start testing now!**

