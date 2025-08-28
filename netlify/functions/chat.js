exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  try {
    const { message, agent_type } = JSON.parse(event.body);
    
    let response = '';
    
    switch (agent_type) {
      case 'chat':
        response = `Hi! I'm Olivier's AI assistant. You asked: "${message}". I can tell you about his experience, skills, projects, education, or contact information.`;
        break;
      case 'guest':
        response = `I'd be happy to help schedule an appointment! Please provide your name, preferred date/time, and the purpose of the meeting.`;
        break;
      case 'planning':
        response = `I can help you with daily planning and scheduling. Ask me about today's schedule or this week's plan.`;
        break;
      case 'project':
        response = `I'm your project management assistant! I can help with tasks, Git workflows, project summaries, and reminders.`;
        break;
      default:
        response = `Hello! How can I assist you today?`;
    }

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
      },
      body: JSON.stringify({
        response,
        agent: agent_type,
        status: 'success'
      })
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Internal server error' })
    };
  }
};