#!/usr/bin/env python3

import sys
import os
sys.path.append('my_assistant_agents')

from secretary_chat_agent.agent import ChatAgent
import asyncio

async def test_agent():
    agent = ChatAgent()
    
    print("=== TESTING DOCUMENT READING ===")
    print(f"Root folder: {agent.root_folder}")
    print(f"CV file exists: {(agent.root_folder / 'olivier_bigirimana_Master_CV.docx').exists()}")
    print(f"Cover letter exists: {(agent.root_folder / 'Olivier_BIGIRIMANA_cover_letter.docx').exists()}")
    print(f"Index.html exists: {(agent.root_folder / 'index.html').exists()}")
    
    print(f"\nCV text length: {len(agent.cv_text)}")
    print(f"Cover letter text length: {len(agent.cover_letter_text)}")
    print(f"Portfolio text length: {len(agent.portfolio_text)}")
    
    if agent.cv_text:
        print(f"\nCV Preview (first 200 chars):\n{agent.cv_text[:200]}...")
    else:
        print("\nCV text is empty!")
        
    if agent.cover_letter_text:
        print(f"\nCover Letter Preview (first 200 chars):\n{agent.cover_letter_text[:200]}...")
    else:
        print("\nCover letter text is empty!")
    
    print("\n=== TESTING CV QUERY ===")
    response = await agent.run_async("tell me about cv")
    print(response)

if __name__ == "__main__":
    asyncio.run(test_agent())