from openai import OpenAI
from dotenv import load_dotenv
from schemas import CalendarEvent
from utils import get_image
from google_calendar import create_event
# Loads environment variables
load_dotenv()

# Creates client for OpenAI endpoint
client = OpenAI()

# Prompt to give to llm
PROMPT = """Extract calendar event information from this image and return it in the following JSON structure:

{
    "name": "Event title/name",
    "date": {
        "start_hour": <0-23>,
        "end_hour": <0-23>,
        "start_minute": <0-59>,
        "end_minute": <0-59>,
        "start_date": "YYYY-MM-DD",
        "end_date": "YYYY-MM-DD",
        "time_zone": "Timezone identifier"
    },
    "location": "Physical or virtual location (or None if not specified)"
}

Requirements:
- Use 24-hour format for hours (0-23)
- Dates must be in YYYY-MM-DD format
- For timezone: use IANA format (e.g., "America/New_York", "Europe/London") if detectable from context, abbreviation (e.g., "EST", "PST") if shown, or "America/New_York" as default if not specified
- If the event is on a single day, start_date and end_date should be the same
- For location: if it's a physical address, provide the full formatted address (e.g., "123 Main St, New York, NY 10001"); if it's a building/room name, include building name and room number; if it's a virtual meeting, include the platform (e.g., "Zoom", "Microsoft Teams"); set to None if not specified
- If end time is not visible: Estimate end time based on context of the title, else default to 1 hour length from start time
- Extract all visible time and date information accurately

Analyze the image carefully and extract the event details."""

# The role of the llm
ROLE = "user"

response = client.responses.parse(
    model="gpt-5-mini-2025-08-07",
    input=[
        {
            'role': ROLE,
            'content': [
                {"type": "input_text", "text":PROMPT},
                {"type": "input_image", "image_url": get_image(3)}
            ]
        }
    ],
    text_format=CalendarEvent
)

# Parse the response into CalendarEvent object
event_data = CalendarEvent.model_validate_json(response.output_text)
print("Extracted event:", event_data)

# Create the Google Calendar event
created_event = create_event(event_data)
print(f"\n✅ Event created: {created_event.get('htmlLink')}")
