"""
Test script to create a calculator page using the Genesis AI Framework.
"""

import sys
import os

# Add the src directory to the path so we can import the agents
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.agents.orchestrator_agent import orchestrator_agent

def main():
    """Main function to test calculator creation."""
    print("Testing Genesis AI Framework - Calculator Creation")
    print("=" * 50)
    
    # Test creating a calculator page
    task = "web'de çalışan bir hesapmakinesi sayfası yap"
    result = orchestrator_agent.receive_task(task)
    print(f"Result: {result}")
    
    # Print task history
    print("\nTask History:")
    for task in orchestrator_agent.task_history:
        print(f"Task: {task.get('task', 'N/A')}")
        print(f"Status: {task.get('status', 'N/A')}")
        if 'result' in task:
            print(f"Result: {task['result']}")
        print("-" * 30)

if __name__ == "__main__":
    main()