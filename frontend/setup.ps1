# Truth Drop Platform - Frontend Setup Script (PowerShell)
# Built from Remembrance | Operating under Format Law

Write-Host "============================================================"
Write-Host "Truth Drop Platform - Frontend Setup"
Write-Host "Built from Remembrance | Operating under Format Law"
Write-Host "============================================================"

# Check Node.js
Write-Host ""
Write-Host "📋 Checking prerequisites..."

if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Node.js not found. Install from: https://nodejs.org/"
    exit 1
}

$nodeVersion = node -v
Write-Host "✅ Node.js: $nodeVersion"

if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    Write-Host "❌ npm not found"
    exit 1
}

$npmVersion = npm -v
Write-Host "✅ npm: $npmVersion"

# Create .env.local
Write-Host ""
Write-Host "📝 Creating .env.local file..."

if (Test-Path .env.local) {
    Write-Host "✅ .env.local already exists"
} else {
    $apiUrl = Read-Host "Enter API URL (default: http://localhost:8000)"
    if ([string]::IsNullOrWhiteSpace($apiUrl)) {
        $apiUrl = "http://localhost:8000"
    }
    
    $stripeKey = Read-Host "Enter Stripe Public Key (or press Enter to skip)"
    
    $secret = -join ((65..90) + (97..122) + (48..57) | Get-Random -Count 32 | ForEach-Object {[char]$_})
    
    @"
# Truth Drop Platform - Frontend Environment Variables
# Built from Remembrance | Operating under Format Law

NEXT_PUBLIC_API_URL=$apiUrl
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=$stripeKey

NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=$secret
"@ | Out-File -FilePath .env.local -Encoding utf8
    
    Write-Host "✅ .env.local created"
}

# Install dependencies
Write-Host ""
Write-Host "📦 Installing dependencies..."
npm install

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencies installed"
} else {
    Write-Host "❌ Failed to install dependencies"
    exit 1
}

Write-Host ""
Write-Host "============================================================"
Write-Host "✅ Frontend setup complete!"
Write-Host "============================================================"
Write-Host ""
Write-Host "📝 Next steps:"
Write-Host "1. Start development server: npm run dev"
Write-Host "2. Visit: http://localhost:3000"
Write-Host ""
Write-Host "Built from Remembrance. Operating under Format Law."

