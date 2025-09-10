"""
Example script demonstrating the Genesis AI Framework.

This script shows how to use the orchestrator to complete a simple task:
adding a factorial function to the utils module.
"""

import sys
import os

# Add the src directory to the path so we can import the agents
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.agents.orchestrator_agent import orchestrator_agent


def main():
    """Main function to demonstrate the framework."""
    print("Genesis AI Framework Demo")
    print("========================")
    
    # Example 1: Standard development task
    print("\\n1. Standard Development Task")
    task = "Add a function named calculate_factorial to the utils.py file and write a test for it."
    result = orchestrator_agent.receive_task(task)
    print(f"Result: {result}")
    
    # Example 2: Meta-development task
    print("\\n2. Meta-Development Task")
    task = "Create a new agent called ApiAgent. It needs a tool to make GET requests to an API."
    result = orchestrator_agent.receive_task(task)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()