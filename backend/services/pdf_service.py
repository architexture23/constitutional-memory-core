"""
Truth Drop Platform - PDF Service
Built from Remembrance | Operating under Format Law
Constitutional Framework: Layer 4 - Risk-to-Reward (Content Delivery)
"""

from models import Codex
from config import settings
import os
from typing import Optional, List
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from markdown import markdown
from html.parser import HTMLParser
import re

class PDFService:
    """PDF generation service - Constitutional Framework: Layer 4"""
    
    def __init__(self):
        self.pdf_dir = settings.PDF_DIR
        self.ebook_dir = settings.EBOOK_DIR
    
    async def generate_download(
        self,
        codex: Codex,
        format: str = "pdf"
    ) -> Optional[str]:
        """
        Generate download file (PDF or EPUB)
        Constitutional Framework: Layer 4 - Risk-to-Reward (Content Delivery)
        """
        if format == "pdf":
            return await self.generate_pdf(codex)
        elif format == "epub":
            return await self.generate_epub(codex)
        else:
            return None
    
    async def generate_pdf(self, codex: Codex) -> Optional[str]:
        """Generate PDF from codex"""
        os.makedirs(self.pdf_dir, exist_ok=True)
        
        file_path = os.path.join(self.pdf_dir, f"{codex.slug}.pdf")
        
        # Create PDF document
        doc = SimpleDocTemplate(
            file_path,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # Build content
        story = []
        styles = getSampleStyleSheet()
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor='#000000',
            spaceAfter=30,
            alignment=TA_CENTER
        )
        story.append(Paragraph(codex.title, title_style))
        story.append(Spacer(1, 12))
        
        # Description
        if codex.description:
            desc_style = ParagraphStyle(
                'CustomDescription',
                parent=styles['Normal'],
                fontSize=12,
                textColor='#666666',
                spaceAfter=20,
                alignment=TA_CENTER
            )
            story.append(Paragraph(codex.description, desc_style))
            story.append(Spacer(1, 12))
        
        # Constitutional Framework Header
        framework_style = ParagraphStyle(
            'CustomFramework',
            parent=styles['Heading2'],
            fontSize=14,
            textColor='#333333',
            spaceAfter=10,
            spaceBefore=20
        )
        story.append(Paragraph("Constitutional Framework", framework_style))
        
        framework_info = f"""
        <b>Format Law:</b> {codex.format_law_version}<br/>
        <b>Constitutional Compliance:</b> {'Yes' if codex.constitutional_compliance else 'No'}<br/>
        <b>Remembrance Integration:</b> {'Yes' if codex.remembrance_integration else 'No'}<br/>
        <b>Version:</b> {codex.version}
        """
        story.append(Paragraph(framework_info, styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Content
        if codex.content:
            # Convert markdown to HTML, then to PDF
            html_content = markdown(codex.content)
            # Simple HTML to PDF conversion
            # For production, use more sophisticated conversion
            paragraphs = self._html_to_paragraphs(html_content)
            for para in paragraphs:
                story.append(para)
                story.append(Spacer(1, 12))
        
        # Build PDF
        doc.build(story)
        
        return file_path
    
    def _html_to_paragraphs(self, html: str) -> List:
        """Convert HTML to ReportLab paragraphs"""
        # Simple HTML tag removal for basic text
        # For production, use more sophisticated HTML parsing
        text = re.sub(r'<[^>]+>', '', html)
        lines = text.split('\n')
        
        paragraphs = []
        styles = getSampleStyleSheet()
        
        for line in lines:
            line = line.strip()
            if line:
                paragraphs.append(Paragraph(line, styles['Normal']))
        
        return paragraphs
    
    async def generate_epub(self, codex: Codex) -> Optional[str]:
        """Generate EPUB from codex"""
        os.makedirs(self.ebook_dir, exist_ok=True)
        
        file_path = os.path.join(self.ebook_dir, f"{codex.slug}.epub")
        
        # For production, use proper EPUB generation library
        # For now, return placeholder
        # TODO: Implement EPUB generation
        
        return file_path

# Initialize service
pdf_service = PDFService()

