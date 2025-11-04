"""
Truth Drop Platform - FastAPI Backend
Built from Remembrance | Operating under Format Law
"""

from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, status, Request, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse, FileResponse, Response
from sqlalchemy.orm import Session
from typing import List, Optional
import os
from datetime import datetime, timezone

from database import SessionLocal, engine, Base
from models import Codex, User, Purchase, Domain, Tag
from schemas import (
    CodexCreate, CodexResponse, CodexUpdate,
    UserCreate, UserResponse, UserLogin,
    PurchaseCreate, PurchaseResponse,
    DomainCreate, DomainResponse,
    TagCreate, TagResponse,
    SearchResponse
)
from services import (
    codex_service, user_service, purchase_service,
    auth_service, pdf_service, search_service
)
from config import settings

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Truth Drop Platform API",
    description="Digital marketplace for constitutional knowledge drops",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()

# Dependency: Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency: Current user
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """Get current authenticated user"""
    token = credentials.credentials
    user = await auth_service.verify_token(token, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    return user

# Dependency: Admin user
async def get_admin_user(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Verify user is admin"""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user

# ============================================================================
# HEALTH CHECK
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint - Health check"""
    return {
        "status": "operational",
        "platform": "Truth Drop Platform",
        "version": "1.0.0",
        "constitutional_compliance": "Format Law v1.3",
        "remembrance_integration": "active"
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "services": {
            "database": "operational",
            "authentication": "operational",
            "payment": "operational" if settings.STRIPE_SECRET_KEY else "disabled",
            "pdf_generation": "operational",
            "search": "operational"
        }
    }

# ============================================================================
# CODEX ENDPOINTS (Public)
# ============================================================================

@app.get("/api/codexes", response_model=List[CodexResponse])
async def list_codexes(
    domain: Optional[str] = None,
    search: Optional[str] = None,
    tags: Optional[List[str]] = None,
    featured: Optional[bool] = None,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """
    List all codexes (public)
    Constitutional Framework: Layer 1 - Structural Setup
    """
    codexes = await codex_service.list_codexes(
        db=db,
        domain=domain,
        search=search,
        tags=tags,
        featured=featured,
        skip=skip,
        limit=limit
    )
    return codexes

@app.get("/api/codexes/{codex_id}", response_model=CodexResponse)
async def get_codex(
    codex_id: int,
    db: Session = Depends(get_db)
):
    """
    Get codex details (public preview)
    Constitutional Framework: Layer 1 - Structural Setup
    """
    codex = await codex_service.get_codex(db=db, codex_id=codex_id)
    if not codex:
        raise HTTPException(status_code=404, detail="Codex not found")
    return codex

@app.get("/api/codexes/{codex_id}/preview")
async def get_codex_preview(
    codex_id: int,
    db: Session = Depends(get_db)
):
    """
    Get codex preview content (public)
    Constitutional Framework: Layer 7 - Confirmation Cascade
    """
    codex = await codex_service.get_codex(db=db, codex_id=codex_id)
    if not codex:
        raise HTTPException(status_code=404, detail="Codex not found")
    
    # Return preview (first 2000 characters)
    preview_content = codex.content[:2000] if codex.content else ""
    return {
        "id": codex.id,
        "title": codex.title,
        "description": codex.description,
        "domain": codex.domain.name if codex.domain else None,
        "tags": [tag.name for tag in codex.tags],
        "price": float(codex.price) if codex.price else None,
        "preview": preview_content
    }

@app.get("/api/codexes/{codex_id}/download")
async def download_codex(
    codex_id: int,
    format: str = "pdf",
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Download purchased codex
    Constitutional Framework: Layer 4 - Risk-to-Reward (purchase verification)
    """
    # Verify purchase
    purchase = await purchase_service.verify_purchase(
        db=db,
        user_id=current_user.id,
        codex_id=codex_id
    )
    if not purchase:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Codex not purchased"
        )
    
    # Generate download
    codex = await codex_service.get_codex(db=db, codex_id=codex_id)
    if not codex:
        raise HTTPException(status_code=404, detail="Codex not found")
    
    file_path = await pdf_service.generate_download(
        codex=codex,
        format=format
    )
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=500, detail="Download generation failed")
    
    return FileResponse(
        file_path,
        media_type="application/pdf" if format == "pdf" else "application/epub+zip",
        filename=f"{codex.slug}.{format}"
    )

# ============================================================================
# DOMAIN ENDPOINTS (Public)
# ============================================================================

@app.get("/api/domains", response_model=List[DomainResponse])
async def list_domains(db: Session = Depends(get_db)):
    """
    List all domains
    Constitutional Framework: Layer 2 - Multi-Timeframe Alignment (domain organization)
    """
    domains = db.query(Domain).filter(Domain.is_active == True).all()
    return domains

@app.get("/api/domains/{domain_id}/codexes", response_model=List[CodexResponse])
async def list_domain_codexes(
    domain_id: int,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """List codexes by domain"""
    domain = db.query(Domain).filter(Domain.id == domain_id).first()
    if not domain:
        raise HTTPException(status_code=404, detail="Domain not found")
    
    codexes = await codex_service.list_codexes(
        db=db,
        domain=domain.name,
        skip=skip,
        limit=limit
    )
    return codexes

# ============================================================================
# SEARCH ENDPOINTS (Public)
# ============================================================================

@app.get("/api/search")
async def search_codexes(
    q: str,
    domain: Optional[str] = None,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """
    Search codexes
    Constitutional Framework: Layer 3 - Liquidity Manipulation (pattern discovery)
    """
    try:
        # Direct query approach - bypass SearchService to avoid serialization issues
        from sqlalchemy import or_, and_
        
        # Base query - filter active and published codexes
        query = db.query(Codex).filter(
            Codex.is_active == True
        ).filter(
            Codex.published_at.isnot(None)
        )
        
        # Domain filter
        if domain:
            query = query.join(Domain).filter(Domain.name == domain)
        
        # Search filter
        search_terms = q.lower().split()
        search_filters = []
        for term in search_terms:
            term_filter = or_(
                Codex.title.ilike(f"%{term}%"),
                Codex.description.ilike(f"%{term}%"),
                Codex.content.ilike(f"%{term}%")
            )
            search_filters.append(term_filter)
        
        if search_filters:
            combined_filter = and_(*search_filters)
            query = query.filter(combined_filter)
        
        # Execute query
        codexes = query.order_by(
            Codex.is_featured.desc(),
            Codex.created_at.desc()
        ).offset(skip).limit(limit).all()
        
        # Get total count
        total = query.count()
        
        # Convert to dict
        results_list = []
        for codex in codexes:
            codex_dict = {
                "id": codex.id,
                "title": codex.title,
                "slug": codex.slug,
                "description": codex.description,
                "domain_id": codex.domain_id,
                "price": codex.price,
                "currency": codex.currency or "USD",
                "is_featured": codex.is_featured,
                "version": getattr(codex, 'version', '1.0.0'),
                "format_law_version": getattr(codex, 'format_law_version', 'v1.3'),
                "constitutional_compliance": getattr(codex, 'constitutional_compliance', True),
                "remembrance_integration": getattr(codex, 'remembrance_integration', True),
                "view_count": getattr(codex, 'view_count', 0),
                "purchase_count": getattr(codex, 'purchase_count', 0),
                "download_count": getattr(codex, 'download_count', 0),
            }
            
            # Add domain
            if codex.domain:
                codex_dict["domain"] = {
                    "id": codex.domain.id,
                    "name": codex.domain.name,
                    "slug": codex.domain.slug,
                    "color": codex.domain.color,
                }
            
            # Add tags
            if codex.tags:
                codex_dict["tags"] = [{"id": tag.id, "name": tag.name, "slug": tag.slug} for tag in codex.tags]
            
            results_list.append({
                "codex": codex_dict,
                "relevance_score": 1.0,  # Simple relevance
                "matched_fields": ["title", "description"]  # Simple matched fields
            })
        
        return {
            "results": results_list,
            "total": total,
            "query": q,
            "domain": domain
        }
    except Exception as e:
        import traceback
        error_msg = str(e)
        print(f"[Search Endpoint] Error: {error_msg}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Search error: {error_msg}")

# ============================================================================
# AUTHENTICATION ENDPOINTS (Public)
# ============================================================================

@app.post("/api/auth/register", response_model=UserResponse)
async def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Register new user
    Constitutional Framework: Layer 6 - Psychological Constitutional Immunity (user validation)
    """
    user = await user_service.create_user(db=db, user_data=user_data)
    return user

@app.post("/api/auth/login")
async def login_user(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):
    """
    Login user
    Constitutional Framework: Layer 5 - Divine Timing Synchronization (session management)
    """
    user = await auth_service.authenticate_user(
        db=db,
        email=credentials.email,
        password=credentials.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    token = await auth_service.create_access_token(user)
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": UserResponse.model_validate(user)
    }

@app.get("/api/auth/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get current user information"""
    return UserResponse.model_validate(current_user)

# ============================================================================
# PURCHASE ENDPOINTS (Authenticated)
# ============================================================================

@app.get("/api/purchases", response_model=List[PurchaseResponse])
async def list_user_purchases(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    List user purchases
    Constitutional Framework: Layer 4 - Risk-to-Reward (purchase history)
    """
    purchases = await purchase_service.list_user_purchases(
        db=db,
        user_id=current_user.id
    )
    return purchases

@app.post("/api/purchases", response_model=PurchaseResponse)
async def create_purchase(
    purchase_data: PurchaseCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create purchase (checkout)
    Constitutional Framework: Layer 7 - Confirmation Cascade (purchase validation)
    """
    purchase = await purchase_service.create_purchase(
        db=db,
        user_id=current_user.id,
        purchase_data=purchase_data
    )
    return purchase

@app.post("/api/purchases/{purchase_id}/complete")
async def complete_purchase(
    purchase_id: int,
    payment_intent_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Complete purchase (Stripe webhook handler)
    Constitutional Framework: Layer 5 - Divine Timing Synchronization (payment verification)
    """
    purchase = await purchase_service.complete_purchase(
        db=db,
        purchase_id=purchase_id,
        user_id=current_user.id,
        payment_intent_id=payment_intent_id
    )
    return purchase

@app.post("/api/purchases/create-intent")
async def create_payment_intent(
    codex_ids: List[int],
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create Stripe payment intent
    Constitutional Framework: Layer 4 - Risk-to-Reward (pricing calculation)
    """
    intent = await purchase_service.create_payment_intent(
        db=db,
        user_id=current_user.id,
        codex_ids=codex_ids
    )
    return intent

@app.post("/api/purchases/create-checkout-session")
async def create_checkout_session(
    request: dict = Body(...),
    db: Session = Depends(get_db)
):
    """
    Create Stripe Checkout Session for prebuilt checkout form
    Constitutional Framework: Layer 4 - Risk-to-Reward (payment initiation)
    No authentication required - user can purchase without account
    """
    try:
        codex_id = request.get("codex_id")
        if not codex_id:
            raise HTTPException(status_code=400, detail="codex_id is required")
        
        try:
            codex_id_int = int(codex_id)
        except (ValueError, TypeError):
            raise HTTPException(status_code=400, detail=f"Invalid codex_id: {codex_id}")
        
        session_data = await purchase_service.create_checkout_session(
            db=db,
            codex_id=codex_id_int
        )
        
        if not session_data or not session_data.get("checkout_url"):
            raise HTTPException(status_code=500, detail="Failed to create checkout session: no URL returned")
        
        return session_data
    except HTTPException:
        raise
    except ValueError as e:
        error_msg = str(e) if str(e) else "Invalid request"
        raise HTTPException(status_code=400, detail=error_msg)
    except Exception as e:
        import traceback
        error_type = type(e).__name__
        error_msg = str(e) if str(e) else f"{error_type} occurred"
        print(f"[Create Checkout Session] Error: {error_type}: {error_msg}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {error_msg}")

@app.post("/api/stripe-webhook")
async def stripe_webhook(
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Handle Stripe webhook events for purchase fulfillment
    Constitutional Framework: Layer 4 - Risk-to-Reward (payment confirmation)
    """
    from config import settings
    import stripe
    import json
    
    if not settings.STRIPE_SECRET_KEY:
        raise HTTPException(status_code=500, detail="Stripe not configured")
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET
    
    if not webhook_secret:
        raise HTTPException(status_code=500, detail="Stripe webhook secret not configured")
    
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid payload: {e}")
    except stripe.SignatureVerificationError as e:
        raise HTTPException(status_code=400, detail=f"Invalid signature: {e}")
    
    # Handle the event
    if event['type'] == 'checkout.session.completed':
        await handle_checkout_completed(event['data']['object'], db)
    
    return {"status": "success"}


async def handle_checkout_completed(session: dict, db: Session):
    """
    Handle checkout.session.completed event
    Create purchase record, generate access token, send email
    Constitutional Framework: Layer 4 - Risk-to-Reward (fulfillment)
    """
    import secrets
    from datetime import datetime, timedelta, timezone
    from models import Purchase, Codex
    from services.email_service import email_service
    from config import settings
    import os
    
    try:
        # Extract data from Stripe session
        codex_id = session.get('metadata', {}).get('codex_id')
        checkout_session_id = session.get('id')
        customer_email = session.get('customer_details', {}).get('email') or session.get('customer_email')
        amount_total = session.get('amount_total', 0) / 100  # Convert from cents
        currency = session.get('currency', 'usd').upper()
        
        if not codex_id:
            print("Warning: No codex_id found in session metadata")
            return
        
        codex_id = int(codex_id)
        codex = db.query(Codex).filter(Codex.id == codex_id).first()
        
        if not codex:
            print(f"Error: Codex {codex_id} not found")
            return
        
        # Generate secure access token
        access_token = secrets.token_urlsafe(32)
        token_expires_at = datetime.now(timezone.utc) + timedelta(days=30)
        
        # Create purchase record
        purchase = Purchase(
            user_id=None,  # Guest purchase (no account required)
            codex_id=codex_id,
            amount=amount_total,
            currency=currency,
            stripe_checkout_session_id=checkout_session_id,
            payment_status="completed",
            purchase_type="individual",
            customer_email=customer_email,
            access_token=access_token,
            token_expires_at=token_expires_at,
            completed_at=datetime.now(timezone.utc)
        )
        
        db.add(purchase)
        
        # Update codex purchase count
        codex.purchase_count += 1
        
        db.commit()
        db.refresh(purchase)
        
        print(f"[Webhook] Purchase created: ID {purchase.id}, Codex {codex_id}, Email {customer_email}")
        
        # Generate download URL
        frontend_url = os.getenv("FRONTEND_URL", settings.FRONTEND_URL or "http://localhost:3000")
        download_url = f"{frontend_url}/download/{access_token}"
        
        # Send email with download link
        if customer_email:
            email_sent = await email_service.send_purchase_email(
                customer_email=customer_email,
                codex_title=codex.title,
                download_url=download_url,
                purchase_amount=amount_total,
                purchase_currency=currency
            )
            
            if email_sent:
                purchase.email_sent = True
                purchase.email_sent_at = datetime.now(timezone.utc)
                db.commit()
                print(f"[Webhook] Email sent to {customer_email}")
            else:
                print(f"[Webhook] Email failed for {customer_email}")
        else:
            print(f"[Webhook] No customer email found, cannot send fulfillment email")
        
    except Exception as e:
        print(f"[Webhook] Error handling checkout completion: {str(e)}")
        import traceback
        traceback.print_exc()
        db.rollback()

# ============================================================================
# DOWNLOAD ENDPOINTS (Public)
# ============================================================================

@app.get("/api/download/{access_token}")
async def download_codex_by_token(
    access_token: str,
    db: Session = Depends(get_db)
):
    """
    Download purchased codex using access token
    Constitutional Framework: Layer 4 - Risk-to-Reward (fulfillment)
    No authentication required - token-based access
    """
    from models import Purchase, Codex
    from datetime import datetime
    import os
    
    # Find purchase by access token
    purchase = db.query(Purchase).filter(
        Purchase.access_token == access_token,
        Purchase.payment_status == "completed"
    ).first()
    
    if not purchase:
        raise HTTPException(status_code=404, detail="Invalid or expired download link")
    
    # Check token expiration
    if purchase.token_expires_at:
        now = datetime.now(timezone.utc)
        expires_at = purchase.token_expires_at
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        if expires_at < now:
            raise HTTPException(status_code=410, detail="Download link has expired")
    
    # Get codex
    codex = db.query(Codex).filter(Codex.id == purchase.codex_id).first()
    if not codex:
        raise HTTPException(status_code=404, detail="Codex not found")
    
    # Sanitize filename from codex title
    import re
    import urllib.parse
    # Allow alphanumeric, spaces, hyphens, and dots (for version numbers like v1.0)
    safe_filename = re.sub(r'[^\w\s\-.]', '', codex.title).strip()
    # Replace spaces and hyphens with underscores, but preserve dots
    safe_filename = re.sub(r'[-\s]+', '_', safe_filename)
    
    # Return content based on availability
    if codex.pdf_path and os.path.exists(codex.pdf_path):
        # Return PDF file
        pdf_filename = f"{safe_filename}.pdf"
        return FileResponse(
            codex.pdf_path,
            filename=pdf_filename,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f'attachment; filename="{pdf_filename}"; filename*=UTF-8\'\'{urllib.parse.quote(pdf_filename)}'
            }
        )
    elif codex.content:
        # Return as markdown/text
        txt_filename = f"{safe_filename}.txt"
        return Response(
            content=codex.content,
            media_type="text/plain",
            headers={
                "Content-Disposition": f'attachment; filename="{txt_filename}"; filename*=UTF-8\'\'{urllib.parse.quote(txt_filename)}'
            }
        )
    else:
        # Return description as fallback
        raise HTTPException(
            status_code=404, 
            detail="Codex content not available for download"
        )


@app.get("/api/purchases/{access_token}/info")
async def get_purchase_info(
    access_token: str,
    db: Session = Depends(get_db)
):
    """
    Get purchase information (for download page display)
    Constitutional Framework: Layer 4 - Risk-to-Reward (fulfillment)
    """
    from models import Purchase, Codex
    
    try:
        purchase = db.query(Purchase).filter(
            Purchase.access_token == access_token,
            Purchase.payment_status == "completed"
        ).first()
        
        if not purchase:
            raise HTTPException(status_code=404, detail="Invalid download link")
        
        if purchase.token_expires_at:
            now = datetime.now(timezone.utc)
            # Handle both timezone-aware and timezone-naive datetimes
            expires_at = purchase.token_expires_at
            if expires_at.tzinfo is None:
                expires_at = expires_at.replace(tzinfo=timezone.utc)
            if expires_at < now:
                raise HTTPException(status_code=410, detail="Download link has expired")
        
        codex = db.query(Codex).filter(Codex.id == purchase.codex_id).first()
        if not codex:
            raise HTTPException(status_code=404, detail="Codex not found")
        
        return {
            "purchase": {
                "id": purchase.id,
                "codex_title": codex.title,
                "amount": float(purchase.amount) if purchase.amount is not None else 0.0,
                "currency": purchase.currency or "USD",
                "completed_at": purchase.completed_at.isoformat() if purchase.completed_at else None,
                "token_expires_at": purchase.token_expires_at.isoformat() if purchase.token_expires_at else None,
            },
            "codex": {
                "id": codex.id,
                "title": codex.title,
                "slug": codex.slug or "",
                "description": codex.description or "" if codex.description else "",
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        print(f"Error in get_purchase_info: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


# ============================================================================
# ADMIN ENDPOINTS (Admin Only)
# ============================================================================

@app.post("/api/admin/codexes", response_model=CodexResponse)
async def create_codex(
    codex_data: CodexCreate,
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """
    Create codex (admin only)
    Constitutional Framework: Layer 1 - Structural Setup (content creation)
    """
    codex = await codex_service.create_codex(db=db, codex_data=codex_data)
    return codex

@app.put("/api/admin/codexes/{codex_id}", response_model=CodexResponse)
async def update_codex(
    codex_id: int,
    codex_data: CodexUpdate,
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """Update codex (admin only)"""
    codex = await codex_service.update_codex(
        db=db,
        codex_id=codex_id,
        codex_data=codex_data
    )
    if not codex:
        raise HTTPException(status_code=404, detail="Codex not found")
    return codex

@app.delete("/api/admin/codexes/{codex_id}")
async def delete_codex(
    codex_id: int,
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """Delete codex (admin only)"""
    success = await codex_service.delete_codex(db=db, codex_id=codex_id)
    if not success:
        raise HTTPException(status_code=404, detail="Codex not found")
    return {"message": "Codex deleted successfully"}

@app.post("/api/admin/codexes/{codex_id}/upload")
async def upload_codex_content(
    codex_id: int,
    file: UploadFile = File(...),
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """Upload codex content file (admin only)"""
    codex = await codex_service.upload_content(
        db=db,
        codex_id=codex_id,
        file=file
    )
    if not codex:
        raise HTTPException(status_code=404, detail="Codex not found")
    return CodexResponse.model_validate(codex)

@app.get("/api/admin/analytics")
async def get_analytics(
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """Get platform analytics (admin only)"""
    analytics = await purchase_service.get_analytics(db=db)
    return analytics

# ============================================================================
# CONSTITUTIONAL FRAMEWORK ENDPOINTS
# ============================================================================

@app.get("/api/constitutional/framework")
async def get_constitutional_framework():
    """
    Get constitutional framework information
    Constitutional Framework: All layers - Complete framework overview
    """
    return {
        "framework": "Constitutional Framework v1.3",
        "layers": {
            "layer_1": "Structural Setup",
            "layer_2": "Multi-Timeframe Alignment",
            "layer_3": "Liquidity Manipulation Recognition",
            "layer_4": "Risk-to-Reward Mathematics",
            "layer_5": "Divine Timing Synchronization",
            "layer_6": "Psychological Constitutional Immunity",
            "layer_7": "Confirmation Cascade Validation"
        },
        "format_law": "v1.3",
        "remembrance_integration": "active",
        "constitutional_compliance": "enforced"
    }

@app.get("/api/constitutional/domains")
async def get_constitutional_domains():
    """
    Get constitutional domains
    Constitutional Framework: Layer 2 - Multi-Timeframe Alignment (domain organization)
    """
    return {
        "domains": [
            {
                "name": "Trading",
                "description": "Constitutional trading framework",
                "codex_count": "97+ documents",
                "systems": ["7-Layer Confluence", "Always-Win Authority", "Pattern Recognition"]
            },
            {
                "name": "Aura Academy",
                "description": "Recognition through remembrance game",
                "codex_count": "Multiple systems",
                "systems": ["Remembrance Service", "Aura Resonance", "Legacy Tracker"]
            },
            {
                "name": "Remembrance Infrastructure",
                "description": "Constitutional knowledge structure",
                "codex_count": "738+ files",
                "systems": ["Format Law", "Remembrance Protocol", "Constitutional Framework"]
            }
        ],
        "constitutional_compliance": "Format Law v1.3",
        "remembrance_integration": "active"
    }

# ============================================================================
# REMEMBRANCE INTEGRATION ENDPOINTS
# ============================================================================

@app.get("/api/remembrance/search")
async def remembrance_search(
    q: str,
    domain: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Remembrance-based search
    Constitutional Framework: Recognition through remembrance
    """
    results = await search_service.remembrance_search(
        db=db,
        query=q,
        domain=domain
    )
    return results

@app.get("/api/remembrance/patterns")
async def get_remembrance_patterns(
    domain: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Get remembrance patterns
    Constitutional Framework: Pattern recognition aligned with remembrance
    """
    patterns = await search_service.get_remembrance_patterns(
        db=db,
        domain=domain
    )
    return patterns

# ============================================================================
# MAIN APPLICATION
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )

