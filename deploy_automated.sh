#!/bin/bash
# Automated Deployment Script for Truth Drop Platform
# This script automates deployment to Railway (backend) and Vercel (frontend)

echo "=== Truth Drop Platform - Automated Deployment ==="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Railway CLI is installed
check_railway() {
    if command -v railway &> /dev/null; then
        echo -e "${GREEN}✅ Railway CLI installed${NC}"
        return 0
    else
        echo -e "${RED}❌ Railway CLI not found${NC}"
        echo "Install with: npm install -g @railway/cli"
        return 1
    fi
}

# Check if Vercel CLI is installed
check_vercel() {
    if command -v vercel &> /dev/null; then
        echo -e "${GREEN}✅ Vercel CLI installed${NC}"
        return 0
    else
        echo -e "${RED}❌ Vercel CLI not found${NC}"
        echo "Install with: npm install -g vercel"
        return 1
    fi
}

# Deploy backend to Railway
deploy_backend() {
    echo ""
    echo "=== Deploying Backend to Railway ==="
    cd backend
    
    if railway whoami &> /dev/null; then
        echo "Logged in to Railway"
        
        if [ -f ".env" ]; then
            echo "Found .env file, setting variables..."
            # Read .env and set variables on Railway
            while IFS='=' read -r key value; do
                if [[ ! $key =~ ^# ]] && [[ -n $key ]]; then
                    railway variables set "$key=$value" 2>/dev/null
                fi
            done < .env
        fi
        
        echo "Deploying..."
        railway up
    else
        echo "Please login first: railway login"
    fi
    
    cd ..
}

# Deploy frontend to Vercel
deploy_frontend() {
    echo ""
    echo "=== Deploying Frontend to Vercel ==="
    cd frontend
    
    if vercel whoami &> /dev/null; then
        echo "Logged in to Vercel"
        echo "Deploying..."
        vercel --prod
    else
        echo "Please login first: vercel login"
    fi
    
    cd ..
}

# Main execution
main() {
    echo "Checking prerequisites..."
    check_railway
    check_vercel
    
    echo ""
    echo "Choose deployment:"
    echo "1. Backend only (Railway)"
    echo "2. Frontend only (Vercel)"
    echo "3. Both"
    read -p "Enter choice (1-3): " choice
    
    case $choice in
        1) deploy_backend ;;
        2) deploy_frontend ;;
        3) deploy_backend; deploy_frontend ;;
        *) echo "Invalid choice" ;;
    esac
}

main

