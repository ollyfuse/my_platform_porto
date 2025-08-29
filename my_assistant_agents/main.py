from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

# Import agents
from secretary_guest_agent.agent import root_agent as guest_agent
from secretary_chat_agent.agent import root_agent as chat_agent
from secretary_planning_agent.agent import root_agent as planning_agent
from Project_manage_agent.agent import root_agent as project_agent

app = FastAPI(title="Portfolio AI Agents", version="1.0.0")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    agent_type: str = "chat"  # chat, guest, planning, project

class ChatResponse(BaseModel):
    response: str
    agent: str
    status: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_with_agent(request: ChatRequest):
    try:
        # Route to appropriate agent
        if request.agent_type == "guest":
            response = await guest_agent.run_async(request.message)
        elif request.agent_type == "planning":
            response = await planning_agent.run_async(request.message)
        elif request.agent_type == "project":
            response = await project_agent.run_async(request.message)
        else:  # default to chat agent
            response = await chat_agent.run_async(request.message)
        
        return ChatResponse(
            response=response,
            agent=request.agent_type,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "agents": ["chat", "guest", "planning", "project"], "version": "2.0"}

@app.get("/api/debug")
async def debug_info():
    from pathlib import Path
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
        agent_working = True
        cv_length = len(chat_agent.cv_text)
        cover_length = len(chat_agent.cover_letter_text)
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)