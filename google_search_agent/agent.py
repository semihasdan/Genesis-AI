from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction="Answer questions using Google Search when needed. Always cite sources.",
    description="Professional search assistant with Google Search capabilities.",
    tools=[google_search]
)