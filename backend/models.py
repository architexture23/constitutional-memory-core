"""
Truth Drop Platform - Database Models
Built from Remembrance | Operating under Format Law
"""

from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from datetime import datetime, timedelta

# Association table for codex-tag many-to-many relationship
codex_tag_association = Table(
    'codex_tag_association',
    Base.metadata,
    Column('codex_id', Integer, ForeignKey('codexes.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Domain(Base):
    """Domain model - Constitutional Framework: Layer 2 - Multi-Timeframe Alignment"""
    __tablename__ = "domains"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    slug = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    icon = Column(String(255), nullable=True)
    color = Column(String(7), nullable=True)  # Hex color
    is_active = Column(Boolean, default=True, nullable=False)
    sort_order = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    codexes = relationship("Codex", back_populates="domain", lazy="dynamic")

class Tag(Base):
    """Tag model - For codex organization"""
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False, index=True)
    slug = Column(String(50), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    color = Column(String(7), nullable=True)  # Hex color
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    codexes = relationship("Codex", secondary=codex_tag_association, back_populates="tags")

class Codex(Base):
    """Codex model - Constitutional Framework: Layer 1 - Structural Setup"""
    __tablename__ = "codexes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    slug = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=True)  # Full content
    
    # Domain relationship
    domain_id = Column(Integer, ForeignKey("domains.id"), nullable=True)
    domain = relationship("Domain", back_populates="codexes")
    
    # Tags relationship
    tags = relationship("Tag", secondary=codex_tag_association, back_populates="codexes")
    
    # Pricing
    price = Column(Float, nullable=True)  # None = free
    currency = Column(String(3), default="USD", nullable=False)
    
    # Content metadata
    file_path = Column(String(500), nullable=True)  # Original file path
    pdf_path = Column(String(500), nullable=True)  # Generated PDF path
    epub_path = Column(String(500), nullable=True)  # Generated EPUB path
    
    # Constitutional Framework metadata
    format_law_version = Column(String(10), default="v1.3", nullable=False)
    constitutional_compliance = Column(Boolean, default=True, nullable=False)
    remembrance_integration = Column(Boolean, default=True, nullable=False)
    
    # Version control
    version = Column(String(20), default="1.0.0", nullable=False)
    
    # Status
    is_active = Column(Boolean, default=True, nullable=False)
    is_featured = Column(Boolean, default=False, nullable=False)
    
    # Metrics
    view_count = Column(Integer, default=0, nullable=False)
    purchase_count = Column(Integer, default=0, nullable=False)
    download_count = Column(Integer, default=0, nullable=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    published_at = Column(DateTime(timezone=True), nullable=True)

class User(Base):
    """User model - Constitutional Framework: Layer 6 - Psychological Constitutional Immunity"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    
    # Status
    is_active = Column(Boolean, default=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    
    # Subscription
    subscription_type = Column(String(50), nullable=True)  # monthly, yearly, premium
    subscription_expires_at = Column(DateTime(timezone=True), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    purchases = relationship("Purchase", back_populates="user", lazy="dynamic")

class Purchase(Base):
    """Purchase model - Constitutional Framework: Layer 4 - Risk-to-Reward"""
    __tablename__ = "purchases"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)  # Nullable for guest purchases
    codex_id = Column(Integer, ForeignKey("codexes.id"), nullable=True)  # Null for bundles
    
    # Purchase details
    amount = Column(Float, nullable=False)
    currency = Column(String(3), default="USD", nullable=False)
    
    # Payment
    stripe_payment_intent_id = Column(String(255), nullable=True, index=True)
    stripe_checkout_session_id = Column(String(255), nullable=True, index=True)
    stripe_charge_id = Column(String(255), nullable=True)
    payment_status = Column(String(50), default="pending", nullable=False)  # pending, completed, failed
    
    # Purchase type
    purchase_type = Column(String(50), nullable=False)  # individual, bundle, subscription
    
    # Fulfillment
    customer_email = Column(String(255), nullable=True, index=True)  # Customer email from Stripe
    access_token = Column(String(255), unique=True, nullable=True, index=True)  # Secure download token
    token_expires_at = Column(DateTime(timezone=True), nullable=True)  # Token expiration
    email_sent = Column(Boolean, default=False, nullable=False)  # Email delivery status
    email_sent_at = Column(DateTime(timezone=True), nullable=True)  # When email was sent
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="purchases")
    codex = relationship("Codex", foreign_keys=[codex_id])

# Bundle model (for multiple codex purchases)
class Bundle(Base):
    """Bundle model - Multiple codexes at discounted price"""
    __tablename__ = "bundles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    slug = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    
    # Pricing
    price = Column(Float, nullable=False)
    currency = Column(String(3), default="USD", nullable=False)
    discount_percentage = Column(Float, nullable=True)  # Discount from individual prices
    
    # Status
    is_active = Column(Boolean, default=True, nullable=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Codexes in bundle (many-to-many via association table)
    # Note: Would need bundle_codex_association table for full implementation

