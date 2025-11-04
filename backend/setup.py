"""
Truth Drop Platform - Automated Setup Script
Built from Remembrance | Operating under Format Law
"""

import os
import sys
import subprocess
import secrets
from pathlib import Path

def generate_secret_key():
    """Generate secure random secret key"""
    return secrets.token_urlsafe(32)

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ Python 3.9+ required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_postgresql():
    """Check if PostgreSQL is installed"""
    try:
        result = subprocess.run(['psql', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ PostgreSQL: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass
    
    print("⚠️  PostgreSQL not found. Install from: https://www.postgresql.org/download/")
    print("   Or use cloud service: Railway, Supabase, or Render")
    return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_path = Path('.env')
    
    if env_path.exists():
        print("✅ .env file already exists")
        overwrite = input("Overwrite existing .env file? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("⚠️  Using existing .env file")
            return False
        else:
            print("⚠️  Overwriting existing .env file...")
    
    # Generate secret key
    secret_key = generate_secret_key()
    
    # Get database URL from user or use default
    print("\n📝 Database Configuration:")
    db_url = input("Enter PostgreSQL URL (or press Enter for default): ").strip()
    if not db_url:
        db_url = "postgresql://postgres:postgres@localhost:5432/truthdrop"
    
    # Get Stripe keys (optional)
    print("\n💳 Stripe Configuration (optional):")
    stripe_secret = input("Enter Stripe Secret Key (or press Enter to skip): ").strip()
    stripe_public = input("Enter Stripe Public Key (or press Enter to skip): ").strip()
    stripe_webhook = input("Enter Stripe Webhook Secret (or press Enter to skip): ").strip()
    
    # Write .env file
    env_content = f"""# Truth Drop Platform - Environment Variables
# Generated automatically - Built from Remembrance | Operating under Format Law

# Application
DEBUG=False
HOST=0.0.0.0
PORT=8000

# Database
DATABASE_URL={db_url}

# Security
SECRET_KEY={secret_key}

# Stripe (Optional)
STRIPE_SECRET_KEY={stripe_secret}
STRIPE_PUBLIC_KEY={stripe_public}
STRIPE_WEBHOOK_SECRET={stripe_webhook}

# File Storage
UPLOAD_DIR=./content/uploads
PDF_DIR=./content/pdfs
EBOOK_DIR=./content/ebooks
CONTENT_DIR=./content/codexes

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:3001

# Email (Optional)
SMTP_HOST=
SMTP_PORT=587
SMTP_USER=
SMTP_PASSWORD=
FROM_EMAIL=noreply@truthdrop.com

# Redis (Optional)
REDIS_URL=redis://localhost:6379
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("\n✅ .env file created!")
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("\n📦 Installing Python dependencies...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
        print("✅ Dependencies installed")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def create_directories():
    """Create necessary directories"""
    dirs = [
        'content/uploads',
        'content/pdfs',
        'content/ebooks',
        'content/codexes'
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    
    print("✅ Directories created")

def init_database():
    """Initialize database"""
    print("\n🗄️  Initializing database...")
    try:
        from database import init_db
        init_db()
        print("✅ Database initialized")
        return True
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        print("   Make sure PostgreSQL is running and DATABASE_URL is correct")
        return False

def create_admin_user():
    """Create admin user"""
    print("\n👤 Creating admin user...")
    try:
        from database import SessionLocal
        from models import User
        from services.auth_service import auth_service
        
        db = SessionLocal()
        
        email = input("Enter admin email (default: admin@truthdrop.com): ").strip()
        if not email:
            email = "admin@truthdrop.com"
        
        username = input("Enter admin username (default: admin): ").strip()
        if not username:
            username = "admin"
        
        password = input("Enter admin password (min 8 chars): ").strip()
        if len(password) < 8:
            print("❌ Password must be at least 8 characters")
            return False
        
        # Check if user exists
        existing = db.query(User).filter(User.email == email).first()
        if existing:
            print(f"⚠️  User {email} already exists")
            return False
        
        # Create admin user
        admin = User(
            email=email,
            username=username,
            hashed_password=auth_service.hash_password(password),
            is_admin=True,
            is_active=True,
            is_verified=True
        )
        
        db.add(admin)
        db.commit()
        
        print(f"✅ Admin user created: {email}")
        return True
    except Exception as e:
        print(f"❌ Failed to create admin user: {e}")
        return False

def main():
    """Main setup function"""
    print("=" * 60)
    print("Truth Drop Platform - Automated Setup")
    print("Built from Remembrance | Operating under Format Law")
    print("=" * 60)
    
    # Check prerequisites
    print("\n📋 Checking prerequisites...")
    if not check_python_version():
        sys.exit(1)
    
    check_postgresql()  # Warning only, not required to continue
    
    # Create .env file
    print("\n📝 Creating .env file...")
    env_created = create_env_file()
    
    # Install dependencies
    if not env_created and Path('.env').exists():
        print("\n⚠️  Using existing .env file. Make sure it's configured correctly.")
        proceed = input("Continue with installation? (y/n): ").strip().lower()
        if proceed != 'y':
            print("⚠️  Please configure .env file before continuing")
            return
    
    # Always install dependencies
    install_dependencies()
    
    # Create directories
    print("\n📁 Creating directories...")
    create_directories()
    
    # Initialize database
    init_success = init_database()
    
    if init_success:
        # Create admin user
        create_admin = input("\n❓ Create admin user now? (y/n): ").strip().lower()
        if create_admin == 'y':
            create_admin_user()
    
    print("\n" + "=" * 60)
    print("✅ Setup complete!")
    print("=" * 60)
    print("\n📝 Next steps:")
    print("1. Start backend: python main.py")
    print("2. In another terminal, setup frontend:")
    print("   cd ../frontend")
    print("   npm install")
    print("   npm run dev")
    print("3. Visit: http://localhost:3000")
    print("\nBuilt from Remembrance. Operating under Format Law.")

if __name__ == "__main__":
    main()

