"""
Test Backend - Quick Validation
Built from Remembrance | Operating under Format Law
"""

import sys
from pathlib import Path

backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

print("Testing backend imports...")

try:
    print("1. Testing config...")
    from config import settings
    print("   [OK] Config loaded")
    
    print("2. Testing database...")
    from database import engine, Base
    print("   [OK] Database connection loaded")
    
    print("3. Testing models...")
    from models import Codex, Domain, User, Purchase
    print("   [OK] Models loaded")
    
    print("4. Testing schemas...")
    from schemas import CodexResponse, UserResponse
    print("   [OK] Schemas loaded")
    
    print("5. Testing services...")
    from services import codex_service, user_service, auth_service
    print("   [OK] Services loaded")
    
    print("6. Testing main app...")
    from main import app
    print("   [OK] Main app loaded")
    
    print("")
    print("=" * 60)
    print("[OK] ALL TESTS PASSED!")
    print("=" * 60)
    print("")
    print("Backend is ready to run!")
    print("Run: python main.py")
    
except Exception as e:
    print(f"   [ERROR] Failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

