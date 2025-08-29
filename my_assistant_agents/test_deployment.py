#!/usr/bin/env python3
"""Test script to verify deployment status"""

from pathlib import Path
import sys

def test_deployment():
    print("=== DEPLOYMENT TEST ===")
    
    # Check current directory
    current_dir = Path(__file__).resolve().parent
    root_dir = current_dir.parent
    
    print(f"Current dir: {current_dir}")
    print(f"Root dir: {root_dir}")
    
    # Check if files exist
    cv_file = root_dir / "olivier_bigirimana_Master_CV.docx"
    cover_file = root_dir / "Olivier_BIGIRIMANA_cover_letter.docx"
    
    print(f"CV file exists: {cv_file.exists()}")
    print(f"Cover letter exists: {cover_file.exists()}")
    
    # Test imports
    try:
        from bs4 import BeautifulSoup
        print("BeautifulSoup: ✅")
    except ImportError:
        print("BeautifulSoup: ❌")
    
    try:
        from docx import Document
        print("python-docx: ✅")
    except ImportError:
        print("python-docx: ❌")
    
    # Test agent
    try:
        from secretary_chat_agent.agent import ChatAgent
        agent = ChatAgent()
        print(f"Agent CV text length: {len(agent.cv_text)}")
        print(f"Agent cover letter length: {len(agent.cover_letter_text)}")
        print("Agent initialization: ✅")
    except Exception as e:
        print(f"Agent initialization: ❌ - {e}")

if __name__ == "__main__":
    test_deployment()