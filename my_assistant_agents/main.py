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
    return {"status": "healthy", "agents": ["chat", "guest", "planning", "project"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)