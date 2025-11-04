"""
Railway Deployment Automation Script
Automates backend deployment to Railway.app
"""
import os
import subprocess
import sys
from pathlib import Path

def check_railway_cli():
    """Check if Railway CLI is installed"""
    try:
        result = subprocess.run(['railway', '--version'], capture_output=True, text=True)
        return True
    except FileNotFoundError:
        return False

def install_railway_cli():
    """Install Railway CLI"""
    print("Installing Railway CLI...")
    print("Please visit: https://docs.railway.app/develop/cli")
    print("For Windows: Download from https://github.com/railwayapp/cli/releases")
    print("\nOr run: npm install -g @railway/cli")
    return False

def deploy_to_railway():
    """Deploy backend to Railway"""
    print("=== Railway Deployment Automation ===")
    print("\nStep 1: Checking Railway CLI...")
    
    if not check_railway_cli():
        print("\n❌ Railway CLI not found.")
        install_railway_cli()
        return False
    
    print("✅ Railway CLI found")
    
    print("\nStep 2: Checking login status...")
    result = subprocess.run(['railway', 'whoami'], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("❌ Not logged in to Railway")
        print("\nPlease run: railway login")
        print("This will open your browser to authenticate")
        return False
    
    print("✅ Logged in to Railway")
    
    print("\nStep 3: Linking project...")
    print("If project not linked, run: railway link")
    
    print("\nStep 4: Setting environment variables...")
    print("Reading from .env file...")
    
    env_file = Path('.env')
    if not env_file.exists():
        print("❌ No .env file found")
        print("Please create .env file with your variables")
        return False
    
    print("✅ .env file found")
    print("\nTo set variables on Railway, run:")
    print("  railway variables set DATABASE_URL=<your-url>")
    print("  railway variables set STRIPE_SECRET_KEY=<your-key>")
    print("  etc...")
    
    print("\nStep 5: Deploying...")
    print("Run: railway up")
    print("\nThis will deploy your backend to Railway!")
    
    return True

def main():
    """Main deployment function"""
    os.chdir(Path(__file__).parent)
    
    print("Truth Drop Platform - Railway Deployment\n")
    
    deploy_to_railway()
    
    print("\n" + "="*50)
    print("Deployment automation complete!")
    print("="*50)
    print("\nNext steps:")
    print("1. Install Railway CLI (if not already)")
    print("2. Run: railway login")
    print("3. Run: railway init (if new project)")
    print("4. Run: railway link (to link existing project)")
    print("5. Set environment variables")
    print("6. Run: railway up (to deploy)")

if __name__ == "__main__":
    main()

