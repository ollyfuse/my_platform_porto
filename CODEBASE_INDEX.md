# Codebase Index - My Platform Porto

## 📋 Project Overview
**Portfolio Website + AI Assistant Agents System**
- **Domain**: bigirimanaolivier.io
- **Type**: Personal portfolio website with integrated AI assistant agents
- **Tech Stack**: HTML5, CSS3, JavaScript (Frontend) + Python/Google ADK (AI Agents)
- **Deployment**: GitHub Pages with automated CI/CD

## 🏗️ Project Structure

```
my_platform_porto/
├── 🌐 Frontend (Portfolio Website)
│   ├── index.html              # Main portfolio page
│   ├── style.css              # Comprehensive styling with dark/light themes
│   ├── javascript.js          # Interactive functionality & animations
│   └── resources/             # Assets directory
│       ├── projects/          # Project screenshots (12 images)
│       ├── Docs/             # Documentation files
│       └── *.svg, *.jpg      # Icons and images
│
├── 🤖 AI Assistant Agents
│   ├── secretary_guest_agent/     # Visitor message & appointment handling
│   ├── secretary_chat_agent/      # Portfolio inquiry responses
│   ├── secretary_planning_agent/  # Daily itinerary management
│   ├── Project_manage_agent/      # Task tracking & Git workflows
│   └── requirements.txt           # Python dependencies
│
├── 📄 Documents
│   ├── olivier_bigirimana_Master_CV.docx
│   ├── Olivier_BIGIRIMANA_cover_letter.docx
│   └── CNAME                      # Custom domain configuration
│
└── ⚙️ Configuration
    ├── .github/workflows/static.yml  # GitHub Pages deployment
    ├── .gitignore                     # Git ignore rules
    └── **/.env                        # Environment configurations
```

## 🌐 Frontend Components

### 1. **index.html** - Main Portfolio Page
- **Sections**: Hero, About, Skills, Projects, Resume, Contact
- **Features**: 
  - Responsive design with mobile navigation
  - Dark/light theme toggle
  - Smooth scrolling navigation
  - Contact form integration
  - Social media links
- **Projects Showcased**: 
  - BBIS Banking Platform
  - Ikanisa Church Management
  - Human Justice API
  - Good Life Wellness Platform

### 2. **style.css** - Advanced Styling System
- **Theme System**: CSS variables for dark/light modes
- **Animations**: 
  - Profile image bounce & glow effects
  - Gradient animations on buttons
  - Floating elements around profile
  - Skill bar progress animations
- **Responsive Design**: Mobile-first approach with breakpoints
- **Interactive Elements**: Hover effects, transitions, backdrop filters

### 3. **javascript.js** - Interactive Functionality
- **Navigation**: Smooth scrolling, active link highlighting
- **Theme Management**: Dark/light mode with localStorage persistence
- **Mobile Features**: Hamburger menu, touch-friendly interactions
- **Animations**: Intersection Observer for scroll-triggered animations
- **Form Handling**: Contact form validation and submission
- **Project Filtering**: Dynamic project category filtering

## 🤖 AI Assistant Agents System

### Architecture
- **Framework**: Google ADK (Agent Development Kit)
- **Model**: Gemini 2.0 Flash / Gemini 1.5 Flash
- **Pattern**: Multi-agent system with specialized roles

### 1. **Secretary Guest Agent** (`secretary_guest_agent/`)
```python
# Core Functions:
- take_message(visitor_name, message) → Message storage
- schedule_appointment(visitor_name, date_time, purpose) → Calendar management
```
- **Purpose**: Handle visitor interactions and appointment scheduling
- **Features**: In-memory calendar system, message logging

### 2. **Secretary Chat Agent** (`secretary_chat_agent/`)
```python
# Core Functions:
- answer_inquiries(prompt) → Portfolio-based responses
- load_html_text() → Portfolio content extraction
- load_docx_text() → CV/Cover letter parsing
```
- **Purpose**: Answer visitor questions about Olivier's background
- **Data Sources**: Portfolio HTML, CV, Cover Letter
- **Features**: Document parsing with BeautifulSoup and python-docx

