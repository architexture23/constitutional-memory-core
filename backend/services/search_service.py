"""
Truth Drop Platform - Search Service
Built from Remembrance | Operating under Format Law
Constitutional Framework: Layer 3 - Liquidity Manipulation (Pattern Discovery)
"""

from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, func
from typing import List, Optional, Dict
from models import Codex, Domain, Tag
from schemas import SearchResult, SearchResponse

class SearchService:
    """Search service - Constitutional Framework: Layer 3"""
    
    async def search_codexes(
        self,
        db: Session,
        query: str,
        domain: Optional[str] = None,
        skip: int = 0,
        limit: int = 50
    ) -> SearchResponse:
        """
        Search codexes
        Constitutional Framework: Layer 3 - Liquidity Manipulation (Pattern Discovery)
        """
        # Base query - only active and published codexes
        codex_query = db.query(Codex).filter(
            Codex.is_active == True,
            Codex.published_at.isnot(None)
        )
        
        # Domain filter
        if domain:
            codex_query = codex_query.join(Domain).filter(Domain.name == domain)
        
        # Search terms
        search_terms = query.lower().split()
        search_filters = []
        
        for term in search_terms:
            term_filter = or_(
                Codex.title.ilike(f"%{term}%"),
                Codex.description.ilike(f"%{term}%"),
                Codex.content.ilike(f"%{term}%")
            )
            search_filters.append(term_filter)
        
        if search_filters:
            # Combine all search terms with AND
            combined_filter = and_(*search_filters)
            codex_query = codex_query.filter(combined_filter)
        
        # Execute query
        codexes = codex_query.order_by(
            Codex.is_featured.desc(),
            Codex.purchase_count.desc(),
            Codex.created_at.desc()
        ).offset(skip).limit(limit).all()
        
        # Calculate relevance scores
        results = []
        from schemas import CodexResponse
        for codex in codexes:
            relevance = self._calculate_relevance(codex, query)
            # Use model_validate with from_attributes for Pydantic v2
            try:
                codex_response = CodexResponse.model_validate(codex, from_attributes=True)
            except Exception as e:
                # Fallback: manual conversion if model_validate fails
                print(f"[SearchService] Error validating codex {codex.id}: {e}")
                import traceback
                traceback.print_exc()
                from schemas import DomainResponse, TagResponse
                domain_data = None
                if codex.domain:
                    try:
                        domain_data = DomainResponse.model_validate(codex.domain, from_attributes=True)
                    except Exception as de:
                        # Fallback to DomainResponse from dict
                        try:
                            domain_data = DomainResponse.model_validate({
                                "id": codex.domain.id,
                                "name": codex.domain.name,
                                "slug": codex.domain.slug,
                                "description": codex.domain.description,
                                "color": codex.domain.color,
                                "is_active": codex.domain.is_active,
                                "sort_order": codex.domain.sort_order,
                                "icon": codex.domain.icon,
                                "created_at": codex.domain.created_at,
                                "updated_at": codex.domain.updated_at,
                            })
                        except:
                            domain_data = None
                
                tags_data = []
                if codex.tags:
                    for tag in codex.tags:
                        try:
                            tags_data.append(TagResponse.model_validate(tag, from_attributes=True))
                        except Exception as te:
                            # Fallback to TagResponse from dict
                            try:
                                tags_data.append(TagResponse.model_validate({
                                    "id": tag.id,
                                    "name": tag.name,
                                    "slug": tag.slug,
                                    "description": tag.description,
                                    "color": tag.color,
                                    "created_at": tag.created_at,
                                }))
                            except:
                                pass
                
                codex_response = CodexResponse(
                    id=codex.id,
                    title=codex.title,
                    slug=codex.slug,
                    description=codex.description,
                    domain_id=codex.domain_id,
                    tag_ids=[tag.id for tag in codex.tags] if codex.tags else [],
                    price=codex.price,
                    currency=codex.currency,
                    is_featured=codex.is_featured,
                    version=codex.version,
                    format_law_version=codex.format_law_version,
                    constitutional_compliance=codex.constitutional_compliance,
                    remembrance_integration=codex.remembrance_integration,
                    is_active=codex.is_active,
                    view_count=codex.view_count,
                    purchase_count=codex.purchase_count,
                    download_count=codex.download_count,
                    created_at=codex.created_at,
                    updated_at=codex.updated_at,
                    published_at=codex.published_at,
                    domain=domain_data,
                    tags=tags_data,
                )
            results.append(SearchResult(
                codex=codex_response,
                relevance_score=relevance,
                matched_fields=self._get_matched_fields(codex, query)
            ))
        
        # Sort by relevance
        results.sort(key=lambda x: x.relevance_score or 0, reverse=True)
        
        total = codex_query.count()
        
        return SearchResponse(
            results=results,
            total=total,
            query=query,
            domain=domain
        )
    
    async def remembrance_search(
        self,
        db: Session,
        query: str,
        domain: Optional[str] = None
    ) -> List[Dict]:
        """
        Remembrance-based search
        Constitutional Framework: Recognition through remembrance
        """
        # Use same search but with remembrance scoring
        search_response = await self.search_codexes(db, query, domain)
        
        # Add remembrance-specific scoring
        remembrance_results = []
        for result in search_response.results:
            remembrance_score = self._calculate_remembrance_score(result.codex, query)
            remembrance_results.append({
                "codex": result.codex,
                "relevance_score": result.relevance_score,
                "remembrance_score": remembrance_score,
                "matched_fields": result.matched_fields
            })
        
        return remembrance_results
    
    async def get_remembrance_patterns(
        self,
        db: Session,
        domain: Optional[str] = None
    ) -> List[Dict]:
        """Get remembrance patterns"""
        # Find codexes with high remembrance integration
        query = db.query(Codex).filter(
            Codex.is_active == True,
            Codex.remembrance_integration == True
        )
        
        if domain:
            query = query.join(Domain).filter(Domain.name == domain)
        
        codexes = query.order_by(
            Codex.purchase_count.desc(),
            Codex.view_count.desc()
        ).limit(20).all()
        
        patterns = []
        for codex in codexes:
            patterns.append({
                "codex": codex,
                "pattern_type": self._identify_pattern_type(codex),
                "remembrance_level": "high" if codex.remembrance_integration else "low"
            })
        
        return patterns
    
    def _calculate_relevance(self, codex: Codex, query: str) -> float:
        """Calculate relevance score"""
        query_lower = query.lower()
        score = 0.0
        
        # Title match (highest weight)
        if codex.title:
            title_lower = codex.title.lower()
            if query_lower in title_lower:
                score += 10.0
            for term in query_lower.split():
                if term in title_lower:
                    score += 5.0
        
        # Description match (medium weight)
        if codex.description:
            desc_lower = codex.description.lower()
            if query_lower in desc_lower:
                score += 5.0
            for term in query_lower.split():
                if term in desc_lower:
                    score += 2.0
        
        # Content match (lower weight)
        if codex.content:
            content_lower = codex.content.lower()
            if query_lower in content_lower:
                score += 2.0
            for term in query_lower.split():
                if term in content_lower:
                    score += 0.5
        
        # Featured boost
        if codex.is_featured:
            score += 1.0
        
        # Purchase count boost (popularity)
        score += codex.purchase_count * 0.1
        
        return score
    
    def _get_matched_fields(self, codex: Codex, query: str) -> List[str]:
        """Get matched fields"""
        query_lower = query.lower()
        matched = []
        
        if codex.title and query_lower in codex.title.lower():
            matched.append("title")
        if codex.description and query_lower in codex.description.lower():
            matched.append("description")
        if codex.content and query_lower in codex.content.lower():
            matched.append("content")
        
        return matched
    
    def _calculate_remembrance_score(self, codex: Codex, query: str) -> float:
        """Calculate remembrance-specific score"""
        base_score = self._calculate_relevance(codex, query)
        
        # Boost for remembrance integration
        if codex.remembrance_integration:
            base_score *= 1.2
        
        # Boost for constitutional compliance
        if codex.constitutional_compliance:
            base_score *= 1.1
        
        return base_score
    
    def _identify_pattern_type(self, codex: Codex) -> str:
        """Identify pattern type from codex"""
        title_lower = codex.title.lower()
        
        if "trading" in title_lower or "forex" in title_lower:
            return "trading"
        elif "aura" in title_lower or "game" in title_lower:
            return "aura_academy"
        elif "remembrance" in title_lower or "infrastructure" in title_lower:
            return "remembrance"
        elif "constitutional" in title_lower or "format" in title_lower:
            return "constitutional"
        else:
            return "general"

# Initialize service
search_service = SearchService()

