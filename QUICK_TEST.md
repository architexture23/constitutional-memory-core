# 🧪 QUICK TEST GUIDE

## ✅ TWO WAYS TO TEST:

---

## 🎯 OPTION 1: FREE CODEX (Easiest - No Payment)

**Just click and get!**

1. **Go to**: http://localhost:3000/codexes/free-test-codex
   
   **OR** browse to it:
   - Go to http://localhost:3000
   - Find "Free Test Codex - Constitutional Framework v1.0"
   - Click it

2. **Click the green "Get Free" button**

3. **You'll be redirected to download page immediately!**
   - No Stripe checkout
   - No payment needed
   - Instant download access

4. **Click "Download Now"** → File downloads! ✅

**That's it!** Quickest way to test the full flow.

---

## 🎯 OPTION 2: TEST CARD (Full Payment Flow)

**Complete Stripe test card info:**

```
Card Number: 4242 4242 4242 4242
Expiry Date: 12/25 (or any future date)
CVC: 123 (or any 3 digits)
ZIP Code: 12345 (or any 5 digits)
Cardholder Name: Test User (or anything)
```

**Steps:**
1. Go to http://localhost:3000
2. Click any codex with a price (e.g., "Constitutional Trading Framework")
3. Click "Purchase Now"
4. Enter the test card info above
5. Complete checkout
6. Check backend console for download link
7. Visit download link → Download! ✅

---

## 📋 What to Check:

### Backend Console Should Show:
```
[Webhook] Purchase created: ID X, Codex Y
[Webhook] Download URL: http://localhost:3000/download/abc123...
```

**For free codex**, you'll see it in the console immediately:
```
[Create Checkout Session] Free codex purchase created
Download URL: http://localhost:3000/download/abc123...
```

### Then:
1. Copy the download URL from console
2. Visit it in your browser
3. See download page
4. Click "Download Now"
5. File downloads! ✅

---

## 🚀 Ready to Test!

**Choose your option:**
- ✅ **Free Codex**: Easiest, no payment (recommended for quick test)
- ✅ **Test Card**: Full payment flow test

**Both work perfectly!**

---

**See `STRIPE_TEST_CARDS.md` for more test card options!**

