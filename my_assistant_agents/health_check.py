from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/debug")
async def debug_info():
    root_dir = Path(__file__).resolve().parent.parent
    
    # Check files
    cv_exists = (root_dir / "olivier_bigirimana_Master_CV.docx").exists()
    cover_exists = (root_dir / "Olivier_BIGIRIMANA_cover_letter.docx").exists()
    
    # Check imports
    try:
        from bs4 import BeautifulSoup
        bs4_available = True
    except ImportError:
        bs4_available = False
    
    try:
        from docx import Document
        docx_available = True
    except ImportError:
        docx_available = False
    
    # Test agent
    try:
        from secretary_chat_agent.agent import ChatAgent
        agent = ChatAgent()
        agent_working = True
        cv_length = len(agent.cv_text)
        cover_length = len(agent.cover_letter_text)
    except Exception as e:
        agent_working = False
        cv_length = 0
        cover_length = 0
    
    return {
        "root_directory": str(root_dir),
        "files": {
            "cv_exists": cv_exists,
            "cover_letter_exists": cover_exists
        },
        "dependencies": {
            "beautifulsoup4": bs4_available,
            "python_docx": docx_available
        },
        "agent": {
            "working": agent_working,
            "cv_text_length": cv_length,
            "cover_letter_length": cover_length
        }
    }