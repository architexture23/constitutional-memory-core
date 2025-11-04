"""
Truth Drop Platform - Purchase Service
Built from Remembrance | Operating under Format Law
Constitutional Framework: Layer 4 - Risk-to-Reward Mathematics
"""

from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional, Dict
from datetime import datetime, timezone, timedelta
import os
from models import Purchase, User, Codex, Domain
from schemas import PurchaseCreate
from config import settings
import stripe

# Initialize Stripe if key is set
if settings.STRIPE_SECRET_KEY:
    stripe.api_key = settings.STRIPE_SECRET_KEY

class PurchaseService:
    """Purchase service - Constitutional Framework: Layer 4"""
    
    async def create_purchase(
        self,
        db: Session,
        user_id: int,
        purchase_data: PurchaseCreate
    ) -> Purchase:
        """
        Create purchase
        Constitutional Framework: Layer 4 - Risk-to-Reward Mathematics
        """
        # Calculate amount if not provided
        if purchase_data.amount is None:
            if purchase_data.codex_id:
                codex = db.query(Codex).filter(Codex.id == purchase_data.codex_id).first()
                amount = codex.price if codex and codex.price else 0.0
            elif purchase_data.codex_ids:
                codexes = db.query(Codex).filter(Codex.id.in_(purchase_data.codex_ids)).all()
                amount = sum(c.price for c in codexes if c.price)
            else:
                amount = 0.0
        else:
            amount = purchase_data.amount
        
        # Create purchase
        purchase = Purchase(
            user_id=user_id,
            codex_id=purchase_data.codex_id,
            amount=amount,
            currency=purchase_data.currency,
            purchase_type=purchase_data.purchase_type,
            payment_status="pending"
        )
        
        db.add(purchase)
        db.commit()
        db.refresh(purchase)
        
        return purchase
    
    async def create_payment_intent(
        self,
        db: Session,
        user_id: int,
        codex_ids: List[int]
    ) -> Dict:
        """Create Stripe payment intent"""
        if not settings.STRIPE_SECRET_KEY:
            raise ValueError("Stripe not configured")
        
        # Get codexes
        codexes = db.query(Codex).filter(Codex.id.in_(codex_ids)).all()
        total_amount = sum(c.price for c in codexes if c.price)
        
        # Create payment intent
        intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),  # Convert to cents
            currency="usd",
            metadata={
                "user_id": user_id,
                "codex_ids": ",".join(map(str, codex_ids))
            }
        )
        
        return {
            "client_secret": intent.client_secret,
            "payment_intent_id": intent.id,
            "amount": total_amount,
            "currency": "usd"
        }
    
    async def create_checkout_session(
        self,
        db: Session,
        codex_id: int,
        user_id: Optional[int] = None
    ) -> Dict:
        """
        Create Stripe Checkout Session for prebuilt checkout form
        Constitutional Framework: Layer 4 - Risk-to-Reward (payment initiation)
        """
        if not settings.STRIPE_SECRET_KEY:
            raise ValueError("Stripe not configured")
        
        # Ensure Stripe is initialized
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        # Get codex
        codex = db.query(Codex).filter(Codex.id == codex_id).first()
        if not codex:
            raise ValueError("Codex not found")
        
        # Build frontend URL from settings
        frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
        
        # Handle free codexes (price = 0 or 0.0) - bypass Stripe, create purchase directly
        # Check if price is None or 0 using float comparison
        if codex.price is None:
            raise ValueError("Codex has no valid price")
        
        # Allow free codexes - check if price is 0 or less (free)
        price_value = float(codex.price) if codex.price is not None else None
        if price_value is not None and price_value <= 0.0:
            import secrets
            from models import Purchase
            
            # Generate access token
            access_token = secrets.token_urlsafe(32)
            token_expires_at = datetime.now(timezone.utc) + timedelta(days=30)
            
            # Create purchase record directly (free purchase)
            purchase = Purchase(
                user_id=None,
                codex_id=codex.id,
                amount=0.0,
                currency=codex.currency or "USD",
                payment_status="completed",
                purchase_type="individual",
                access_token=access_token,
                token_expires_at=token_expires_at,
                completed_at=datetime.now(timezone.utc),
                stripe_checkout_session_id="free_purchase"
            )
            
            db.add(purchase)
            codex.purchase_count += 1
            db.commit()
            db.refresh(purchase)
            
            # Generate download URL
            download_url = f"{frontend_url}/download/{access_token}"
            
            return {
                "checkout_url": download_url,  # Redirect directly to download
                "session_id": f"free_{purchase.id}",
                "is_free": True
            }
        
        # Create checkout session for paid codexes
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': codex.title,
                                'description': (codex.description or f"Purchase {codex.title}")[:500],
                            },
                            'unit_amount': int(codex.price * 100),  # Convert to cents
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=f"{frontend_url}/purchase/success?session_id={{CHECKOUT_SESSION_ID}}",
                cancel_url=f"{frontend_url}/purchase/cancel",
                metadata={
                    "codex_id": str(codex.id),
                    "codex_slug": codex.slug,
                }
            )
            
            return {
                "checkout_url": checkout_session.url,
                "session_id": checkout_session.id
            }
        except stripe.StripeError as e:
            error_msg = getattr(e, 'user_message', None) or str(e) or "Unknown Stripe error"
            raise ValueError(f"Stripe error: {error_msg}")
    
    async def complete_purchase(
        self,
        db: Session,
        purchase_id: int,
        user_id: int,
        payment_intent_id: str
    ) -> Optional[Purchase]:
        """Complete purchase after payment"""
        purchase = db.query(Purchase).filter(
            Purchase.id == purchase_id,
            Purchase.user_id == user_id
        ).first()
        
        if not purchase:
            return None
        
        # Verify payment intent
        if settings.STRIPE_SECRET_KEY:
            try:
                intent = stripe.PaymentIntent.retrieve(payment_intent_id)
                if intent.status != "succeeded":
                    return None
            except stripe.StripeError:
                return None
        
        # Update purchase
        purchase.payment_status = "completed"
        purchase.stripe_payment_intent_id = payment_intent_id
        purchase.completed_at = datetime.now(timezone.utc)
        
        # Update codex purchase count
        if purchase.codex_id:
            codex = db.query(Codex).filter(Codex.id == purchase.codex_id).first()
            if codex:
                codex.purchase_count += 1
        
        db.commit()
        db.refresh(purchase)
        
        return purchase
    
    async def verify_purchase(
        self,
        db: Session,
        user_id: int,
        codex_id: int
    ) -> bool:
        """Verify user has purchased codex"""
        purchase = db.query(Purchase).filter(
            Purchase.user_id == user_id,
            Purchase.codex_id == codex_id,
            Purchase.payment_status == "completed"
        ).first()
        
        return purchase is not None
    
    async def list_user_purchases(
        self,
        db: Session,
        user_id: int
    ) -> List[Purchase]:
        """List user purchases"""
        purchases = db.query(Purchase).filter(
            Purchase.user_id == user_id,
            Purchase.payment_status == "completed"
        ).order_by(Purchase.completed_at.desc()).all()
        
        return purchases
    
    async def get_analytics(self, db: Session) -> Dict:
        """Get platform analytics"""
        from models import Codex, User, Domain
        
        total_codexes = db.query(Codex).filter(Codex.is_active == True).count()
        total_users = db.query(User).filter(User.is_active == True).count()
        total_purchases = db.query(Purchase).filter(Purchase.payment_status == "completed").count()
        total_revenue = db.query(Purchase).filter(
            Purchase.payment_status == "completed"
        ).with_entities(func.sum(Purchase.amount)).scalar() or 0.0
        
        # Popular codexes (by purchase count)
        popular_codexes = db.query(Codex).filter(
            Codex.is_active == True
        ).order_by(Codex.purchase_count.desc()).limit(10).all()
        
        # Recent purchases
        recent_purchases = db.query(Purchase).filter(
            Purchase.payment_status == "completed"
        ).order_by(Purchase.completed_at.desc()).limit(10).all()
        
        return {
            "total_codexes": total_codexes,
            "total_users": total_users,
            "total_purchases": total_purchases,
            "total_revenue": float(total_revenue),
            "popular_codexes": popular_codexes,
            "recent_purchases": recent_purchases
        }

# Initialize service
purchase_service = PurchaseService()

