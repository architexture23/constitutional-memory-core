# 🧪 TEST OPTIONS - Choose Your Test Method

## ✅ Option 1: Full Stripe Test Card (Recommended)

**Complete Test Card Info:**

```
Card Number: 4242 4242 4242 4242
Expiry Date: 12/25 (or any future date like 01/26, 06/27, etc.)
CVC: 123 (or any 3 digits)
ZIP Code: 12345 (or any 5 digits)
Cardholder Name: Test User (or anything)
```

**This card always succeeds in Stripe test mode!**

**Steps:**
1. Go to http://localhost:3000
2. Click any codex with a price (e.g., "Constitutional Trading Framework")
3. Click "Purchase Now"
4. Enter the test card info above
5. Complete checkout
6. Check backend logs for download link
7. Test download!

---

## ✅ Option 2: Free Codex (No Payment Needed)

**I've created a FREE test codex for you!**

**Free Codex URL:**
```
http://localhost:3000/codexes/free-test-codex
```

**OR find it by:**
1. Go to http://localhost:3000
2. Look for "Free Test Codex - Constitutional Framework v1.0"
3. Click it
4. Click "Get Free" (or "Purchase Now" - it's free!)
5. No payment required!
6. Check backend logs for download link

---

## 🎯 Which Should You Use?

### Use Stripe Test Card If:
- ✅ You want to test the full payment flow
- ✅ You want to see Stripe Checkout
- ✅ You want to test the complete purchase experience

### Use Free Codex If:
- ✅ You want to test without entering card info
- ✅ You want to test fulfillment quickly
- ✅ You want to verify download links work

---

## 📋 Test Flow:

**With Test Card:**
1. Purchase → Stripe Checkout → Enter test card → Complete → Webhook → Download link

**With Free Codex:**
1. Get Free Codex → Webhook → Download link (no payment needed)

**Both work! Choose whichever you prefer!**

---

## 🧪 What to Check After Purchase:

**Backend Console Should Show:**
```
[Webhook] Purchase created: ID X, Codex Y
[Webhook] Download URL: http://localhost:3000/download/abc123...
[Email Service] No email service configured. Would send to email@example.com
[Email Service] Download URL: http://localhost:3000/download/abc123...
```

**Copy the download URL and visit it in your browser!**

---

**See `STRIPE_TEST_CARDS.md` for more test card options!**

