"""
Truth Drop Platform - User Service
Built from Remembrance | Operating under Format Law
Constitutional Framework: Layer 6 - Psychological Constitutional Immunity
"""

from sqlalchemy.orm import Session
from typing import Optional
from models import User
from schemas import UserCreate
from services.auth_service import auth_service
import re

class UserService:
    """User service - Constitutional Framework: Layer 6"""
    
    async def create_user(
        self,
        db: Session,
        user_data: UserCreate
    ) -> User:
        """
        Create new user
        Constitutional Framework: Layer 6 - Psychological Constitutional Immunity
        """
        # Validate email
        existing_user = db.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            raise ValueError("Email already registered")
        
        # Validate username
        existing_username = db.query(User).filter(User.username == user_data.username).first()
        if existing_username:
            raise ValueError("Username already taken")
        
        # Validate username format
        if not re.match(r'^[a-zA-Z0-9_-]+$', user_data.username):
            raise ValueError("Username can only contain letters, numbers, hyphens, and underscores")
        
        # Hash password
        hashed_password = auth_service.hash_password(user_data.password)
        
        # Create user
        user = User(
            email=user_data.email,
            username=user_data.username,
            full_name=user_data.full_name,
            hashed_password=hashed_password,
            is_active=True,
            is_admin=False,
            is_verified=False
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user
    
    async def get_user(self, db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    async def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    async def update_user(self, db: Session, user_id: int, **kwargs) -> Optional[User]:
        """Update user"""
        user = await self.get_user(db, user_id)
        if not user:
            return None
        
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        
        db.commit()
        db.refresh(user)
        
        return user

# Initialize service
user_service = UserService()

