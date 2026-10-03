from dotenv import load_dotenv
import os

from agno.agent import Agent
from agno.models.groq import Groq

# Load .env file
load_dotenv()

# Check Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in your .env file")

# Create Agno Agent using Groq
agno_agent = Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    description="Agno Q&A agent",
    markdown=False
)

# Ask question
agno_agent.print_response(
    "write a python program to find the largest number in list?",
    stream=True
)