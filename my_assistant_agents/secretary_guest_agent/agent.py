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
        # Simple message routing based on keywords
        if "schedule" in message.lower() or "appointment" in message.lower():
            return "I'd be happy to help schedule an appointment! Please provide your name, preferred date/time, and the purpose of the meeting."
        elif "message" in message.lower():
            return "I've noted your message. Olivier will get back to you soon!"
        else:
            return "Hello! I can help you schedule appointments with Olivier or take messages. How can I assist you?"

root_agent = GuestAgent()
