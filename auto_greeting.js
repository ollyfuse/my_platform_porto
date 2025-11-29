// Auto-greeting functionality for portfolio visitors
document.addEventListener('DOMContentLoaded', function() {
    // Auto-greeting when portfolio loads
    function showAutoGreeting() {
        if (!localStorage.getItem('portfolioVisited')) {
            setTimeout(() => {
                const chatToggle = document.getElementById('chatToggle');
                
                // Add pulsing animation to chat button
                chatToggle.style.animation = 'pulse 2s infinite';
                
                // Show notification bubble
                const notification = document.createElement('div');
                notification.className = 'chat-notification';
                notification.innerHTML = '💬 Hi! Ask me about Olivier\'s experience!';
                document.body.appendChild(notification);
                
                // Remove notification after 5 seconds
                setTimeout(() => {
                    if (notification.parentNode) {
                        notification.remove();
                    }
                    chatToggle.style.animation = '';
                }, 5000);
                
                localStorage.setItem('portfolioVisited', 'true');
            }, 3000); // Show after 3 seconds
        }
    }
    
    // Initialize auto-greeting
    showAutoGreeting();
    
    // Enhanced chat toggle with better greeting
    const chatToggle = document.getElementById('chatToggle');
    const chatWidget = document.getElementById('chatWidget');
    const chatMessages = document.getElementById('chatMessages');
    
    if (chatToggle) {
        chatToggle.addEventListener('click', () => {
            chatWidget.classList.toggle('active');
            if (chatWidget.classList.contains('active')) {
                setTimeout(() => {
                    const chatInput = document.getElementById('chatInput');
                    if (chatInput) chatInput.focus();
                }, 300);
                
                if (chatMessages && chatMessages.children.length === 0) {
                    setTimeout(() => {
                        const addMessage = window.addMessage;
                        if (addMessage) {
                            addMessage('👋 **Hello! I\'m Olivier\'s AI Assistant**\\n\\nI have complete access to his CV, portfolio, and professional background. I can answer detailed questions about his experience, skills, projects, and qualifications.\\n\\n*Try asking: \"Tell me about your CV\" or \"What projects have you built?\"*', 'bot');
                        }
                    }, 500);
                }
            }
        });
    }
});