"""
Database Migration: Make user_id nullable in Purchase table for guest purchases
Run this to allow guest purchases (no user account required)
"""

import sys
import os

# Add backend directory to path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, backend_dir)

from sqlalchemy import text
from database import engine

def run_migration():
    """Make user_id nullable in purchases table"""
    print("Running migration: Make user_id nullable in Purchase table...")
    
    with engine.connect() as conn:
        try:
            # Make user_id nullable (for guest purchases)
            conn.execute(text("""
                ALTER TABLE purchases 
                ALTER COLUMN user_id DROP NOT NULL;
            """))
            
            conn.commit()
            print("[OK] Migration completed successfully!")
            print("Updated:")
            print("  - user_id: Now nullable (allows guest purchases)")
            
        except Exception as e:
            conn.rollback()
            print(f"[ERROR] Migration failed: {str(e)}")
            # Check if column is already nullable
            if "does not exist" in str(e) or "already" in str(e).lower():
                print("[INFO] Column might already be nullable. Checking...")
            raise

if __name__ == "__main__":
    run_migration()

