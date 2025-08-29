# Quick Backend Deployment

## 🚀 Render Deployment Steps:

1. **Go to Render.com** → New Web Service
2. **Connect GitHub** repository
3. **Configure:**
   ```
   Name: olivier-ai-agents
   Root Directory: my_assistant_agents
   Build Command: pip install -r requirements_minimal.txt
   Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

4. **Environment Variables:**
   ```
   GOOGLE_API_KEY = your_google_ai_studio_key
   GOOGLE_GENAI_USE_VERTEXAI = FALSE
   ```

5. **After Deploy:**
   - Copy your Render URL (e.g., `https://olivier-ai-agents.onrender.com`)
   - Update `javascript.js` line 318 with your URL
   - Push changes to trigger Netlify redeploy

## ✅ Result:
- Frontend: Netlify (your portfolio)
- Backend: Render (AI agents)
- Full AI interaction enabled!

## 🔧 Alternative: Railway
If Render doesn't work, try Railway.app with same configuration.