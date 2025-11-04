"""
Truth Drop Platform - Fix Codexes Published Date
Built from Remembrance | Operating under Format Law
"""

import sys
from pathlib import Path
from datetime import datetime, timezone

# Add parent directory to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from database import SessionLocal
from models import Codex

def fix_codexes_published():
    """Set published_at for all codexes that don't have it"""
    print("Fixing codexes published_at...")
    
    with SessionLocal() as db:
        codexes = db.query(Codex).filter(Codex.published_at == None).all()
        print(f"Found {len(codexes)} codexes without published_at")
        
        for codex in codexes:
            codex.published_at = datetime.now(timezone.utc)
            print(f"  Set published_at for: {codex.title}")
        
        db.commit()
        print(f"[OK] Fixed {len(codexes)} codexes")
        
        # Verify
        total = db.query(Codex).count()
        published = db.query(Codex).filter(Codex.published_at.isnot(None)).count()
        print(f"[OK] Total codexes: {total}, Published: {published}")

if __name__ == "__main__":
    try:
        fix_codexes_published()
    except Exception as e:
        print(f"[ERROR] Error fixing codexes: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

