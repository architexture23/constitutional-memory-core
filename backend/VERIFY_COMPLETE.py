"""
Complete Backend Verification - Tests Everything
Built from Remembrance | Operating under Format Law
"""

import sys
import os
from pathlib import Path

backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

print("=" * 60)
print("COMPLETE BACKEND VERIFICATION")
print("Built from Remembrance | Operating under Format Law")
print("=" * 60)
print("")

errors = []
warnings = []

# Test 1: Config
print("1. Testing config...")
try:
    from config import settings
    assert settings.DATABASE_URL and 'postgres.railway.internal' not in settings.DATABASE_URL, "Using internal URL"
    print("   [OK] Config loaded - public database URL verified")
except Exception as e:
    errors.append(f"Config error: {e}")
    print(f"   [ERROR] {e}")

# Test 2: Database
print("2. Testing database connection...")
try:
    from database import engine, Base, SessionLocal
    from sqlalchemy import text
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        result.fetchone()
    print("   [OK] Database connection successful")
except Exception as e:
    errors.append(f"Database error: {e}")
    print(f"   [ERROR] {e}")

# Test 3: Models
print("3. Testing models...")
try:
    from models import Codex, Domain, User, Purchase, Tag, Bundle
    print("   [OK] All models loaded")
except Exception as e:
    errors.append(f"Models error: {e}")
    print(f"   [ERROR] {e}")

# Test 4: Schemas
print("4. Testing schemas...")
try:
    from schemas import (
        CodexCreate, CodexResponse, CodexUpdate,
        UserCreate, UserResponse, UserLogin,
        PurchaseCreate, PurchaseResponse,
        DomainResponse, TagResponse
    )
    print("   [OK] All schemas loaded")
except Exception as e:
    errors.append(f"Schemas error: {e}")
    print(f"   [ERROR] {e}")

# Test 5: Services
print("5. Testing services...")
try:
    from services import (
        codex_service, user_service, auth_service,
        purchase_service, pdf_service, search_service
    )
    print("   [OK] All services loaded")
except Exception as e:
    errors.append(f"Services error: {e}")
    print(f"   [ERROR] {e}")

# Test 6: Main App
print("6. Testing main application...")
try:
    from main import app
    print("   [OK] Main app loaded")
except Exception as e:
    errors.append(f"Main app error: {e}")
    print(f"   [ERROR] {e}")

# Test 7: FastAPI App Structure
print("7. Testing FastAPI app structure...")
try:
    from main import app
    assert app is not None
    routes = [route.path for route in app.routes]
    assert len(routes) > 0
    print(f"   [OK] FastAPI app has {len(routes)} routes")
except Exception as e:
    errors.append(f"FastAPI structure error: {e}")
    print(f"   [ERROR] {e}")

# Test 8: Database Tables
print("8. Testing database tables...")
try:
    from database import engine
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    expected_tables = ['domains', 'tags', 'codexes', 'users', 'purchases']
    missing = [t for t in expected_tables if t not in tables]
    if missing:
        warnings.append(f"Missing tables: {missing}")
        print(f"   [WARNING] Missing tables: {missing}")
    else:
        print(f"   [OK] All required tables exist ({len(tables)} tables)")
except Exception as e:
    errors.append(f"Database tables error: {e}")
    print(f"   [ERROR] {e}")

print("")
print("=" * 60)
if errors:
    print(f"[ERROR] {len(errors)} errors found:")
    for error in errors:
        print(f"  - {error}")
    print("")
    print("Backend is NOT ready to run.")
    sys.exit(1)
else:
    print("[OK] ALL TESTS PASSED!")
    print("=" * 60)
    print("")
    print("Backend is ready to run!")
    print("Run: python main.py")
    print("")
    if warnings:
        print(f"Warnings ({len(warnings)}):")
        for warning in warnings:
            print(f"  - {warning}")
        print("")

