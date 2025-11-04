# Simple Railway Deployment Script
# Run this in the SAME terminal where you ran 'railway login'

Write-Host "`n=== Railway Deployment ===" -ForegroundColor Green
Write-Host ""

# Step 1: Link Project
Write-Host "Step 1: Linking project..." -ForegroundColor Cyan
railway link -p ce2ffc15-0e22-4b04-8632-27d70e72701b
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Could not link project" -ForegroundColor Red
    Write-Host "Make sure you ran 'railway login' first in this terminal!" -ForegroundColor Yellow
    exit
}
Write-Host "Project linked!" -ForegroundColor Green
Write-Host ""

# Step 2: Set Environment Variables
Write-Host "Step 2: Setting environment variables..." -ForegroundColor Cyan
railway variables --set "FRONTEND_URL=https://frontend-csd4ftpzk-architexture23s-projects.vercel.app"
railway variables --set "DATABASE_URL=postgresql://postgres:yBICuFzSKbAoeQBXxlULQEyeZgOTvEup@yamanote.proxy.rlwy.net:56573/railway"
railway variables --set "STRIPE_SECRET_KEY=<your-stripe-secret-key>"
railway variables --set "STRIPE_PUBLIC_KEY=<your-stripe-public-key>"
railway variables --set "SECRET_KEY=QnPfcUzYOXUeP8MBGfkj3mHb4E0ir28t9wDKFpJ44"
railway variables --set "HOST=0.0.0.0"
railway variables --set "PORT=8000"
railway variables --set "DEBUG=False"
Write-Host "Environment variables set!" -ForegroundColor Green
Write-Host ""

# Step 3: Deploy
Write-Host "Step 3: Deploying to Railway..." -ForegroundColor Cyan
Write-Host "This may take a few minutes..." -ForegroundColor Yellow
railway up
if ($LASTEXITCODE -ne 0) {
    Write-Host "Deployment may have failed - check Railway dashboard" -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "=== Deployment Complete! ===" -ForegroundColor Green
Write-Host "Check Railway dashboard for your backend URL!" -ForegroundColor Cyan
Write-Host ""

