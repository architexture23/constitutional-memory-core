"""
Debug search endpoint
"""
import sys
from pathlib import Path

backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

try:
    from services.search_service import SearchService
    from database import SessionLocal
    from models import Codex
    
    db = SessionLocal()
    service = SearchService()
    
    # Test search
    print("Testing search service...")
    import asyncio
    try:
        result = asyncio.run(service.search_codexes(db, 'trading'))
        print(f"Results count: {len(result.results)}")
        print(f"Total: {result.total}")
        if result.results:
            print(f"First result: {result.results[0].codex.title}")
        print("SUCCESS")
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
    
    # Check codexes
    codexes = db.query(Codex).filter(Codex.is_active == True, Codex.published_at.isnot(None)).all()
    print(f"\nActive published codexes: {len(codexes)}")
    for c in codexes:
        print(f"  - {c.title} (domain: {c.domain.name if c.domain else None})")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

