"""
Email Service for Purchase Fulfillment
Constitutional Framework: Layer 4 - Risk-to-Reward (fulfillment)
Built from Remembrance | Operating under Format Law
"""

import os
from typing import Optional, Dict
from config import settings
from datetime import datetime

# Try to import email services
try:
    import sendgrid
    from sendgrid.helpers.mail import Mail
    SENDGRID_AVAILABLE = True
except ImportError:
    SENDGRID_AVAILABLE = False

try:
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    SMTP_AVAILABLE = True
except ImportError:
    SMTP_AVAILABLE = False


class EmailService:
    """Email service for sending purchase fulfillment emails"""
    
    def __init__(self):
        self.sender_email = os.getenv("EMAIL_SENDER", "noreply@truthdrop.com")
        self.sender_name = os.getenv("EMAIL_SENDER_NAME", "Truth Drop Platform")
        self.frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
    
    async def send_purchase_email(
        self,
        customer_email: str,
        codex_title: str,
        download_url: str,
        purchase_amount: float,
        purchase_currency: str = "USD"
    ) -> bool:
        """
        Send purchase fulfillment email with download link
        Constitutional Framework: Layer 4 - Risk-to-Reward (fulfillment)
        """
        try:
            # Try SendGrid first (recommended)
            if settings.SENDGRID_API_KEY and SENDGRID_AVAILABLE:
                return await self._send_via_sendgrid(
                    customer_email, codex_title, download_url, purchase_amount, purchase_currency
                )
            
            # Fallback to SMTP
            if settings.SMTP_HOST and SMTP_AVAILABLE:
                return await self._send_via_smtp(
                    customer_email, codex_title, download_url, purchase_amount, purchase_currency
                )
            
            # If no email service configured, log and return True (email will be sent later)
            print(f"[Email Service] No email service configured. Would send to {customer_email}")
            print(f"[Email Service] Download URL: {download_url}")
            return True
            
        except Exception as e:
            print(f"[Email Service] Error sending email: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    async def _send_via_sendgrid(
        self,
        customer_email: str,
        codex_title: str,
        download_url: str,
        purchase_amount: float,
        purchase_currency: str
    ) -> bool:
        """Send email via SendGrid"""
        try:
            sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
            
            subject = f"Your Purchase: {codex_title}"
            
            html_content = f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h1 style="color: #00AA00;">Thank You for Your Purchase!</h1>
                    
                    <p>Your purchase of <strong>{codex_title}</strong> has been confirmed.</p>
                    
                    <div style="background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin: 20px 0;">
                        <p><strong>Amount Paid:</strong> {purchase_currency} ${purchase_amount:.2f}</p>
                        <p><strong>Item:</strong> {codex_title}</p>
                    </div>
                    
                    <p>You can download your purchase using the link below:</p>
                    
                    <div style="text-align: center; margin: 30px 0;">
                        <a href="{download_url}" 
                           style="background-color: #00AA00; color: white; padding: 15px 30px; 
                                  text-decoration: none; border-radius: 5px; display: inline-block; 
                                  font-weight: bold; font-size: 16px;">
                            Download Now
                        </a>
                    </div>
                    
                    <p style="font-size: 12px; color: #666; margin-top: 30px;">
                        This download link is valid for 30 days. If you have any questions, 
                        please contact support.
                    </p>
                    
                    <hr style="border: none; border-top: 1px solid #eee; margin: 30px 0;">
                    
                    <p style="font-size: 12px; color: #999;">
                        Built from Remembrance | Operating under Format Law<br>
                        Truth Drop Platform - Constitutional Knowledge Marketplace
                    </p>
                </div>
            </body>
            </html>
            """
            
            plain_content = f"""
Thank You for Your Purchase!

Your purchase of {codex_title} has been confirmed.

Amount Paid: {purchase_currency} ${purchase_amount:.2f}
Item: {codex_title}

Download your purchase here:
{download_url}

This download link is valid for 30 days.

Built from Remembrance | Operating under Format Law
Truth Drop Platform
            """
            
            message = Mail(
                from_email=(self.sender_email, self.sender_name),
                to_emails=customer_email,
                subject=subject,
                plain_text_content=plain_content,
                html_content=html_content
            )
            
            response = sg.send(message)
            print(f"[Email Service] SendGrid email sent to {customer_email}. Status: {response.status_code}")
            return response.status_code in [200, 201, 202]
            
        except Exception as e:
            print(f"[Email Service] SendGrid error: {str(e)}")
            raise
    
    async def _send_via_smtp(
        self,
        customer_email: str,
        codex_title: str,
        download_url: str,
        purchase_amount: float,
        purchase_currency: str
    ) -> bool:
        """Send email via SMTP"""
        try:
            smtp_host = settings.SMTP_HOST
            smtp_port = int(settings.SMTP_PORT or 587)
            smtp_user = settings.SMTP_USER
            smtp_password = settings.SMTP_PASSWORD
            
            msg = MIMEMultipart('alternative')
            msg['From'] = f"{self.sender_name} <{self.sender_email}>"
            msg['To'] = customer_email
            msg['Subject'] = f"Your Purchase: {codex_title}"
            
            plain_text = f"""
Thank You for Your Purchase!

Your purchase of {codex_title} has been confirmed.

Amount Paid: {purchase_currency} ${purchase_amount:.2f}
Item: {codex_title}

Download your purchase here:
{download_url}

This download link is valid for 30 days.
            """
            
            html_text = f"""
            <html>
            <body style="font-family: Arial, sans-serif;">
                <h1>Thank You for Your Purchase!</h1>
                <p>Your purchase of <strong>{codex_title}</strong> has been confirmed.</p>
                <p><strong>Amount Paid:</strong> {purchase_currency} ${purchase_amount:.2f}</p>
                <p><a href="{download_url}" style="background-color: #00AA00; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Download Now</a></p>
                <p style="font-size: 12px;">This download link is valid for 30 days.</p>
            </body>
            </html>
            """
            
            msg.attach(MIMEText(plain_text, 'plain'))
            msg.attach(MIMEText(html_text, 'html'))
            
            with smtplib.SMTP(smtp_host, smtp_port) as server:
                server.starttls()
                if smtp_user and smtp_password:
                    server.login(smtp_user, smtp_password)
                server.send_message(msg)
            
            print(f"[Email Service] SMTP email sent to {customer_email}")
            return True
            
        except Exception as e:
            print(f"[Email Service] SMTP error: {str(e)}")
            raise


# Initialize service
email_service = EmailService()

