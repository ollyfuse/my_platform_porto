import datetime

class PlanningAgent:
    def __init__(self):
        self.calendar = []
    
    async def run_async(self, message: str) -> str:
        message_lower = message.lower()
        
        if "today" in message_lower or "schedule" in message_lower:
            today = datetime.date.today().strftime("%Y-%m-%d")
            today_appointments = [appt for appt in self.calendar if appt.get("datetime", "").startswith(today)]
            
            if not today_appointments:
                return f"No appointments scheduled for today ({today}). Your day is free!"
            
            itinerary = "\n".join([f"• {a['datetime']}: {a['visitor']} - {a['purpose']}" for a in today_appointments])
            return f"Today's schedule ({today}):\n{itinerary}"
        
        elif "week" in message_lower:
            return "Weekly planning feature coming soon! Currently showing daily schedules."
        
        else:
            return "I can help you with daily planning and scheduling. Ask me about 'today's schedule' or 'this week's plan'."

root_agent = PlanningAgent()