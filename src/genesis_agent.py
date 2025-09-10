"""
Genesis Agent for the Genesis AI Framework.

This module creates an ADK-compatible agent that wraps the OrchestratorAgent
to make it available through the ADK web interface.
"""

from typing import Dict, Any
from google.adk.agents import Agent
from src.agents.orchestrator_agent import orchestrator_agent

# Create an ADK-compatible agent that wraps our OrchestratorAgent
genesis_agent = Agent(
    name="genesis_agent",
    model="gemini-2.5-flash",  # You can change this to your preferred model
    instruction="""
You are the Genesis AI, a self-expanding, multi-agent software development framework. 
Your capabilities include:

1. Standard Development Tasks:
   - Writing code and tests
   - Running tests and handling failures
   - Managing version control with Git

2. Meta-Development Tasks (Self-Expansion):
   - Creating new agents with new tools
   - Expanding your own skillset

When given a task, you will:
1. Break it down into a step-by-step plan
2. Delegate tasks to specialist agents (FileSystemAgent, CodeGenerationAgent, TestingAgent, GitAgent)
3. Manage the overall workflow following Test-Driven Development principles
4. Report results back to the user

For standard development tasks, follow the Code-Test-Correct loop.
For meta-development tasks, create new agents and tools as needed.
""",
    description="Self-expanding multi-agent software development framework",
    tools=[]  # The orchestrator manages tools internally
)

# We'll handle the orchestration logic in the process method
def process(user_input: str) -> Dict[str, Any]:
    """
    Process user input using the Genesis AI framework.
    
    Args:
        user_input (str): The user's request
        
    Returns:
        Dict[str, Any]: The result of processing the request
    """
    try:
        # Use our orchestrator agent to handle the task
        result = orchestrator_agent.receive_task(user_input)
        return result
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Attach the process function to the agent
genesis_agent.process = process