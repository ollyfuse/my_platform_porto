# In-memory calendar (for demo; later you can integrate Google Calendar)
calendar = []

def take_message(visitor_name: str, message: str) -> dict:
    return {"status": "success", "report": f"Message from {visitor_name}: '{message}' saved."}

def schedule_appointment(visitor_name: str, date_time: str, purpose: str) -> dict:
    entry = {"visitor": visitor_name, "datetime": date_time, "purpose": purpose}
    calendar.append(entry)
    return {"status": "success", "report": f"Appointment scheduled: {entry}"}

class GuestAgent:
    async def run_async(self, message: str) -> str:
        message_lower = message.lower()
        
        if "schedule" in message_lower or "appointment" in message_lower or "meeting" in message_lower:
            return "📅 I'd be happy to help schedule an appointment with Olivier! Please provide:\n\n👤 Your name\n🕰️ Preferred date/time\n🎯 Purpose of the meeting\n\nI'll make sure Olivier gets all the details!"
        elif "message" in message_lower or "note" in message_lower:
            return "📝 I've noted your message for Olivier. He'll get back to you soon! Is there anything specific you'd like me to include?"
        elif "available" in message_lower or "free" in message_lower:
            return "🕰️ Olivier is generally available for meetings Monday-Friday, 9 AM - 5 PM EAT. Would you like to schedule something specific?"
        else:
            return "👋 Hello! I'm Olivier's scheduling assistant. I can help you:\n\n📅 Schedule appointments\n📝 Take messages\n🕰️ Check availability\n\nHow can I assist you today?"

root_agent = GuestAgent()
