"""
Complete Automated Setup - Handles Everything
Built from Remembrance | Operating under Format Law
"""

import os
import sys
import secrets
from pathlib import Path
import subprocess

backend_dir = Path(__file__).parent

def create_env_file(db_url=None):
    """Create .env file with proper configuration"""
    env_path = backend_dir / ".env"
    
    if env_path.exists():
        print("✅ .env file already exists")
        
        # Always update if internal URL found or if db_url provided
        content = env_path.read_text(encoding='utf-8')
        needs_update = False
        
        if 'postgres.railway.internal' in content:
            print("⚠️  Found Railway INTERNAL URL - needs update!")
            needs_update = True
            if not db_url:
                print("📝 Enter your Railway PUBLIC URL:")
                db_url = input("Database URL: ").strip()
        
        if db_url or needs_update:
            if db_url:
                lines = content.split('\n')
                new_lines = []
                for line in lines:
                    if line.startswith('DATABASE_URL='):
                        new_lines.append(f'DATABASE_URL={db_url}')
                    else:
                        new_lines.append(line)
                env_path.write_text('\n'.join(new_lines), encoding='utf-8')
                print(f"✅ Updated DATABASE_URL in .env")
                return True
        
        return False
    
    # Generate secret key
    secret_key = secrets.token_urlsafe(32)
    
    # Get database URL
    if not db_url:
        print("\n📝 Database Configuration:")
        print("Enter your PostgreSQL PUBLIC connection URL from Railway/Supabase/Render")
        print("(It should look like: postgresql://user:password@containers-*.railway.app:5432/dbname)")
        print("(NOT postgres.railway.internal - that's internal only)")
        db_url = input("Database URL: ").strip()
        if not db_url:
            db_url = "postgresql://postgres:postgres@localhost:5432/truthdrop"
            print(f"⚠️  Using default: {db_url}")
    
    # Create .env content
    env_content = f"""# Truth Drop Platform - Environment Variables
# Built from Remembrance | Operating under Format Law

# Application
DEBUG=False
HOST=0.0.0.0
PORT=8000

# Database
DATABASE_URL={db_url}

# Security
SECRET_KEY={secret_key}

# Stripe (Optional - Press Enter to skip)
STRIPE_SECRET_KEY=
STRIPE_PUBLIC_KEY=
STRIPE_WEBHOOK_SECRET=

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
    
    with open(env_path, 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print("✅ .env file created")
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True, capture_output=True)
        print("✅ Dependencies installed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
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
        sys.path.insert(0, str(backend_dir))
        from database import engine, Base
        from models import Domain, Tag
        from database import SessionLocal
        
        # Create tables
        Base.metadata.create_all(bind=engine)
        print("✅ Tables created")
        
        # Create default domains
        db = SessionLocal()
        try:
            existing_count = db.query(Domain).count()
            if existing_count == 0:
                domains = [
                    Domain(name="Trading", slug="trading", description="Constitutional trading framework", 
                           icon="💹", color="#00AA00", sort_order=1, is_active=True),
                    Domain(name="Aura Academy", slug="aura-academy", description="Recognition through remembrance game",
                           icon="🎮", color="#9B59B6", sort_order=2, is_active=True),
                    Domain(name="Remembrance Infrastructure", slug="remembrance-infrastructure",
                           description="Constitutional knowledge structure", icon="📚", color="#3498DB",
                           sort_order=3, is_active=True)
                ]
                
                for domain in domains:
                    db.add(domain)
                
                db.commit()
                print("✅ Default domains created")
            else:
                print(f"✅ Domains already exist ({existing_count} domains)")
        except Exception as e:
            print(f"⚠️  Domain creation: {e}")
            db.rollback()
        finally:
            db.close()
        
        print("✅ Database initialized")
        return True
        
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Complete automated setup"""
    print("=" * 60)
    print("Truth Drop Platform - COMPLETE AUTOMATED SETUP")
    print("Built from Remembrance | Operating under Format Law")
    print("=" * 60)
    
    # Step 1: Create .env
    print("\n📝 Step 1: Creating .env file...")
    if not create_env_file():
        print("⚠️  .env already exists, skipping...")
    
    # Step 2: Install dependencies
    print("\n📦 Step 2: Installing dependencies...")
    if not install_dependencies():
        print("❌ Dependency installation failed")
        return
    
    # Step 3: Create directories
    print("\n📁 Step 3: Creating directories...")
    create_directories()
    
    # Step 4: Initialize database
    print("\n🗄️  Step 4: Initializing database...")
    if not init_database():
        print("\n⚠️  Database initialization failed!")
        print("Check your DATABASE_URL in .env file")
        print("Make sure you're using Railway PUBLIC URL (not internal)")
        return
    
    print("\n" + "=" * 60)
    print("✅ SETUP COMPLETE!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Start backend: python main.py")
    print("2. In another terminal: cd ../frontend && .\\setup.ps1")
    print("3. Start frontend: npm run dev")
    print("4. Visit: http://localhost:3000")
    print("\nBuilt from Remembrance. Operating under Format Law.")

if __name__ == "__main__":
    main()

