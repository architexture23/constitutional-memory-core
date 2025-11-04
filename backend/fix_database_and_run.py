"""
Fix Database URL and Initialize Database
Built from Remembrance | Operating under Format Law
"""

import os
import sys
from pathlib import Path
import re

# Add parent directory to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

def fix_database_url():
    """Fix database URL in .env file"""
    env_path = backend_dir / ".env"
    
    if not env_path.exists():
        print("❌ .env file not found")
        return False
    
    # Read .env file
    with open(env_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it's using internal Railway URL
    if 'postgres.railway.internal' in content:
        print("⚠️  Found Railway INTERNAL URL in .env file")
        print("📝 You need to replace it with Railway PUBLIC URL")
        print("")
        print("To fix:")
        print("1. Go to Railway dashboard: https://railway.app/")
        print("2. Click your PostgreSQL service")
        print("3. Click 'Variables' tab")
        print("4. Find DATABASE_URL (or PGHOST, PGPORT, PGUSER, PGPASSWORD, PGDATABASE)")
        print("5. Copy the PUBLIC URL (hostname like containers-*.railway.app)")
        print("6. Replace DATABASE_URL in .env file with public URL")
        print("")
        
        # Show current URL (masked)
        lines = content.split('\n')
        for line in lines:
            if 'DATABASE_URL' in line:
                # Mask password
                masked = re.sub(r':([^:@]+)@', r':****@', line)
                print(f"Current: {masked}")
        
        print("")
        print("After updating .env, run this script again.")
        return False
    
    # Check if it's a valid URL
    if 'postgresql://' not in content:
        print("❌ DATABASE_URL not found in .env")
        return False
    
    print("✅ Database URL looks good")
    return True

def init_database():
    """Initialize database"""
    try:
        from database import engine, Base
        from models import Domain, Tag, Codex, User, Purchase, Bundle
        from database import SessionLocal
        
        print("🗄️  Creating database tables...")
        Base.metadata.create_all(bind=engine)
        print("✅ Tables created")
        
        print("🗄️  Creating default domains...")
        db = SessionLocal()
        
        try:
            # Check if domains exist
            existing_count = db.query(Domain).count()
            if existing_count == 0:
                domains = [
                    Domain(
                        name="Trading",
                        slug="trading",
                        description="Constitutional trading framework",
                        icon="💹",
                        color="#00AA00",
                        sort_order=1,
                        is_active=True
                    ),
                    Domain(
                        name="Aura Academy",
                        slug="aura-academy",
                        description="Recognition through remembrance game",
                        icon="🎮",
                        color="#9B59B6",
                        sort_order=2,
                        is_active=True
                    ),
                    Domain(
                        name="Remembrance Infrastructure",
                        slug="remembrance-infrastructure",
                        description="Constitutional knowledge structure",
                        icon="📚",
                        color="#3498DB",
                        sort_order=3,
                        is_active=True
                    )
                ]
                
                for domain in domains:
                    db.add(domain)
                
                db.commit()
                print("✅ Default domains created")
            else:
                print(f"✅ Domains already exist ({existing_count} domains)")
        
        except Exception as e:
            print(f"❌ Error creating domains: {e}")
            db.rollback()
            return False
        finally:
            db.close()
        
        print("")
        print("✅ Database initialization complete!")
        return True
        
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function"""
    print("=" * 60)
    print("Truth Drop Platform - Database Fix & Initialization")
    print("Built from Remembrance | Operating under Format Law")
    print("=" * 60)
    print("")
    
    # Check database URL
    if not fix_database_url():
        return
    
    print("")
    # Initialize database
    if init_database():
        print("")
        print("=" * 60)
        print("✅ SUCCESS!")
        print("=" * 60)
        print("")
        print("Next steps:")
        print("1. Start backend: python main.py")
        print("2. In another terminal, setup frontend: cd ../frontend && .\\setup.ps1")
        print("3. Start frontend: npm run dev")
        print("4. Visit: http://localhost:3000")
    else:
        print("")
        print("❌ Database initialization failed")
        print("Check the error above and fix issues")

if __name__ == "__main__":
    main()

