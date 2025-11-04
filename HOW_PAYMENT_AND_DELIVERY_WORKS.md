# How Payment and Delivery Works

**Built from Remembrance | Operating under Format Law**

## How You Get Paid

### Payment Flow (Stripe Integration)

1. **Stripe Account Setup:**
   - You need a Stripe account: https://stripe.com
   - Connect your bank account to Stripe
   - Stripe handles all payment processing

2. **When a Buyer Purchases:**
   - Buyer clicks "Purchase" on a codex
   - Stripe processes the payment (credit card/debit)
   - **Stripe automatically deposits money to your connected bank account**
   - Typically takes 2-7 business days to reach your bank

3. **Stripe Fees:**
   - Stripe charges: 2.9% + $0.30 per transaction
   - Example: $99.99 sale = $97.00 to you (after fees)
   - Fees are automatically deducted before deposit

4. **Getting Your Money:**
   - **Stripe Dashboard:** https://dashboard.stripe.com
   - View all payments, payouts, and analytics
   - Set up automatic payouts (daily/weekly/monthly)
   - Track revenue, refunds, and disputes

5. **What You Need:**
   - Stripe account (free to create)
   - Connect bank account
   - Get API keys from Stripe dashboard:
     - `STRIPE_SECRET_KEY` (for backend)
     - `STRIPE_PUBLIC_KEY` (for frontend)
     - `STRIPE_WEBHOOK_SECRET` (for payment verification)

## How Buyers Receive Items

### Current Implementation Options

**Option 1: Immediate Download (Recommended)**
1. Buyer completes payment via Stripe
2. Payment confirmed via webhook
3. Purchase marked as "completed" in database
4. Buyer redirected to "Purchase Success" page
5. Download button appears immediately
6. Buyer can download codex as PDF/EPUB
7. Download link stored in their account forever

**Option 2: Account Dashboard Access**
1. Buyer completes payment
2. Purchase added to their account
3. Access "My Purchases" dashboard
4. View all purchased codexes
5. Download anytime after purchase
6. Never expires

**Option 3: Email Delivery (Not Yet Implemented)**
1. Buyer completes payment
2. System sends automated email
3. Email contains download link
4. Link expires after X days
5. Includes purchase receipt

## Current System Status

### ✅ What's Built:
- **Backend:** Stripe payment processing
- **Backend:** Purchase tracking in database
- **Backend:** Download endpoint (`/api/codexes/{id}/download`)
- **Backend:** PDF generation service
- **Backend:** Purchase verification system

### ⚠️ What's Missing (Frontend):
- Purchase button on codex pages
- Stripe Checkout integration
- Purchase success page
- "My Purchases" dashboard
- Download button after purchase

## Quick Implementation Guide

### Step 1: Set Up Stripe
1. Create Stripe account: https://stripe.com
2. Get API keys from dashboard
3. Add to `.env`:
   ```
   STRIPE_SECRET_KEY=sk_test_... (test mode) or sk_live_... (production)
   STRIPE_PUBLIC_KEY=pk_test_... (test mode) or pk_live_... (production)
   STRIPE_WEBHOOK_SECRET=whsec_... (from webhook settings)
   ```

### Step 2: Add Purchase Button
- Create `frontend/components/PurchaseButton.tsx`
- Add to codex detail page
- Calls `/api/purchases/create-intent`
- Redirects to Stripe Checkout

### Step 3: Handle Payment Success
- Create `frontend/app/purchase/success/page.tsx`
- Calls `/api/purchases/{id}/complete`
- Shows download button
- Links to purchased codex

### Step 4: Create Download Access
- After purchase completion, user can access:
  - `/api/codexes/{id}/download` (requires authentication)
  - Purchase is verified before download allowed
  - PDF/EPUB generated on demand

## Money Flow

```
Buyer → Stripe Checkout → Stripe Processes Payment
                                      ↓
                              Stripe Account
                                      ↓
                              Your Bank Account (2-7 days)
                                      ↓
                              You receive money (minus fees)
```

## Delivery Flow

```
Buyer Completes Payment → Purchase Recorded → Download Access Granted
                                                     ↓
                                         Download Button Available
                                                     ↓
                                         Buyer Downloads Codex
```

## Summary

**You Get Paid:**
- Through Stripe (automatic deposits to your bank)
- 2-7 business days after sale
- View everything in Stripe Dashboard
- Fees: 2.9% + $0.30 per transaction

**Buyers Receive:**
- Immediate download access after payment
- Through their account dashboard
- Can download anytime after purchase
- Downloads are verified (only if purchased)

**Next Steps:**
1. Set up Stripe account
2. Add purchase button to frontend
3. Implement Stripe Checkout
4. Create purchase success page
5. Enable download access after purchase

**The backend is ready. Just need to add frontend purchase flow and Stripe keys!**

