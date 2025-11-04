"""Simple search test"""
import sys
from pathlib import Path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from database import SessionLocal
from models import Codex, Domain
from sqlalchemy import or_, and_

db = SessionLocal()

# Test direct query
try:
    query = db.query(Codex).filter(
        Codex.is_active == True
    ).filter(
        Codex.published_at.isnot(None)
    )
    
    # Search for "trading"
    search_terms = "trading".lower().split()
    search_filters = []
    for term in search_terms:
        term_filter = or_(
            Codex.title.ilike(f"%{term}%"),
            Codex.description.ilike(f"%{term}%"),
            Codex.content.ilike(f"%{term}%")
        )
        search_filters.append(term_filter)
    
    if search_filters:
        combined_filter = and_(*search_filters)
        query = query.filter(combined_filter)
    
    codexes = query.all()
    print(f"Found {len(codexes)} codexes")
    for c in codexes:
        print(f"  - {c.title}")
    
    print("SUCCESS")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()

