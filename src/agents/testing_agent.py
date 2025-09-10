"""
TestingAgent for the Genesis AI Framework.

This agent is responsible for:
1. Running the test suite
2. Reporting test results in a structured way
"""

import subprocess
import sys
from typing import Dict, Any, Union
from google.adk.agents import Agent


class TestingAgent:
    """Agent specialized in running tests and reporting results."""
    
    def __init__(self):
        """Initialize the testing agent."""
        pass
    
    def run_pytest_suite(self) -> Dict[str, Union[bool, str]]:
        """
        Execute pytest in the project's root directory.
        
        Returns:
            Dict[str, Union[bool, str]]: Test results with success status and output
        """
        try:
            # Run pytest and capture output
            result = subprocess.run(
                [sys.executable, "-m", "pytest", "-v"],
                capture_output=True,
                text=True,
                cwd="."
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout if result.returncode == 0 else result.stderr
            }
        except Exception as e:
            return {
                "success": False,
                "output": f"Error running pytest: {str(e)}"
            }
    
    def execute_task(self, instruction: str) -> Dict[str, Any]:
        """
        Execute a testing task based on natural language instruction.
        
        Args:
            instruction (str): Natural language instruction for the task
            
        Returns:
            Dict[str, Any]: Result of the task execution
        """
        print(f"TestingAgent executing task: {instruction}")
        
        # For now, we just run the full test suite
        # In a full implementation, we might run specific tests
        result = self.run_pytest_suite()
        
        return {
            "success": True,
            "message": f"Executed testing task: {instruction}",
            "test_result": result
        }


# Create a global instance of the testing agent
testing_agent = TestingAgent()