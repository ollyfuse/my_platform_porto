from pathlib import Path
import re

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

try:
    from docx import Document
except ImportError:
    Document = None

class ChatAgent:
    def __init__(self):
        self.root_folder = Path(__file__).resolve().parents[2]
        self.portfolio_text = self._load_html_text("index.html")
        self.cv_text = self._load_docx_text("olivier_bigirimana_Master_CV.docx")
        self.cover_letter_text = self._load_docx_text("Olivier_BIGIRIMANA_cover_letter.docx")
        
        # Debug info for production
        print(f"Root folder: {self.root_folder}")
        print(f"CV text loaded: {len(self.cv_text)} chars")
        print(f"Cover letter loaded: {len(self.cover_letter_text)} chars")
        print(f"Portfolio text loaded: {len(self.portfolio_text)} chars")
        # Embedded CV content as fallback
        self.embedded_cv = """Olivier BIGIRIMANA
📍 Rwanda | 📧 cyotero26@gmail.com | 📱 +250 787595645 | 🌐 Portfolio | 🔗 LinkedIn

Professional Summary
Enthusiastic and versatile tech professional with a Bachelor's degree in Computer Science and experience spanning web development, networking, quality assurance, and creative digital content production. Skilled in building full-stack web applications with Django, PostgreSQL, and Tailwind CSS, integrating APIs, and delivering high-quality, production-ready code.

Core Competencies
Web Development: HTML, CSS, JavaScript, Tailwind CSS, Django, PostgreSQL, REST API design
Software Engineering: Python (OOP), Git/GitHub, Agile practices, testing with Django test framework
Networking: Setup, configuration, troubleshooting, and maintenance
Quality Assurance: Manual testing, automated testing, bug tracking, test case development"""
        
        self.portfolio_info = {
            "name": "Olivier Bigirimana",
            "title": "Full-Stack Developer & Software Engineer",
            "location": "Kigali, Rwanda",
            "experience": "5+ years in full-stack development",
            "skills": ["Python", "Django", "JavaScript", "React", "PostgreSQL", "REST APIs", "Docker", "AWS"],
            "projects": [
                "ProcureToPay - Enterprise Procure-to-Pay system with multi-level approval workflows",
                "FuseTalk Rwanda - Video & text chat platform for cultural connection and tourism",
                "UmugandaTech - Community volunteer platform for national development",
                "DocuFind - Secure document recovery platform with privacy protection"
            ],
            "education": "Bachelor of Computer Science - University of Rwanda (2019-2024)",
            "contact": {
                "email": "cyotero26@gmail.com",
                "phone": "+250 787 595 645",
                "github": "https://github.com/ollyfuse",
                "linkedin": "https://www.linkedin.com/in/bigirimana-olivier-700ba21ba/"
            }
        }
    
    def _load_html_text(self, filename: str) -> str:
        path = self.root_folder / filename
        if not path.exists():
            return ""
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                if BeautifulSoup:
                    soup = BeautifulSoup(content, "html.parser")
                    for s in soup(["script", "style"]):
                        s.extract()
                    return soup.get_text(separator="\n").strip()
                else:
                    # Basic HTML cleaning
                    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
                    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
                    content = re.sub(r'<[^>]+>', '', content)
                    return content.strip()
        except:
            return ""
    
    def _load_docx_text(self, filename: str) -> str:
        path = self.root_folder / filename
        if not path.exists() or not Document:
            return ""
        try:
            doc = Document(str(path))
            return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
        except:
            return ""
    
    async def run_async(self, message: str) -> str:
        message_lower = message.lower()
        
        # Enhanced keyword matching for better accuracy
        if any(word in message_lower for word in ["cv", "resume", "curriculum"]):
            cv_content = self.cv_text if self.cv_text and len(self.cv_text) > 100 else self.embedded_cv
            
            if cv_content:
                lines = cv_content.split('\n')
                formatted_lines = []
                for line in lines[:12]:
                    if line.strip():
                        formatted_lines.append(line.strip())
                
                cv_preview = '\n'.join(formatted_lines)
                return f"📄 **Olivier's CV Summary:**\n\n{cv_preview}\n\n💡 *Want specific details? Ask about 'experience', 'education', or 'skills'*"
            
            return "📄 **Professional Summary:**\n\n🚀 **Current Role:** Full-Stack Developer at Solvit Africa Fellowship\n💻 **Experience:** 5+ years in full-stack development\n🎓 **Education:** Bachelor of Computer Science - University of Rwanda\n🏆 **Expertise:** Python, Django, JavaScript, React, PostgreSQL\n\n*Building complete web applications from frontend to backend*"
        
        elif any(word in message_lower for word in ["cover letter", "letter", "motivation", "why hire"]):
            if self.cover_letter_text:
                paragraphs = self.cover_letter_text.split('\n\n')
                preview_paragraphs = [p.strip() for p in paragraphs[:3] if p.strip()]
                letter_preview = '\n\n'.join(preview_paragraphs)
                return f"📜 **Career Motivation:**\n\n{letter_preview}\n\n💡 *This reflects his passion for technology and problem-solving*"
            return "📜 **Why Choose Olivier:**\n\n🎯 **Passion:** Building technology that solves real-world problems\n🚀 **Growth:** From IT Support → QA → Full-Stack Developer\n🌍 **Impact:** Creating solutions for fintech, social platforms, and enterprise\n📚 **Learning:** Continuously adapting to new technologies and best practices\n\n*Driven by the challenge of creating meaningful software solutions*"
        
        elif any(word in message_lower for word in ["experience", "work", "job", "career", "employment"]):
            return "💼 **Professional Journey:**\n\n🚀 **Current (2025):** Full-Stack Developer - Solvit Africa Fellowship\n   • Built ProcureToPay system with React frontend & Django backend\n   • Developed FuseTalk platform with real-time WebSocket chat\n   • Implemented Docker containerization & CI/CD pipelines\n   • Achieved 40% API performance improvement\n\n🔍 **Previous Roles:**\n   • **Quality Assurance:** Testing, automation, security focus\n   • **IT Support:** System reliability, user experience\n   • **Freelance Projects:** 15+ REST APIs, payment integrations\n\n*Each role built the foundation for full-stack expertise*"
        
        elif any(word in message_lower for word in ["skills", "technology", "tech", "stack", "programming", "languages"]):
            skills = ", ".join(self.portfolio_info['skills'])
            return f"🚀 **Technical Stack:**\n\n🌐 **Frontend:** JavaScript (85%), React (80%), HTML/CSS, Responsive Design\n🔧 **Backend:** Python (90%), Django (88%), REST APIs (92%)\n📋 **Database:** PostgreSQL (85%), Redis, Database Optimization\n☁️ **DevOps:** Docker (78%), AWS (75%), CI/CD Pipelines\n🔄 **Tools:** Git, Celery, WebSocket, Testing Frameworks\n\n🎯 **Specialization:** Building complete web applications from concept to deployment\n\n*Full-stack expertise with focus on scalable, maintainable solutions*"
        
        elif any(word in message_lower for word in ["projects", "portfolio", "work", "built", "developed"]):
            return "💼 **Featured Projects:**\n\n🏆 **ProcureToPay** - Enterprise Procurement System\n   • **Frontend:** React with modern UI/UX\n   • **Backend:** Django REST API with multi-level approvals\n   • **Features:** JWT auth, role-based permissions, Docker deployment\n   • **Live Demo:** https://procuretopays.netlify.app/\n\n🌍 **FuseTalk Rwanda** - Cultural Connection Platform\n   • **Frontend:** Real-time chat interface\n   • **Backend:** WebSocket + Django for live communication\n   • **Purpose:** Connecting locals with tourists for cultural exchange\n\n🤝 **UmugandaTech** - Community Volunteer Platform\n   • **Full-Stack:** Complete volunteer management system\n   • **Integration:** Twilio API for SMS notifications\n   • **Impact:** Supporting Rwanda's national development\n   • **Live:** https://umugandatech.netlify.app\n\n*Each project demonstrates end-to-end development capabilities*"
        
        elif "contact" in message_lower or "reach" in message_lower:
            contact = self.portfolio_info['contact']
            return f"📞 Contact Olivier:\n\n📧 **Email**: {contact['email']}\n📱 **Phone**: {contact['phone']}\n💼 **LinkedIn**: {contact['linkedin']}\n🔗 **GitHub**: {contact['github']}\n📍 **Location**: {self.portfolio_info['location']}\n\nFeel free to reach out for collaboration opportunities or technical discussions!"
        
        elif "education" in message_lower or "study" in message_lower or "university" in message_lower:
            return f"🎓 Olivier's Education & Certifications:\n\n🏫 **Degree**: {self.portfolio_info['education']}\n   • Specialized in Software Engineering\n   • Focus on backend systems and database design\n\n🏆 **Recent Certifications (2025)**:\n   • Quality Assurance Certification – Digital Talent Program\n   • Intermediate Python for Developers\n   • DevOps Continuous Feedback Implementation\n   • Software testing, bug tracking, automation basics\n\n📚 **Continuous Learning**: Always staying updated with latest backend technologies and best practices."
        
        elif "location" in message_lower or "where" in message_lower:
            return f"📍 Olivier is based in **{self.portfolio_info['location']}**.\n\nHe's available for remote work and collaboration with international teams, bringing East African tech talent to global projects."
        
        elif "about" in message_lower or "tell me about" in message_lower:
            if self.portfolio_text and "about me" in self.portfolio_text.lower():
                lines = self.portfolio_text.split('\n')
                about_section = []
                capture = False
                for line in lines:
                    if "about me" in line.lower():
                        capture = True
                        continue
                    if capture and line.strip():
                        about_section.append(line.strip())
                        if len(about_section) >= 4:
                            break
                if about_section:
                    return f"👨💻 About Olivier (from portfolio):\n\n" + "\n\n".join(about_section[:3]) + "\n\n💡 Extracted from his live portfolio!"
            return f"👨‍💻 About {self.portfolio_info['name']}:\n\nA passionate **{self.portfolio_info['title']}** with **{self.portfolio_info['experience']}**, based in **{self.portfolio_info['location']}**.\n\n🎯 **Mission**: Crafting scalable backend solutions and robust APIs that power modern applications.\n\n💡 **Passion**: Clean code architecture, database optimization, and implementing security best practices.\n\n🌍 **Impact**: Working on diverse projects from fintech platforms to wellness applications, always focused on solving real-world problems through technology.\n\n🎵 **Personal**: When not coding, enjoys music and creating cultural connections through musical experiences."
        
        else:
            return f"👋 **Hello! I'm {self.portfolio_info['name']}'s AI Assistant**\n\n💬 **Quick Questions You Can Ask:**\n\n📄 *"Tell me about your CV"* - Professional background\n🚀 *"What's your experience?"* - Work history & achievements\n💻 *"What are your technical skills?"* - Full-stack expertise\n🎯 *"Show me your projects"* - Portfolio & live demos\n🎓 *"What's your education?"* - Academic background\n📞 *"How can I contact you?"* - Get in touch info\n💡 *"Why should I hire you?"* - Career motivation\n\n**{self.portfolio_info['name']}** is a **{self.portfolio_info['title']}** with **{self.portfolio_info['experience']}**.\n\n*Just ask naturally - I understand context!*"

root_agent = ChatAgent()