### 3. **Secretary Planning Agent** (`secretary_planning_agent/`)
```python
# Core Functions:
- daily_itinerary() → Today's appointment summary
```
- **Purpose**: Generate daily schedules and itineraries
- **Integration**: Shares calendar data with guest agent

### 4. **Project Manager Agent** (`Project_manage_agent/`)
```python
# Core Functions:
- add_task(description, due_date, priority, tags)
- update_task_status(task_id, new_status)
- add_project_doc(title, url, type, description)
- generate_git_workflow_summary(branch_name, feature_description)
- set_reminder(text, date, type)
- get_project_summary(days_back)
```
- **Purpose**: Comprehensive project management and Git workflow assistance
- **Features**: Task tracking, documentation management, Git workflow generation

## 📦 Dependencies & Technologies

### Frontend
- **Fonts**: Google Fonts (Poppins)
- **Icons**: Font Awesome 6.0.0
- **Styling**: Pure CSS3 with advanced features
- **JavaScript**: Vanilla ES6+ with modern APIs

### Backend (AI Agents)
```txt
Key Dependencies:
├── google-adk==1.13.0           # Agent Development Kit
├── google-genai==1.32.0         # Gemini AI integration
├── fastapi==0.116.1             # Web framework
├── beautifulsoup4==4.13.5       # HTML parsing
├── python-docx==1.2.0           # Word document processing
├── pydantic==2.11.7             # Data validation
└── uvicorn==0.35.0              # ASGI server
```

## 🚀 Deployment & CI/CD

### GitHub Pages Configuration
- **Workflow**: `.github/workflows/static.yml`
- **Trigger**: Push to main branch + manual dispatch
- **Process**: Automated deployment of entire repository
- **Domain**: Custom domain via CNAME (bigirimanaolivier.io)

### Environment Configuration
- **API Keys**: Google AI Studio API key in `.env` files
- **Security**: `.env` files gitignored for security
- **Vertex AI**: Configurable (currently disabled)

## 🎨 Design Features

### Visual Elements
- **Color Scheme**: Purple/blue gradients with cyan accents
- **Typography**: Poppins font family with varied weights
- **Layout**: CSS Grid and Flexbox for responsive design
- **Animations**: Smooth transitions and hover effects

### User Experience
- **Accessibility**: ARIA labels, keyboard navigation
- **Performance**: Optimized images, efficient CSS
- **Mobile-First**: Responsive design with touch interactions
- **Theme Support**: System preference detection + manual toggle

## 📊 Project Metrics

### Codebase Statistics
- **Total Files**: ~50+ files
- **Frontend**: 3 core files (HTML, CSS, JS)
- **AI Agents**: 4 specialized agents
- **Assets**: 20+ images and icons
- **Documentation**: 3 professional documents

### Features Count
- **Portfolio Sections**: 6 main sections
- **AI Agent Functions**: 10+ specialized functions
- **Interactive Elements**: 15+ animated components
- **Responsive Breakpoints**: 3 device categories

## 🔧 Development Workflow

### Git Workflow (Automated via Project Manager Agent)
1. Feature branch creation
2. Development and testing
3. Commit with conventional messages
4. Push and PR creation
5. Review and merge process

### Local Development
```bash
# Frontend: Open index.html in browser
# AI Agents: Python environment with requirements.txt
pip install -r my_assistant_agents/requirements.txt
```

## 🎯 Key Strengths

1. **Multi-Modal System**: Combines static portfolio with intelligent agents
2. **Professional Design**: Modern, responsive, and accessible
3. **Scalable Architecture**: Modular agent system for easy expansion
4. **Automated Deployment**: Seamless CI/CD pipeline
5. **Comprehensive Documentation**: Well-structured codebase with clear separation

## 🔮 Future Enhancement Opportunities

1. **Database Integration**: Replace in-memory storage with persistent DB
2. **Real-time Features**: WebSocket integration for live chat
3. **Advanced AI**: Multi-modal capabilities (voice, image processing)
4. **Analytics**: User interaction tracking and insights
5. **API Gateway**: Centralized API management for agents

---

**Last Updated**: January 2025  
**Maintainer**: Olivier Bigirimana  
**Status**: Active Development