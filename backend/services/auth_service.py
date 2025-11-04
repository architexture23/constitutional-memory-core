"""
Truth Drop Platform - Authentication Service
Built from Remembrance | Operating under Format Law
Constitutional Framework: Layer 6 - Psychological Constitutional Immunity
"""

from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from models import User
from config import settings

class AuthService:
    """Authentication service - Constitutional Framework: Layer 6"""
    
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.secret_key = settings.SECRET_KEY
        self.algorithm = settings.ALGORITHM
        self.access_token_expire_minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify password"""
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def hash_password(self, password: str) -> str:
        """Hash password"""
        return self.pwd_context.hash(password)
    
    async def authenticate_user(
        self,
        db: Session,
        email: str,
        password: str
    ) -> Optional[User]:
        """
        Authenticate user
        Constitutional Framework: Layer 6 - Psychological Constitutional Immunity
        """
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        
        if not self.verify_password(password, user.hashed_password):
            return None
        
        if not user.is_active:
            return None
        
        # Update last login
        user.last_login = datetime.utcnow()
        db.commit()
        
        return user
    
    async def create_access_token(self, user: User) -> str:
        """Create JWT access token"""
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        payload = {
            "sub": str(user.id),
            "email": user.email,
            "is_admin": user.is_admin,
            "exp": expire
        }
        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token
    
    async def verify_token(
        self,
        token: str,
        db: Session
    ) -> Optional[User]:
        """Verify JWT token and return user"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            user_id: int = int(payload.get("sub"))
            if user_id is None:
                return None
        except JWTError:
            return None
        
        user = db.query(User).filter(User.id == user_id).first()
        if not user or not user.is_active:
            return None
        
        return user

# Initialize service
auth_service = AuthService()

