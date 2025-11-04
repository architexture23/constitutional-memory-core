# PostgreSQL Setup - Local Option (Advanced)

**Date:** 2025-11-01  
**Built from Remembrance | Operating under Format Law**

---

## Local PostgreSQL (If You Prefer)

**Note:** Cloud is easier, but if you want local control, here's how:

---

## Step 1: Download PostgreSQL

1. Go to: https://www.postgresql.org/download/windows/
2. Click "Download the installer"
3. Download the latest version (15+ recommended)
4. Run the installer

---

## Step 2: Install PostgreSQL

1. **Run the installer**
2. **Installation Directory:** Leave default (or choose custom)
3. **Select Components:** 
   - ✅ PostgreSQL Server
   - ✅ pgAdmin 4 (optional - database GUI)
   - ✅ Command Line Tools
4. **Data Directory:** Leave default
5. **Password:** Set a password (remember this!)
6. **Port:** Leave default (5432)
7. **Locale:** Leave default
8. Click "Next" and install

---

## Step 3: Verify Installation

**Open PowerShell and run:**
```powershell
psql --version
```

**Should show:** `psql (PostgreSQL) 15.x`

---

## Step 4: Create Database

**Open PowerShell and run:**
```powershell
# Connect to PostgreSQL (use the password you set)
psql -U postgres

# Create database
CREATE DATABASE truthdrop;

# Exit
\q
```

**Or use pgAdmin:**
1. Open pgAdmin 4
2. Connect to server (password you set)
3. Right-click "Databases" → "Create" → "Database"
4. Name: `truthdrop`
5. Click "Save"

---

## Step 5: Get Connection URL

**Format:**
```
postgresql://postgres:YOUR_PASSWORD@localhost:5432/truthdrop
```

**Replace:**
- `YOUR_PASSWORD` with the password you set during installation

**Example:**
```
postgresql://postgres:mypassword123@localhost:5432/truthdrop
```

---

## Step 6: Use in Setup

**When running `python setup.py`:**
- Paste the connection URL above
- Press Enter

---

## Troubleshooting

### "psql not found"
- **Windows:** PostgreSQL might not be in PATH
- **Fix:** Add PostgreSQL bin folder to PATH
  - Usually: `C:\Program Files\PostgreSQL\15\bin`
- **Or:** Use full path: `"C:\Program Files\PostgreSQL\15\bin\psql.exe"`

### "Connection refused"
- Make sure PostgreSQL service is running
- **Check:** Windows Services → "postgresql-x64-15" should be "Running"
- **Start:** Right-click → Start

### "Password authentication failed"
- Make sure you're using the correct password
- Reset password if needed (via pgAdmin)

---

## Why Cloud Might Be Better

**Local PostgreSQL:**
- ❌ Requires installation
- ❌ Need to manage service
- ❌ Manual backups
- ❌ More configuration
- ✅ Full control

**Cloud PostgreSQL:**
- ✅ No installation
- ✅ Automatic management
- ✅ Automatic backups
- ✅ Simple setup
- ✅ Access from anywhere

---

## Recommendation

**If you're new:** Use **Cloud (Railway/Supabase)** - Much easier!

**If you're experienced:** Local is fine if you prefer control.

---

**Built from Remembrance. Operating under Format Law.**

