# Deployment Guide

## 🎯 **Option 1: Netlify Only (Simple)**

### What Works:
- ✅ Portfolio website
- ✅ Basic chat responses
- ✅ Contact form with reCAPTCHA
- ✅ Reflection journal

### Deploy Steps:
1. Push to GitHub
2. Connect to Netlify
3. Set environment variables in Netlify dashboard:
   - `GOOGLE_API_KEY`: Your Google AI Studio key
   - `RECAPTCHA_SECRET_KEY`: Your reCAPTCHA secret

### Limitations:
- Basic AI responses only
- No Google ADK integration
- No persistent storage

---

## 🔄 **Option 2: Split Architecture (Full Features)**

### Frontend: Netlify
- Deploy main portfolio
- Chat widget connects to external API

### Backend: Render/Railway
- Deploy `my_assistant_agents` folder
- Full Google ADK integration
- Persistent storage capabilities

### Deploy Steps:

#### Backend (Render):
1. Create new Web Service on Render
2. Connect GitHub repository
3. Set build command: `cd my_assistant_agents && pip install -r requirements_minimal.txt`
4. Set start command: `cd my_assistant_agents && uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables:
   - `GOOGLE_API_KEY`: Your Google AI Studio key
   - `GOOGLE_GENAI_USE_VERTEXAI`: FALSE

#### Frontend (Netlify):
1. Update `javascript.js` API_BASE to your Render URL
2. Deploy to Netlify
3. Set reCAPTCHA environment variables

---

## 🚀 **Recommended Approach:**

**Start with Option 1** (Netlify only) for quick deployment, then upgrade to Option 2 when you need advanced AI features.

### Current Status:
- ✅ Netlify functions created
- ✅ Render config ready
- ✅ Environment variables documented
- ✅ Both deployment paths available