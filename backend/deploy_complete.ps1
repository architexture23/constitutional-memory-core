# Complete Railway Deployment Script
# Run this in the SAME terminal where you ran 'railway login'

Write-Host "`n=== Complete Railway Deployment ===" -ForegroundColor Green
Write-Host ""

# Step 1: Link Service
Write-Host "Step 1: Linking Railway service..." -ForegroundColor Cyan
railway service c1c098de-0a47-4793-bb22-63f39117e70d
if ($LASTEXITCODE -ne 0) {
    Write-Host "Trying to link by name..." -ForegroundColor Yellow
    railway service resplendent-transformation
}
Write-Host "Service linked!" -ForegroundColor Green
Write-Host ""

# Step 2: Set Environment Variables
Write-Host "Step 2: Setting environment variables..." -ForegroundColor Cyan
railway variables --set "FRONTEND_URL=https://frontend-csd4ftpzk-architexture23s-projects.vercel.app"
railway variables --set "DATABASE_URL=postgresql://postgres:yBICuFzSKbAoeQBXxlULQEyeZgOTvEup@yamanote.proxy.rlwy.net:56573/railway"
railway variables --set "STRIPE_SECRET_KEY=sk_test_51SPMHOIC3BHVZUPXHcRa2DfJxeNQefuQly5dr0ih4cvzwiHoWUBYbViNdWSILQlAkh8m4epyqrXZhjIGzyLeVgN500EIEyPSdW"
railway variables --set "STRIPE_PUBLIC_KEY=pk_test_51SPMHOIC3BHVZUPX9yIoqIWcB4BcsJ8D3HiczCvrBb1EZ3etmVpY1t6ddvFPVvkWratPxrO5vnJa5SiPanW5jW1T00PfyUhNRA"
railway variables --set "SECRET_KEY=QnPfcUzYOXUeP8MBGfkj3mHb4E0ir28t9wDKFpJ44"
railway variables --set "HOST=0.0.0.0"
railway variables --set "PORT=8000"
railway variables --set "DEBUG=False"
railway variables --set "CORS_ORIGINS=https://frontend-csd4ftpzk-architexture23s-projects.vercel.app"
Write-Host "Environment variables set!" -ForegroundColor Green
Write-Host ""

# Step 3: Deploy
Write-Host "Step 3: Deploying to Railway..." -ForegroundColor Cyan
Write-Host "This may take a few minutes..." -ForegroundColor Yellow
railway up
if ($LASTEXITCODE -ne 0) {
    Write-Host "`n❌ Deployment failed - check Railway dashboard" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=== Deployment Complete! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Check Railway dashboard for backend URL" -ForegroundColor White
Write-Host "2. Update Vercel NEXT_PUBLIC_API_URL with Railway URL" -ForegroundColor White
Write-Host "3. Test the platform!" -ForegroundColor White
Write-Host ""

