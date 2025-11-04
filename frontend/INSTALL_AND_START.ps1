# Truth Drop Platform - Complete Frontend Setup & Start
# Built from Remembrance | Operating under Format Law

Write-Host "============================================================"
Write-Host "Truth Drop Platform - Frontend Setup & Start"
Write-Host "Built from Remembrance | Operating under Format Law"
Write-Host "============================================================"
Write-Host ""

# Check Node.js
if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "[ERROR] Node.js not found. Install from: https://nodejs.org/"
    exit 1
}

$nodeVersion = node -v
Write-Host "[OK] Node.js: $nodeVersion"

# Check npm
if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    Write-Host "[ERROR] npm not found"
    exit 1
}

$npmVersion = npm -v
Write-Host "[OK] npm: $npmVersion"

# Check/create .env.local
Write-Host ""
Write-Host "Checking .env.local..."

if (Test-Path ".env.local") {
    Write-Host "[OK] .env.local exists"
} else {
    Write-Host "Creating .env.local..."
    @"
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=$(New-Guid)
"@ | Out-File -FilePath ".env.local" -Encoding utf8
    Write-Host "[OK] .env.local created"
}

# Install dependencies
Write-Host ""
Write-Host "Installing dependencies (this may take 1-2 minutes)..."
npm install --legacy-peer-deps

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] npm install failed"
    Write-Host "Trying again with --force..."
    npm install --force
}

# Verify Next.js installed
Write-Host ""
Write-Host "Verifying installation..."
if (Test-Path "node_modules\next") {
    Write-Host "[OK] Next.js installed"
} else {
    Write-Host "[ERROR] Next.js not found - installing directly..."
    npm install next react react-dom --save
}

Write-Host ""
Write-Host "============================================================"
Write-Host "[OK] Frontend setup complete!"
Write-Host "============================================================"
Write-Host ""
Write-Host "Starting development server..."
Write-Host ""
Write-Host "Frontend will run on: http://localhost:3000"
Write-Host "Press CTRL+C to stop"
Write-Host ""

# Start dev server
npm run dev

