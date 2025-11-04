# 📧 Gmail SMTP Setup Instructions

## Quick Setup (5 minutes)

Your email is configured to use **rdtiptoe2@gmail.com**. To enable email sending, you need a Gmail App Password.

### Step 1: Enable 2-Step Verification

1. Go to https://myaccount.google.com/security
2. Enable "2-Step Verification" (required for App Passwords)

### Step 2: Generate App Password

1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and "Other (Custom name)"
3. Enter name: "Truth Drop Platform"
4. Click "Generate"
5. Copy the 16-character password (spaces will be removed automatically)

### Step 3: Add to .env File

Open `backend/.env` and add:

```
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=rdtiptoe2@gmail.com
SMTP_PASSWORD=your_16_character_app_password_here
EMAIL_SENDER=rdtiptoe2@gmail.com
EMAIL_SENDER_NAME=Truth Drop Platform
```

**Replace `your_16_character_app_password_here` with the password from Step 2**

### Step 4: Restart Backend

After adding the password, restart your backend:

```powershell
# Stop backend (Ctrl+C)
cd backend
python main.py
```

### Step 5: Test Email

Make a test purchase and check if email is sent!

---

## Alternative: SendGrid (Recommended for Production)

**Free Tier:** 100 emails/day

1. Sign up at https://sendgrid.com (free)
2. Get API key from dashboard
3. Add to `backend/.env`:
   ```
   SENDGRID_API_KEY=SG.your_api_key_here
   EMAIL_SENDER=noreply@truthdrop.com
   EMAIL_SENDER_NAME=Truth Drop Platform
   ```
4. Remove SMTP settings (SendGrid takes priority)

---

## No Email Setup? That's OK!

The system works **without email configuration**:
- Download links will be logged to console
- You can manually share download links with buyers
- All functionality works, just no automatic emails

---

**Your email: rdtiptoe2@gmail.com** ✅

