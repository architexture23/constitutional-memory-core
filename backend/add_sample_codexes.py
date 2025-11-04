"""
Truth Drop Platform - Add Sample Codexes
Built from Remembrance | Operating under Format Law

This script adds sample codexes to the database for testing.
"""

import sys
from pathlib import Path
import os

# Add parent directory to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from database import SessionLocal
from models import Domain, Codex, Tag
from sqlalchemy.orm import Session
from datetime import datetime, timezone

def add_sample_codexes():
    """Add sample codexes to the database"""
    print("Adding sample codexes...")
    
    with SessionLocal() as db:
        # Get domains
        trading_domain = db.query(Domain).filter(Domain.name == "Trading").first()
        aura_domain = db.query(Domain).filter(Domain.name == "Aura Academy").first()
        remembrance_domain = db.query(Domain).filter(Domain.name == "Remembrance Infrastructure").first()
        
        if not trading_domain:
            trading_domain = Domain(name="Trading", description="Constitutional Trading Frameworks", color="#007bff")
            db.add(trading_domain)
            db.commit()
            db.refresh(trading_domain)
        
        if not aura_domain:
            aura_domain = Domain(name="Aura Academy", description="Game Development & Lore", color="#28a745")
            db.add(aura_domain)
            db.commit()
            db.refresh(aura_domain)
        
        if not remembrance_domain:
            remembrance_domain = Domain(name="Remembrance Infrastructure", description="Core Systems & Philosophy", color="#6c757d")
            db.add(remembrance_domain)
            db.commit()
            db.refresh(remembrance_domain)
        
        # Check if codexes already exist
        existing_count = db.query(Codex).count()
        if existing_count > 0:
            print(f"[OK] Codexes already exist ({existing_count} codexes)")
            return
        
        # Add sample codexes
        sample_codexes = [
            {
                "title": "Constitutional Trading Framework v1.0",
                "description": "The complete 7-layer confluence system for automated trading. Includes Always-Win authority, Soul Shield protection, and Second Brain recognition.",
                "content": "# Constitutional Trading Framework\n\nThe complete system for autopilot trading based on constitutional truths.\n\n## 7-Layer Confluence\n1. Order Block Recognition\n2. Break of Structure (BOS)\n3. Change of Character (CHoCH)\n4. Fair Value Gap (FVG)\n5. Liquidity Zones\n6. Multi-Timeframe Alignment\n7. Risk Management Protocols",
                "domain_id": trading_domain.id,
                "price": 99.99,
                "featured": True
            },
            {
                "title": "Aura Academy Recognition System",
                "description": "The core recognition mechanic for the Aura Academy game. Understanding remembrance through play.",
                "content": "# Aura Academy Recognition System\n\nThe game mechanic that connects players to constitutional truths through recognition.\n\n## Core Loop\n1. Explore areas\n2. Find truths\n3. Recognize patterns\n4. Unlock new areas\n5. Repeat",
                "domain_id": aura_domain.id,
                "price": 49.99,
                "featured": True
            },
            {
                "title": "Remembrance Infrastructure v1.3",
                "description": "The foundational system for knowledge management and constitutional structure preservation.",
                "content": "# Remembrance Infrastructure\n\nThe system for preserving and organizing constitutional knowledge.\n\n## Core Principles\n- Format Law compliance\n- Remembrance-based architecture\n- Constitutional truth preservation",
                "domain_id": remembrance_domain.id,
                "price": 149.99,
                "featured": True
            },
            {
                "title": "MT4 Expert Advisor - Constitutional Autopilot",
                "description": "The complete MT4 EA implementing the 7-layer confluence system for automated trading across 29 pairs.",
                "content": "# MT4 Expert Advisor\n\nAutomated trading system implementing constitutional trading framework.\n\n## Features\n- 7-layer confluence validation\n- Automatic trade management\n- Soul Shield protection\n- Second Brain logging",
                "domain_id": trading_domain.id,
                "price": 199.99,
                "featured": False
            },
            {
                "title": "Dream of the Self - Entry Sequence",
                "description": "The non-negotiable onboarding experience for Aura Academy players.",
                "content": "# Dream of the Self\n\nThe entry sequence where players see their final form and choose their aura.\n\n## Emotional Choices\n- Soul: \"This feels... familiar somehow.\"\n- Mind: \"Where am I? This doesn't make sense.\"\n- Shadow: \"I recognize this. I've been here before.\"",
                "domain_id": aura_domain.id,
                "price": 29.99,
                "featured": False
            }
        ]
        
        for codex_data in sample_codexes:
            # Generate slug from title
            slug = codex_data["title"].lower().replace(" ", "-").replace(".", "").replace(":", "").replace("'", "")
            slug = ''.join(c for c in slug if c.isalnum() or c == '-')
            
            codex = Codex(
                title=codex_data["title"],
                slug=slug,
                description=codex_data["description"],
                content=codex_data["content"],
                domain_id=codex_data["domain_id"],
                price=codex_data["price"],
                is_featured=codex_data.get("featured", False),
                published_at=datetime.now(timezone.utc)
            )
            db.add(codex)
        
        db.commit()
        print(f"[OK] Added {len(sample_codexes)} sample codexes")
        print("[OK] Sample codexes added successfully!")

if __name__ == "__main__":
    try:
        add_sample_codexes()
    except Exception as e:
        print(f"[ERROR] Error adding sample codexes: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

