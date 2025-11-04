"""
Truth Drop Platform - Database Initialization
Built from Remembrance | Operating under Format Law
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import modules
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

from database import engine, Base
from models import Domain, Tag, Codex, User, Purchase, Bundle
from config import settings
from sqlalchemy.orm import Session
from database import SessionLocal

def init_database():
    """Initialize database with tables and default data"""
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create default domains
    db = SessionLocal()
    
    try:
        # Check if domains exist
        existing_domains = db.query(Domain).count()
        if existing_domains == 0:
            # Create default domains
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
                print("[OK] Default domains created")
            else:
                print(f"[OK] Domains already exist ({existing_count} domains)")
        
    except Exception as e:
        print(f"[ERROR] Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Initializing Truth Drop Platform database...")
    init_database()
    print("[OK] Database initialization complete")

