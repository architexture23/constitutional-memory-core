# Truth Drop Platform - Update Environment Files with Stripe Keys
# Built from Remembrance | Operating under Format Law

Write-Host "============================================================"
Write-Host "UPDATE ENVIRONMENT FILES WITH STRIPE KEYS"
Write-Host "============================================================"
Write-Host ""

$backendEnvPath = "TRUTH_DROP_PLATFORM\backend\.env"
$frontendEnvPath = "TRUTH_DROP_PLATFORM\frontend\.env.local"

# Stripe Keys
$stripeSecretKey = "<your-stripe-secret-key>"
$stripePublicKey = "<your-stripe-public-key>"

# Update Backend .env
Write-Host "Updating backend .env file..."
if (Test-Path $backendEnvPath) {
    $backendEnv = Get-Content $backendEnvPath -Raw
    
    # Update or add STRIPE_SECRET_KEY
    if ($backendEnv -match "STRIPE_SECRET_KEY=") {
        $backendEnv = $backendEnv -replace "STRIPE_SECRET_KEY=.*", "STRIPE_SECRET_KEY=$stripeSecretKey"
    } else {
        $backendEnv += "`nSTRIPE_SECRET_KEY=$stripeSecretKey"
    }
    
    # Update or add STRIPE_PUBLIC_KEY
    if ($backendEnv -match "STRIPE_PUBLIC_KEY=") {
        $backendEnv = $backendEnv -replace "STRIPE_PUBLIC_KEY=.*", "STRIPE_PUBLIC_KEY=$stripePublicKey"
    } else {
        $backendEnv += "`nSTRIPE_PUBLIC_KEY=$stripePublicKey"
    }
    
    # Ensure FRONTEND_URL is set
    if ($backendEnv -notmatch "FRONTEND_URL=") {
        $backendEnv += "`nFRONTEND_URL=http://localhost:3000"
    }
    
    Set-Content -Path $backendEnvPath -Value $backendEnv -NoNewline
    Write-Host "✅ Backend .env updated!"
} else {
    Write-Host "⚠️  Backend .env file not found. Creating it..."
    $backendEnvContent = @"
DATABASE_URL=your_database_url_here
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

STRIPE_SECRET_KEY=$stripeSecretKey
STRIPE_PUBLIC_KEY=$stripePublicKey
STRIPE_WEBHOOK_SECRET=

FRONTEND_URL=http://localhost:3000

CORS_ORIGINS_STR=http://localhost:3000,http://localhost:8000
"@
    Set-Content -Path $backendEnvPath -Value $backendEnvContent
    Write-Host "✅ Backend .env created!"
}

Write-Host ""

# Update Frontend .env.local
Write-Host "Updating frontend .env.local file..."
if (Test-Path $frontendEnvPath) {
    $frontendEnv = Get-Content $frontendEnvPath -Raw
    
    # Update or add NEXT_PUBLIC_API_URL
    if ($frontendEnv -match "NEXT_PUBLIC_API_URL=") {
        $frontendEnv = $frontendEnv -replace "NEXT_PUBLIC_API_URL=.*", "NEXT_PUBLIC_API_URL=http://localhost:8000"
    } else {
        $frontendEnv += "`nNEXT_PUBLIC_API_URL=http://localhost:8000"
    }
    
    # Update or add NEXT_PUBLIC_STRIPE_PUBLIC_KEY
    if ($frontendEnv -match "NEXT_PUBLIC_STRIPE_PUBLIC_KEY=") {
        $frontendEnv = $frontendEnv -replace "NEXT_PUBLIC_STRIPE_PUBLIC_KEY=.*", "NEXT_PUBLIC_STRIPE_PUBLIC_KEY=$stripePublicKey"
    } else {
        $frontendEnv += "`nNEXT_PUBLIC_STRIPE_PUBLIC_KEY=$stripePublicKey"
    }
    
    Set-Content -Path $frontendEnvPath -Value $frontendEnv -NoNewline
    Write-Host "✅ Frontend .env.local updated!"
} else {
    Write-Host "⚠️  Frontend .env.local file not found. Creating it..."
    $frontendEnvContent = @"
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=$stripePublicKey
"@
    Set-Content -Path $frontendEnvPath -Value $frontendEnvContent
    Write-Host "✅ Frontend .env.local created!"
}

Write-Host ""
Write-Host "============================================================"
Write-Host "✅ Environment files updated with Stripe keys!"
Write-Host "============================================================"
Write-Host ""
Write-Host "Next Steps:"
Write-Host "1. Install Stripe CLI: https://stripe.com/docs/stripe-cli"
Write-Host "2. Run: stripe login"
Write-Host "3. Run: stripe listen --forward-to localhost:8000/api/stripe-webhook"
Write-Host "4. Copy the webhook secret (whsec_...) and add it to backend .env as STRIPE_WEBHOOK_SECRET"
Write-Host ""
Write-Host "See STRIPE_KEYS_SETUP.md for full instructions!"
Write-Host ""




