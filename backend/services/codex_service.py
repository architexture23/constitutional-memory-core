"""
Truth Drop Platform - Codex Service
Built from Remembrance | Operating under Format Law
Constitutional Framework: Layer 1 - Structural Setup
"""

from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from typing import List, Optional
from datetime import datetime
from models import Codex, Domain, Tag
from schemas import CodexCreate, CodexUpdate
import os
import re
from config import settings

class CodexService:
    """Codex service - Constitutional Framework: Layer 1"""
    
    def __init__(self):
        self.format_law_version = "v1.3"
        self.constitutional_compliance = True
    
    async def list_codexes(
        self,
        db: Session,
        domain: Optional[str] = None,
        search: Optional[str] = None,
        tags: Optional[List[str]] = None,
        featured: Optional[bool] = None,
        skip: int = 0,
        limit: int = 50
    ) -> List[Codex]:
        """
        List codexes with filters
        Constitutional Framework: Layer 1 - Structural Setup
        """
        query = db.query(Codex).filter(
            Codex.is_active == True,
            Codex.published_at.isnot(None)  # Only show published codexes
        )
        
        # Domain filter
        if domain:
            query = query.join(Domain).filter(Domain.name == domain)
        
        # Featured filter
        if featured is not None:
            query = query.filter(Codex.is_featured == featured)
        
        # Search filter
        if search:
            search_term = f"%{search}%"
            query = query.filter(
                or_(
                    Codex.title.ilike(search_term),
                    Codex.description.ilike(search_term),
                    Codex.content.ilike(search_term)
                )
            )
        
        # Tags filter
        if tags:
            query = query.join(Codex.tags).filter(Tag.name.in_(tags))
        
        # Order by featured, then created_at
        query = query.order_by(Codex.is_featured.desc(), Codex.created_at.desc())
        
        # Pagination
        codexes = query.offset(skip).limit(limit).all()
        return codexes
    
    async def get_codex(self, db: Session, codex_id: int) -> Optional[Codex]:
        """Get codex by ID"""
        return db.query(Codex).filter(Codex.id == codex_id).first()
    
    async def get_codex_by_slug(self, db: Session, slug: str) -> Optional[Codex]:
        """Get codex by slug"""
        return db.query(Codex).filter(Codex.slug == slug).first()
    
    async def create_codex(
        self,
        db: Session,
        codex_data: CodexCreate
    ) -> Codex:
        """
        Create new codex
        Constitutional Framework: Layer 1 - Structural Setup
        """
        # Generate slug if not provided
        slug = codex_data.slug or self._generate_slug(codex_data.title)
        
        # Ensure slug is unique
        existing = await self.get_codex_by_slug(db, slug)
        if existing:
            slug = f"{slug}-{int(datetime.utcnow().timestamp())}"
        
        # Create codex
        codex = Codex(
            title=codex_data.title,
            slug=slug,
            description=codex_data.description,
            content=codex_data.content,
            domain_id=codex_data.domain_id,
            price=codex_data.price,
            currency=codex_data.currency,
            format_law_version=codex_data.format_law_version,
            constitutional_compliance=codex_data.constitutional_compliance,
            remembrance_integration=codex_data.remembrance_integration,
            version=codex_data.version,
            is_active=codex_data.is_active,
            is_featured=codex_data.is_featured,
            published_at=datetime.utcnow()
        )
        
        # Add tags
        if codex_data.tag_ids:
            tags = db.query(Tag).filter(Tag.id.in_(codex_data.tag_ids)).all()
            codex.tags = tags
        
        db.add(codex)
        db.commit()
        db.refresh(codex)
        
        return codex
    
    async def update_codex(
        self,
        db: Session,
        codex_id: int,
        codex_data: CodexUpdate
    ) -> Optional[Codex]:
        """Update codex"""
        codex = await self.get_codex(db, codex_id)
        if not codex:
            return None
        
        # Update fields
        if codex_data.title is not None:
            codex.title = codex_data.title
        if codex_data.description is not None:
            codex.description = codex_data.description
        if codex_data.domain_id is not None:
            codex.domain_id = codex_data.domain_id
        if codex_data.price is not None:
            codex.price = codex_data.price
        if codex_data.content is not None:
            codex.content = codex_data.content
        if codex_data.is_active is not None:
            codex.is_active = codex_data.is_active
        if codex_data.is_featured is not None:
            codex.is_featured = codex_data.is_featured
        
        # Update tags
        if codex_data.tag_ids is not None:
            tags = db.query(Tag).filter(Tag.id.in_(codex_data.tag_ids)).all()
            codex.tags = tags
        
        codex.updated_at = datetime.utcnow()
        
        db.commit()
        db.refresh(codex)
        
        return codex
    
    async def delete_codex(self, db: Session, codex_id: int) -> bool:
        """Delete codex (soft delete)"""
        codex = await self.get_codex(db, codex_id)
        if not codex:
            return False
        
        codex.is_active = False
        codex.updated_at = datetime.utcnow()
        
        db.commit()
        return True
    
    async def upload_content(
        self,
        db: Session,
        codex_id: int,
        file
    ) -> Optional[Codex]:
        """Upload codex content file"""
        codex = await self.get_codex(db, codex_id)
        if not codex:
            return None
        
        # Save file
        file_path = os.path.join(settings.UPLOAD_DIR, f"{codex.slug}_{codex.id}")
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Read content
        if file.filename.endswith('.md'):
            with open(file_path, "r", encoding="utf-8") as f:
                codex.content = f.read()
        elif file.filename.endswith('.txt'):
            with open(file_path, "r", encoding="utf-8") as f:
                codex.content = f.read()
        
        codex.file_path = file_path
        codex.updated_at = datetime.utcnow()
        
        db.commit()
        db.refresh(codex)
        
        return codex
    
    def _generate_slug(self, title: str) -> str:
        """Generate slug from title"""
        slug = title.lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug)
        slug = re.sub(r'^-+|-+$', '', slug)
        return slug

# Initialize service
codex_service = CodexService()

