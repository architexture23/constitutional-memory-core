# Railway Deployment Script
# Run this AFTER railway login succeeds

Write-Host "=== Railway Deployment Script ===" -ForegroundColor Green
Write-Host ""

# Step 1: Link Project
Write-Host "Step 1: Linking Railway project..." -ForegroundColor Cyan
railway link -p ce2ffc15-0e22-4b04-8632-27d70e72701b
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to link project" -ForegroundColor Red
    Write-Host "Make sure you ran 'railway login' first in this terminal" -ForegroundColor Yellow
    exit 1
}
Write-Host "✅ Project linked!" -ForegroundColor Green
Write-Host ""

# Step 2: Set Environment Variables
Write-Host "Step 2: Setting environment variables..." -ForegroundColor Cyan

$envVars = @{
    "DATABASE_URL" = "postgresql://postgres:yBICuFzSKbAoeQBXxlULQEyeZgOTvEup@yamanote.proxy.rlwy.net:56573/railway"
    "FRONTEND_URL" = "https://frontend-csd4ftpzk-architexture23s-projects.vercel.app"
    "STRIPE_SECRET_KEY" = "<your-stripe-secret-key>"
    "STRIPE_PUBLIC_KEY" = "<your-stripe-public-key>"
    "SECRET_KEY" = "QnPfcUzYOXUeP8MBGfkj3mHb4E0ir28t9wDKFpJ44"
    "HOST" = "0.0.0.0"
    "PORT" = "8000"
    "DEBUG" = "False"
}

$setFlags = @()
foreach ($key in $envVars.Keys) {
    $value = $envVars[$key]
    $setFlags += "--set"
    $setFlags += "$key=$value"
    Write-Host "  Setting $key..." -ForegroundColor Gray
}

railway variables @setFlags
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Warning: Some variables may not have been set" -ForegroundColor Yellow
    Write-Host "You can set them manually via Railway web dashboard" -ForegroundColor Yellow
}
Write-Host "✅ Environment variables set!" -ForegroundColor Green
Write-Host ""

# Step 3: Deploy
Write-Host "Step 3: Deploying to Railway..." -ForegroundColor Cyan
railway up
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Deployment failed" -ForegroundColor Red
    exit 1
}
Write-Host ""
Write-Host "=== Deployment Complete! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Check Railway dashboard for deployment URL" -ForegroundColor White
Write-Host "2. Update Vercel environment variable NEXT_PUBLIC_API_URL with Railway URL" -ForegroundColor White
Write-Host "3. Test the full flow!" -ForegroundColor White

