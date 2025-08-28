# AI Agents Integration

## 🚀 Quick Start

### 1. Start the Backend Server
```bash
cd my_assistant_agents
python start_server.py
```

### 2. Open Portfolio
Open `index.html` in your browser. The AI chat widget will appear in the bottom-right corner.

## 🤖 Available Agents

1. **Portfolio Q&A** - Answers questions about your experience, skills, projects
2. **Schedule Meeting** - Helps visitors schedule appointments
3. **Daily Planning** - Shows daily schedules and planning
4. **Project Help** - Assists with project management and Git workflows

## 🔧 Features

- **Chat Widget**: Floating chat interface with agent selection
- **Real-time Communication**: Direct API integration with backend
- **Responsive Design**: Works on desktop and mobile
- **Theme Support**: Matches your portfolio's dark/light theme

## 📡 API Endpoints

- `POST /api/chat` - Send messages to agents
- `GET /api/health` - Check server status
- `GET /docs` - Interactive API documentation

## 🎨 Customization

### Change API URL
Edit `javascript.js` line with `API_BASE` to point to your deployed backend.

### Modify Agent Responses
Edit the agent files in their respective directories to customize responses.

### Style the Chat Widget
Modify the chat widget styles in `style.css` under "Chat Widget Styles".

## 🚀 Deployment

### Backend (Recommended: Railway, Heroku, or DigitalOcean)
1. Deploy the `my_assistant_agents` folder
2. Set environment variables if needed
3. Update `API_BASE` in `javascript.js`

### Frontend
Already configured for GitHub Pages deployment.