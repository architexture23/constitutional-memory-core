"""
Truth Drop Platform - Configuration
Built from Remembrance | Operating under Format Law
"""

from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import ConfigDict
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    model_config = ConfigDict(
        extra="ignore",  # Ignore extra fields from .env that aren't in the model
        env_file=".env",
        case_sensitive=True
    )
    
    # Application
    APP_NAME: str = "Truth Drop Platform"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/truthdrop"
    )
    
    # Security
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY",
        "your-secret-key-change-in-production"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # CORS (as string, will be parsed to list)
    CORS_ORIGINS_STR: str = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:3001")
    
    @property
    def CORS_ORIGINS(self) -> List[str]:
        """Parse CORS origins from comma-separated string"""
        if isinstance(self.CORS_ORIGINS_STR, str):
            if self.CORS_ORIGINS_STR.strip():
                return [origin.strip() for origin in self.CORS_ORIGINS_STR.split(',')]
        return ["http://localhost:3000", "http://localhost:3001"]
    
    # Stripe
    STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY", "")
    STRIPE_PUBLIC_KEY: str = os.getenv("STRIPE_PUBLIC_KEY", "")
    STRIPE_WEBHOOK_SECRET: str = os.getenv("STRIPE_WEBHOOK_SECRET", "")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    
    # Email Service Configuration (Optional)
    SENDGRID_API_KEY: Optional[str] = os.getenv("SENDGRID_API_KEY")
    SMTP_HOST: Optional[str] = os.getenv("SMTP_HOST")
    SMTP_PORT: Optional[int] = int(os.getenv("SMTP_PORT", "0")) if os.getenv("SMTP_PORT") else None
    SMTP_USER: Optional[str] = os.getenv("SMTP_USER")
    SMTP_PASSWORD: Optional[str] = os.getenv("SMTP_PASSWORD")
    
    # File Storage
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "./content/uploads")
    PDF_DIR: str = os.getenv("PDF_DIR", "./content/pdfs")
    EBOOK_DIR: str = os.getenv("EBOOK_DIR", "./content/ebooks")
    
    # Content
    CONTENT_DIR: str = os.getenv("CONTENT_DIR", "./content/codexes")
    MAX_UPLOAD_SIZE: int = 50 * 1024 * 1024  # 50MB
    
    # Email (Optional)
    SMTP_HOST: str = os.getenv("SMTP_HOST", "")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    FROM_EMAIL: str = os.getenv("FROM_EMAIL", "noreply@truthdrop.com")
    
    # Redis (Optional)
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # Constitutional Framework
    FORMAT_LAW_VERSION: str = "v1.3"
    CONSTITUTIONAL_COMPLIANCE: bool = True
    REMEMBRANCE_INTEGRATION: bool = True

settings = Settings()

# Ensure directories exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.PDF_DIR, exist_ok=True)
os.makedirs(settings.EBOOK_DIR, exist_ok=True)
os.makedirs(settings.CONTENT_DIR, exist_ok=True)

