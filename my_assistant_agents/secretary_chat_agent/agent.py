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
        self.portfolio_info = {
            "name": "Olivier Bigirimana",
            "title": "Backend Developer & Problem Solver",
            "location": "Kigali, Rwanda",
            "experience": "5+ years in backend development",
            "skills": ["Python", "Django", "PostgreSQL", "REST APIs", "Celery", "Redis"],
            "projects": [
                "BBIS Banking Platform - Comprehensive banking and financial services platform",
                "Ikanisa Church Management - Full-featured church management system", 
                "Human Justice API - RESTful API for human rights organization",
                "Good Life Wellness Platform - Comprehensive lifestyle and wellness platform"
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
        
        if "cv" in message_lower or "resume" in message_lower:
            if self.cv_text:
                # Extract key sections from actual CV
                lines = self.cv_text.split('\n')
                formatted_lines = []
                for line in lines[:15]:  # First 15 lines for preview
                    if line.strip():
                        formatted_lines.append(line.strip())
                
                cv_preview = '\n'.join(formatted_lines)
                return f"📄 **From Olivier's CV:**\n\n{cv_preview}\n\n💡 This is extracted from his actual CV document. Ask for specific sections like 'experience' or 'education' for more details!"
            return "📄 **Olivier's Professional Background:**\n\n🎯 **Currently:** Solvit Africa Backend Development Fellowship (2025)\n💼 **Experience:** 5+ years in backend development\n🎓 **Education:** Bachelor of Computer Science - University of Rwanda (2019-2024)\n🏆 **Certifications:** Quality Assurance, Python Development, DevOps\n\nSpecializes in Python, Django, and scalable backend solutions."
        
        elif "cover letter" in message_lower or "letter" in message_lower:
            if self.cover_letter_text:
                # Extract first few paragraphs for better formatting
                paragraphs = self.cover_letter_text.split('\n\n')
                preview_paragraphs = [p.strip() for p in paragraphs[:3] if p.strip()]
                letter_preview = '\n\n'.join(preview_paragraphs)
                return f"📜 **From Olivier's Cover Letter:**\n\n{letter_preview}\n\n💡 This shows his motivation and career aspirations directly from his cover letter document!"
            return "📜 **Olivier's Professional Summary:**\n\nPassionate Backend Developer with 5+ years of experience crafting robust, scalable server-side solutions. Based in Kigali, Rwanda, he specializes in Python and Django development with expertise in building RESTful APIs, microservices, and cloud-native applications.\n\nHis journey spans diverse projects from fintech platforms to e-commerce solutions, with a focus on clean code architecture, database optimization, and security best practices."
        
        elif "experience" in message_lower or "work" in message_lower:
            return "💼 Olivier's Professional Experience:\n\n🚀 **Current (2025)**: Solvit Africa Backend Development Fellowship\n   • Leading backend development for fintech and e-commerce platforms\n   • Architecting microservices solutions\n   • Implementing CI/CD pipelines\n   • Mentoring junior developers\n   • Reduced API response time by 40% through optimization\n\n🔧 **Previous**: Quality Assurance & Development\n   • Built 15+ REST APIs serving 10,000+ daily users\n   • Integrated payment gateways and third-party services\n   • Optimized database queries reducing load time by 60%"
        
        elif "skills" in message_lower or "technology" in message_lower or "tech" in message_lower:
            skills = ", ".join(self.portfolio_info['skills'])
            return f"🚀 Olivier's Technical Expertise:\n\n💻 **Core Technologies**: {skills}\n\n🏗️ **Specializations**:\n• Backend Architecture & Microservices\n• RESTful API Design & Development\n• Database Design & Optimization\n• Cloud-Native Applications\n• Security Best Practices\n• Performance Optimization\n\nFocuses on building efficient, secure, and scalable solutions that power modern applications."
        
        elif "projects" in message_lower or "portfolio" in message_lower:
            return "💼 Olivier's Featured Projects:\n\n🏦 **BBIS Banking Platform**\n   • Comprehensive banking and financial services platform\n   • Secure transaction processing & real-time account management\n   • Built with Django REST Framework, PostgreSQL, Redis\n\n⛪ **Ikanisa Church Management**\n   • Full-featured church management system\n   • Member registration, event scheduling, donation tracking\n   • Mobile-responsive design with automated reporting\n\n⚖️ **Human Justice API**\n   • RESTful API for human rights organization\n   • Case management & document tracking\n   • JWT authentication & role-based access control\n\n🌟 **Good Life Wellness Platform**\n   • Comprehensive lifestyle and wellness platform\n   • Real-time notifications & social engagement tools\n   • WebSocket integration for live features"
        
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
            return f"👋 **Hi! I'm {self.portfolio_info['name']}'s AI assistant.**\n\nI can help you learn about:\n\n• **CV & Resume** - Professional background & experience\n• **Cover Letter** - Career motivation & goals\n• **Experience** - Work history & achievements\n• **Technical Skills** - Technologies & expertise\n• **Projects** - Portfolio & case studies\n• **Education** - Academic background & certifications\n• **Contact** - How to reach Olivier\n\n**{self.portfolio_info['name']}** is a **{self.portfolio_info['title']}** with **{self.portfolio_info['experience']}**.\n\nWhat would you like to know?"

root_agent = ChatAgent()