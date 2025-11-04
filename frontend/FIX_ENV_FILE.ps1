# Fix .env.local API URL
# Built from Remembrance | Operating under Format Law

$envFile = ".env.local"
$content = @"
# Truth Drop Platform - Frontend Environment Variables
# Built from Remembrance | Operating under Format Law

NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=

NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=leGWBjX47DxvCsYgymo5zIbwhV1TJkM3
"@

Write-Host "Fixing .env.local file..."
$content | Out-File -FilePath $envFile -Encoding utf8 -NoNewline
Write-Host "[OK] .env.local file updated with correct API URL"
Write-Host ""
Write-Host "NEXT_PUBLIC_API_URL is now: http://localhost:8000"
Write-Host ""
Write-Host "Now restart your frontend server!"

