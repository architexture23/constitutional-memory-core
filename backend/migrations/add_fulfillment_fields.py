"""
Database Migration: Add Fulfillment Fields to Purchase Table
Run this after updating the Purchase model
"""

import sys
import os

# Add backend directory to path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, backend_dir)

from sqlalchemy import text
from database import engine

def run_migration():
    """Add fulfillment fields to purchases table"""
    print("Running migration: Add fulfillment fields to Purchase table...")
    
    with engine.connect() as conn:
        try:
            # Add new columns (if they don't exist)
            conn.execute(text("""
                ALTER TABLE purchases 
                ADD COLUMN IF NOT EXISTS customer_email VARCHAR(255);
            """))
            
            conn.execute(text("""
                ALTER TABLE purchases 
                ADD COLUMN IF NOT EXISTS access_token VARCHAR(255) UNIQUE;
            """))
            
            conn.execute(text("""
                ALTER TABLE purchases 
                ADD COLUMN IF NOT EXISTS token_expires_at TIMESTAMP WITH TIME ZONE;
            """))
            
            conn.execute(text("""
                ALTER TABLE purchases 
                ADD COLUMN IF NOT EXISTS email_sent BOOLEAN DEFAULT FALSE;
            """))
            
            conn.execute(text("""
                ALTER TABLE purchases 
                ADD COLUMN IF NOT EXISTS email_sent_at TIMESTAMP WITH TIME ZONE;
            """))
            
            conn.execute(text("""
                ALTER TABLE purchases 
                ADD COLUMN IF NOT EXISTS stripe_checkout_session_id VARCHAR(255);
            """))
            
            # Create indexes
            conn.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_purchases_access_token ON purchases(access_token);
            """))
            
            conn.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_purchases_customer_email ON purchases(customer_email);
            """))
            
            conn.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_purchases_checkout_session ON purchases(stripe_checkout_session_id);
            """))
            
            conn.commit()
            print("[OK] Migration completed successfully!")
            print("Added fields:")
            print("  - customer_email")
            print("  - access_token")
            print("  - token_expires_at")
            print("  - email_sent")
            print("  - email_sent_at")
            print("  - stripe_checkout_session_id")
            
        except Exception as e:
            conn.rollback()
            print(f"[ERROR] Migration failed: {str(e)}")
            raise

if __name__ == "__main__":
    run_migration()

