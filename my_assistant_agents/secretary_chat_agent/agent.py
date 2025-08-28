from pathlib import Path

class ChatAgent:
    def __init__(self):
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
    
    async def run_async(self, message: str) -> str:
        message_lower = message.lower()
        
        if "experience" in message_lower or "work" in message_lower:
            return f"Olivier has {self.portfolio_info['experience']} specializing in Python and Django development. He's worked on diverse projects including fintech platforms, church management systems, and wellness applications."
        
        elif "skills" in message_lower or "technology" in message_lower:
            skills = ", ".join(self.portfolio_info['skills'])
            return f"Olivier's technical expertise includes: {skills}. He focuses on building efficient, secure, and scalable backend solutions."
        
        elif "projects" in message_lower or "portfolio" in message_lower:
            projects = "\n• ".join(self.portfolio_info['projects'])
            return f"Here are some of Olivier's key projects:\n• {projects}"
        
        elif "contact" in message_lower or "reach" in message_lower:
            contact = self.portfolio_info['contact']
            return f"You can reach Olivier at:\n📧 Email: {contact['email']}\n📱 Phone: {contact['phone']}\n💼 LinkedIn: {contact['linkedin']}\n🔗 GitHub: {contact['github']}"
        
        elif "education" in message_lower or "study" in message_lower:
            return f"Olivier holds a {self.portfolio_info['education']}, specializing in Software Engineering with focus on backend systems and database design."
        
        elif "location" in message_lower or "where" in message_lower:
            return f"Olivier is based in {self.portfolio_info['location']}."
        
        else:
            return f"Hi! I'm Olivier's AI assistant. I can tell you about his experience, skills, projects, education, or contact information. {self.portfolio_info['name']} is a {self.portfolio_info['title']} with {self.portfolio_info['experience']}. What would you like to know?"

root_agent = ChatAgent()