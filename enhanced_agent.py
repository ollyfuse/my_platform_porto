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

class EnhancedChatAgent:
    def __init__(self):
        self.root_folder = Path(__file__).resolve().parent
        self.portfolio_text = self._load_html_text("index.html")
        self.cv_text = self._load_docx_text("olivier_bigirimana_Master_CV.docx")
        self.cover_letter_text = self._load_docx_text("Olivier_BIGIRIMANA_cover_letter.docx")
        
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
        
        # Enhanced CV responses
        if any(word in message_lower for word in ["cv", "resume", "curriculum", "background", "qualification"]):
            cv_content = self.cv_text if self.cv_text and len(self.cv_text) > 100 else self.embedded_cv
            
            if cv_content:
                lines = cv_content.split('\n')
                formatted_lines = []
                for line in lines[:15]:
                    if line.strip():
                        formatted_lines.append(line.strip())
                
                cv_preview = '\n'.join(formatted_lines)
                return f"📄 **Olivier's Complete CV:**\n\n{cv_preview}\n\n🎯 **Quick Facts:**\n• 5+ years full-stack development\n• Bachelor's in Computer Science (2019-2024)\n• Specialized in Python, Django, JavaScript, React\n• Enterprise project experience (ProcureToPay, FuseTalk)\n• Quality Assurance & DevOps certified\n\n💡 *Ask about specific sections: 'experience', 'education', 'projects', or 'certifications'*"
            
            return "📄 **Olivier's Professional Profile:**\n\n👨💻 **Current Position:** Full-Stack Developer - Solvit Africa Fellowship (2025)\n🎓 **Education:** Bachelor of Computer Science - University of Rwanda (2019-2024)\n💼 **Experience:** 5+ years in full-stack web development\n🏆 **Specialization:** Python, Django, JavaScript, React, PostgreSQL, Docker\n\n🚀 **Key Achievements:**\n• Built enterprise procurement system (ProcureToPay)\n• Developed cultural connection platform (FuseTalk Rwanda)\n• 40% API performance improvement\n• Docker containerization & CI/CD implementation\n\n📋 **Certifications:**\n• Quality Assurance - Digital Talent Program\n• Intermediate Python for Developers\n• DevOps Continuous Feedback Implementation\n\n*Complete end-to-end web application development expertise*"
        
        # Enhanced experience responses
        elif any(word in message_lower for word in ["experience", "work", "job", "career", "employment", "history"]):
            return "💼 **Detailed Work Experience:**\n\n🚀 **Current Role (2025 - Present):**\n**Full-Stack Developer** - Solvit Africa Fellowship\n\n**Key Projects & Achievements:**\n• **ProcureToPay System:** Enterprise procurement platform with React frontend, Django REST backend, multi-level approval workflows, JWT authentication, Docker deployment\n• **FuseTalk Rwanda:** Cultural connection platform with real-time video/text chat, WebRTC integration, tourism discovery features\n• **Performance Optimization:** Achieved 40% improvement in API response times through database query optimization and caching strategies\n• **DevOps Implementation:** Set up CI/CD pipelines, Docker containerization, automated testing with 95% code coverage\n• **Team Leadership:** Mentored junior developers, conducted code reviews, established development best practices\n\n🔧 **Previous Experience:**\n• **Quality Assurance Specialist:** Manual & automated testing, bug tracking, security testing, test case development\n• **IT Support Technician:** System administration, network troubleshooting, user support, hardware maintenance\n• **Freelance Developer:** Built 15+ REST APIs serving 10,000+ daily users, integrated payment gateways (Stripe, PayPal), third-party service integrations\n\n📈 **Career Progression:** IT Support → QA → Backend Development → Full-Stack Development\n\n*Comprehensive experience across the entire software development lifecycle*"
        
        # Default comprehensive greeting
        else:
            return f"👋 **Hello! I'm {self.portfolio_info['name']}'s AI Assistant**\n\nI have comprehensive knowledge about Olivier's professional background and can provide detailed information about his CV, experience, and qualifications.\n\n💬 **What I Can Help With:**\n\n📄 *\"Tell me about your CV\"* - Complete professional background & qualifications\n🚀 *\"What's your work experience?\"* - Detailed career history & achievements\n💻 *\"What are your technical skills?\"* - Full-stack technologies & expertise levels\n🎯 *\"Show me your projects\"* - Live demos & technical implementation details\n🎓 *\"What's your education?\"* - Academic background & professional certifications\n📞 *\"How can I contact Olivier?\"* - Direct contact information & availability\n💡 *\"Why should I hire him?\"* - Career motivation & unique value proposition\n🏢 *\"Tell me about ProcureToPay\"* - Enterprise project deep-dive\n🌍 *\"What is FuseTalk Rwanda?\"* - Social platform features & impact\n\n**About Olivier:** {self.portfolio_info['title']} with {self.portfolio_info['experience']}, specializing in building complete web applications from concept to deployment.\n\n*Ask me anything - I have access to his complete professional profile!*"

root_agent = EnhancedChatAgent()