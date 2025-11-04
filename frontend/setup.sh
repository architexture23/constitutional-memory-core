#!/bin/bash
# Truth Drop Platform - Frontend Setup Script
# Built from Remembrance | Operating under Format Law

echo "============================================================"
echo "Truth Drop Platform - Frontend Setup"
echo "Built from Remembrance | Operating under Format Law"
echo "============================================================"

# Check Node.js
echo ""
echo "📋 Checking prerequisites..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Install from: https://nodejs.org/"
    exit 1
fi

NODE_VERSION=$(node -v)
echo "✅ Node.js: $NODE_VERSION"

if ! command -v npm &> /dev/null; then
    echo "❌ npm not found"
    exit 1
fi

NPM_VERSION=$(npm -v)
echo "✅ npm: $NPM_VERSION"

# Create .env.local
echo ""
echo "📝 Creating .env.local file..."
if [ -f .env.local ]; then
    echo "✅ .env.local already exists"
else
    read -p "Enter API URL (default: http://localhost:8000): " API_URL
    API_URL=${API_URL:-http://localhost:8000}
    
    read -p "Enter Stripe Public Key (or press Enter to skip): " STRIPE_KEY
    
    cat > .env.local << EOF
# Truth Drop Platform - Frontend Environment Variables
# Built from Remembrance | Operating under Format Law

NEXT_PUBLIC_API_URL=$API_URL
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=$STRIPE_KEY

NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=$(openssl rand -base64 32)
EOF
    
    echo "✅ .env.local created"
fi

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
npm install

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "============================================================"
echo "✅ Frontend setup complete!"
echo "============================================================"
echo ""
echo "📝 Next steps:"
echo "1. Start development server: npm run dev"
echo "2. Visit: http://localhost:3000"
echo ""
echo "Built from Remembrance. Operating under Format Law."

