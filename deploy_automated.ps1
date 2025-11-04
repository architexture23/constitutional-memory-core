# Automated Deployment Script for Truth Drop Platform (PowerShell)
# This script automates deployment to Railway (backend) and Vercel (frontend)

Write-Host "=== Truth Drop Platform - Automated Deployment ===" -ForegroundColor Green
Write-Host ""

# Check if Railway CLI is installed
function Check-Railway {
    try {
        $null = railway --version 2>$null
        Write-Host "✅ Railway CLI installed" -ForegroundColor Green
        return $true
    } catch {
        Write-Host "❌ Railway CLI not found" -ForegroundColor Red
        Write-Host "Install with: npm install -g @railway/cli" -ForegroundColor Yellow
        return $false
    }
}

# Check if Vercel CLI is installed
function Check-Vercel {
    try {
        $null = vercel --version 2>$null
        Write-Host "✅ Vercel CLI installed" -ForegroundColor Green
        return $true
    } catch {
        Write-Host "❌ Vercel CLI not found" -ForegroundColor Red
        Write-Host "Install with: npm install -g vercel" -ForegroundColor Yellow
        return $false
    }
}

# Deploy backend to Railway
function Deploy-Backend {
    Write-Host ""
    Write-Host "=== Deploying Backend to Railway ===" -ForegroundColor Cyan
    Set-Location backend
    
    # Set Railway token from saved token file
    $railwayTokenFile = "..\RAILWAY_TOKEN_SAVED.md"
    if (Test-Path $railwayTokenFile) {
        $tokenContent = Get-Content $railwayTokenFile -Raw
        if ($tokenContent -match 'Token ID:.*`([^`]+)`') {
            $env:RAILWAY_TOKEN = $matches[1]
            Write-Host "Railway token loaded from file" -ForegroundColor Green
        }
    } else {
        # Fallback to hardcoded token if file not found
        $env:RAILWAY_TOKEN = "ad1e4414-15a0-4771-a952-4e479e4004cf"
        Write-Host "Using Railway token" -ForegroundColor Yellow
    }
    
    try {
        railway whoami 2>&1 | Out-Null
        Write-Host "Logged in to Railway" -ForegroundColor Green
        
        # Check if project is linked
        $projectLinked = $false
        if (Test-Path ".railway" -PathType Container) {
            $projectLinked = $true
            Write-Host "Project already linked" -ForegroundColor Green
        } else {
            Write-Host "Linking or creating Railway project..." -ForegroundColor Yellow
            # Try to link existing project (non-interactive)
            railway link 2>&1 | Out-Null
            if ($LASTEXITCODE -eq 0 -or (Test-Path ".railway" -PathType Container)) {
                $projectLinked = $true
                Write-Host "Project linked" -ForegroundColor Green
            } else {
                # Create new project if link fails
                Write-Host "Creating new Railway project..." -ForegroundColor Yellow
                railway init --template python 2>&1 | Out-Null
                if ($LASTEXITCODE -eq 0 -or (Test-Path ".railway" -PathType Container)) {
                    $projectLinked = $true
                    Write-Host "New project created" -ForegroundColor Green
                }
            }
        }
        
        if (-not $projectLinked) {
            Write-Host "Warning: Could not link/create project. Continuing with deployment..." -ForegroundColor Yellow
        }
        
        if (Test-Path ".env") {
            Write-Host "Found .env file, setting variables..." -ForegroundColor Yellow
            # Read .env and set variables on Railway
            Get-Content .env | ForEach-Object {
                if ($_ -match '^([^=]+)=(.*)$' -and $_ -notmatch '^#') {
                    $key = $matches[1]
                    $value = $matches[2]
                    Write-Host "Setting $key..." -ForegroundColor Gray
                    railway variables set "$key=$value" 2>$null
                }
            }
        }
        
        Write-Host "Deploying..." -ForegroundColor Yellow
        railway up
    } catch {
        Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "Railway token set, retrying..." -ForegroundColor Yellow
        railway up
    }
    
    Set-Location ..
}

# Deploy frontend to Vercel
function Deploy-Frontend {
    Write-Host ""
    Write-Host "=== Deploying Frontend to Vercel ===" -ForegroundColor Cyan
    Set-Location frontend
    
    # Set Vercel token from saved token file
    $vercelTokenFile = "..\VERCEL_TOKEN_SAVED.md"
    if (Test-Path $vercelTokenFile) {
        $tokenContent = Get-Content $vercelTokenFile -Raw
        if ($tokenContent -match 'Token ID:.*`([^`]+)`') {
            $vercelToken = $matches[1]
            Write-Host "Vercel token loaded from file" -ForegroundColor Green
        }
    } else {
        # Fallback to hardcoded token if file not found
        $vercelToken = "I9OlHOgMOfHk3XMkn9uRropD"
        Write-Host "Using Vercel token" -ForegroundColor Yellow
    }
    
    try {
        vercel whoami --token $vercelToken 2>&1 | Out-Null
        Write-Host "Logged in to Vercel" -ForegroundColor Green
        Write-Host "Deploying..." -ForegroundColor Yellow
        vercel --prod --yes --token $vercelToken
    } catch {
        Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "Vercel token set, retrying..." -ForegroundColor Yellow
        vercel --prod --yes --token $vercelToken
    }
    
    Set-Location ..
}

# Main execution
Write-Host "Checking prerequisites..." -ForegroundColor Yellow
$railwayOk = Check-Railway
$vercelOk = Check-Vercel

if (-not $railwayOk -or -not $vercelOk) {
    Write-Host "Please install missing CLI tools first" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Starting full autonomous deployment..." -ForegroundColor Green
Write-Host "Deploying both backend and frontend..." -ForegroundColor Cyan

Deploy-Backend
Deploy-Frontend

Write-Host ""
Write-Host "=== Deployment Complete ===" -ForegroundColor Green

