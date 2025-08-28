#!/usr/bin/env python3
import uvicorn
from main import app

if __name__ == "__main__":
    print("🚀 Starting AI Agents Server...")
    print("📡 Server will be available at: http://localhost:8000")
    print("🤖 Available agents: chat, guest, planning, project")
    print("📋 API docs at: http://localhost:8000/docs")
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)