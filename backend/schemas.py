"""
Truth Drop Platform - Pydantic Schemas
Built from Remembrance | Operating under Format Law
"""

from pydantic import BaseModel, EmailStr, Field, validator
from typing import List, Optional
from datetime import datetime

# ============================================================================
# CODEX SCHEMAS
# ============================================================================

class CodexBase(BaseModel):
    """Base codex schema"""
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    domain_id: Optional[int] = None
    tag_ids: Optional[List[int]] = []
    price: Optional[float] = Field(None, ge=0)
    currency: str = Field(default="USD", max_length=3)
    format_law_version: str = Field(default="v1.3", max_length=10)
    constitutional_compliance: bool = Field(default=True)
    remembrance_integration: bool = Field(default=True)
    version: str = Field(default="1.0.0", max_length=20)
    is_active: bool = Field(default=True)
    is_featured: bool = Field(default=False)

class CodexCreate(CodexBase):
    """Schema for creating codex"""
    content: Optional[str] = None
    slug: Optional[str] = None

class CodexUpdate(BaseModel):
    """Schema for updating codex"""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    domain_id: Optional[int] = None
    tag_ids: Optional[List[int]] = None
    price: Optional[float] = Field(None, ge=0)
    content: Optional[str] = None
    is_active: Optional[bool] = None
    is_featured: Optional[bool] = None

class CodexResponse(CodexBase):
    """Schema for codex response"""
    id: int
    slug: str
    view_count: int
    purchase_count: int
    download_count: int
    domain: Optional["DomainResponse"] = None
    tags: List["TagResponse"] = []
    created_at: datetime
    updated_at: Optional[datetime] = None
    published_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# ============================================================================
# DOMAIN SCHEMAS
# ============================================================================

class DomainBase(BaseModel):
    """Base domain schema"""
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")
    is_active: bool = Field(default=True)
    sort_order: int = Field(default=0)

class DomainCreate(DomainBase):
    """Schema for creating domain"""
    slug: Optional[str] = None

class DomainResponse(DomainBase):
    """Schema for domain response"""
    id: int
    slug: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# ============================================================================
# TAG SCHEMAS
# ============================================================================

class TagBase(BaseModel):
    """Base tag schema"""
    name: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = None
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")

class TagCreate(TagBase):
    """Schema for creating tag"""
    slug: Optional[str] = None

class TagResponse(TagBase):
    """Schema for tag response"""
    id: int
    slug: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# ============================================================================
# USER SCHEMAS
# ============================================================================

class UserBase(BaseModel):
    """Base user schema"""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=100)
    full_name: Optional[str] = Field(None, max_length=255)

class UserCreate(UserBase):
    """Schema for creating user"""
    password: str = Field(..., min_length=8, max_length=100)

class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr
    password: str

class UserResponse(UserBase):
    """Schema for user response"""
    id: int
    is_active: bool
    is_admin: bool
    is_verified: bool
    subscription_type: Optional[str] = None
    subscription_expires_at: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# ============================================================================
# PURCHASE SCHEMAS
# ============================================================================

class PurchaseBase(BaseModel):
    """Base purchase schema"""
    amount: float = Field(..., ge=0)
    currency: str = Field(default="USD", max_length=3)
    purchase_type: str = Field(..., pattern="^(individual|bundle|subscription)$")

class PurchaseCreate(PurchaseBase):
    """Schema for creating purchase"""
    codex_id: Optional[int] = None
    codex_ids: Optional[List[int]] = []  # For bundles

class PurchaseResponse(PurchaseBase):
    """Schema for purchase response"""
    id: int
    user_id: int
    codex_id: Optional[int] = None
    stripe_payment_intent_id: Optional[str] = None
    stripe_charge_id: Optional[str] = None
    payment_status: str
    created_at: datetime
    completed_at: Optional[datetime] = None
    codex: Optional[CodexResponse] = None
    
    class Config:
        from_attributes = True

# ============================================================================
# SEARCH SCHEMAS
# ============================================================================

class SearchResult(BaseModel):
    """Schema for search result"""
    codex: CodexResponse
    relevance_score: Optional[float] = None
    matched_fields: Optional[List[str]] = []

class SearchResponse(BaseModel):
    """Schema for search response"""
    results: List[SearchResult]
    total: int
    query: str
    domain: Optional[str] = None

# ============================================================================
# ANALYTICS SCHEMAS
# ============================================================================

class AnalyticsResponse(BaseModel):
    """Schema for analytics response"""
    total_codexes: int
    total_users: int
    total_purchases: int
    total_revenue: float
    popular_codexes: List[CodexResponse]
    popular_domains: List[DomainResponse]
    recent_purchases: List[PurchaseResponse]

