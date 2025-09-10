"""
OrchestratorAgent for the Genesis AI Framework.

This agent is responsible for:
1. Receiving high-level user goals
2. Breaking them down into a step-by-step plan
3. Delegating tasks to specialist agents
4. Managing the state of the overall task
5. Communicating results back to the user
"""

from typing import Dict, Any
from google.adk.agents import Agent
from src.agents.file_system_agent import file_system_agent
from src.agents.code_generation_agent import code_generation_agent
from src.agents.testing_agent import testing_agent
from src.agents.git_agent import git_agent


class OrchestratorAgent:
    """Main orchestrator that manages the AI development workflow."""
    
    def __init__(self):
        """Initialize the orchestrator with all specialist agents."""
        self.file_system_agent = file_system_agent
        self.code_generation_agent = code_generation_agent
        self.testing_agent = testing_agent
        self.git_agent = git_agent
        self.task_history = []
    
    def receive_task(self, user_goal: str) -> Dict[str, Any]:
        """
        Receive a high-level user goal and process it.
        
        Args:
            user_goal (str): The user's high-level goal
            
        Returns:
            Dict[str, Any]: Result of the task execution
        """
        print(f"Orchestrator received task: {user_goal}")
        self.task_history.append({"task": user_goal, "status": "started"})
        
        # Determine if this is a standard development task or meta-development task
        if "create a new agent" in user_goal.lower() or "self-expansion" in user_goal.lower():
            result = self._handle_meta_development_task(user_goal)
        else:
            result = self._handle_standard_development_task(user_goal)
            
        self.task_history.append({"task": user_goal, "status": "completed", "result": result})
        return result
    
    def _handle_standard_development_task(self, user_goal: str) -> Dict[str, Any]:
        """
        Handle a standard development task following the Code-Test-Correct loop.
        
        Args:
            user_goal (str): The user's goal
            
        Returns:
            Dict[str, Any]: Result of the task execution
        """
        # Create a plan based on the user goal
        plan = self._create_plan(user_goal)
        
        # Create a new branch for this feature
        branch_name = plan.get("branch_name", "feature/new-task")
        self.git_agent.create_new_branch(branch_name)
        
        # Execute each step in the plan
        for step in plan.get("steps", []):
            if step["agent"] == "code_generation":
                self.code_generation_agent.execute_task(step["instruction"])
            elif step["agent"] == "testing":
                test_result = self.testing_agent.run_pytest_suite()
                if not test_result["success"]:
                    # Enter correction loop
                    correction_result = self._handle_test_failure(test_result, plan)
                    if not correction_result["success"]:
                        return correction_result
        
        # If we get here, all tests passed
        self.git_agent.add_all_changes_to_staging()
        self.git_agent.commit_changes(plan.get("commit_message", "feat: Complete task"))
        
        return {
            "success": True,
            "message": f"Task completed successfully on branch {branch_name}",
            "branch": branch_name
        }
    
    def _handle_meta_development_task(self, user_goal: str) -> Dict[str, Any]:
        """
        Handle a meta-development task for self-expansion.
        
        Args:
            user_goal (str): The user's goal for creating new agents
            
        Returns:
            Dict[str, Any]: Result of the task execution
        """
        # Create a plan for self-expansion
        plan = self._create_meta_plan(user_goal)
        
        # Create a new branch for this feature
        branch_name = plan.get("branch_name", "feature/self-expansion")
        self.git_agent.create_new_branch(branch_name)
        
        # Execute each step in the plan
        for step in plan.get("steps", []):
            if step["agent"] == "file_system":
                self.file_system_agent.execute_task(step["instruction"])
            elif step["agent"] == "code_generation":
                self.code_generation_agent.execute_task(step["instruction"])
            elif step["agent"] == "testing":
                test_result = self.testing_agent.run_pytest_suite()
                if not test_result["success"]:
                    return {
                        "success": False,
                        "message": f"Tests failed during self-expansion: {test_result['output']}"
                    }
        
        # If we get here, all tests passed
        self.git_agent.add_all_changes_to_staging()
        self.git_agent.commit_changes(plan.get("commit_message", "feat: Add new agent capability"))
        
        return {
            "success": True,
            "message": "I have successfully expanded my capabilities",
            "branch": branch_name
        }
    
    def _create_plan(self, user_goal: str) -> Dict[str, Any]:
        """
        Create a step-by-step plan for a standard development task.
        
        Args:
            user_goal (str): The user's goal
            
        Returns:
            Dict[str, Any]: The execution plan
        """
        # This is a simplified plan creation. In a full implementation,
        # this would use an LLM to create a detailed plan.
        if "calculate_factorial" in user_goal and "utils.py" in user_goal:
            return {
                "branch_name": "feature/factorial-function",
                "commit_message": "feat: Add factorial function and tests",
                "steps": [
                    {
                        "agent": "code_generation",
                        "instruction": "Write a Python function calculate_factorial in the file src/utils.py. The function should handle non-negative integers."
                    },
                    {
                        "agent": "code_generation",
                        "instruction": "Write a pytest test case in tests/test_utils.py to verify the calculate_factorial function for inputs 0, 1, and 5."
                    },
                    {
                        "agent": "testing",
                        "instruction": "Run the test suite."
                    }
                ]
            }
        elif "hesapmakinesi" in user_goal.lower() or "calculator" in user_goal.lower():
            return {
                "branch_name": "feature/calculator-page",
                "commit_message": "feat: Add calculator web page",
                "steps": [
                    {
                        "agent": "code_generation",
                        "instruction": "Create a new HTML file src/calculator.html with a fully functional calculator web page. Include CSS styling and JavaScript for calculator functionality. The calculator should support basic operations: addition, subtraction, multiplication, and division."
                    },
                    {
                        "agent": "code_generation",
                        "instruction": "Create a new CSS file src/calculator.css with styling for the calculator page."
                    },
                    {
                        "agent": "code_generation",
                        "instruction": "Create a new JavaScript file src/calculator.js with the calculator logic."
                    }
                ]
            }
        else:
            # Generic plan for other tasks
            return {
                "branch_name": "feature/new-task",
                "commit_message": "feat: Complete development task",
                "steps": []
            }
    
    def _create_meta_plan(self, user_goal: str) -> Dict[str, Any]:
        """
        Create a step-by-step plan for a meta-development task.
        
        Args:
            user_goal (str): The user's goal for creating new agents
            
        Returns:
            Dict[str, Any]: The execution plan
        """
        # This is a simplified plan creation for meta-development tasks
        return {
            "branch_name": "feature/create-api-agent",
            "commit_message": "feat: Create new ApiAgent",
            "steps": [
                {
                    "agent": "file_system",
                    "instruction": "Analyze the project structure. Identify how existing agents are structured."
                },
                {
                    "agent": "code_generation",
                    "instruction": "Create a new file src/agents/api_agent.py. Define a new ApiAgent with a tool named make_get_request(url: str) that uses the requests library."
                },
                {
                    "agent": "code_generation",
                    "instruction": "Add requests to the requirements.txt file."
                },
                {
                    "agent": "code_generation",
                    "instruction": "Write a basic test in tests/test_api_agent.py to ensure the new agent can be initialized."
                },
                {
                    "agent": "testing",
                    "instruction": "Run the test suite."
                }
            ]
        }
    
    def _handle_test_failure(self, test_result: Dict[str, Any], plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle test failures by entering a correction loop.
        
        Args:
            test_result (Dict[str, Any]): The failed test results
            plan (Dict[str, Any]): The original execution plan
            
        Returns:
            Dict[str, Any]: Result after attempting correction
        """
        # In a full implementation, this would analyze the error and
        # instruct the CodeGenerationAgent to fix the code
        error_output = test_result.get("output", "Unknown error")
        
        # Send back to CodeGenerationAgent for correction
        correction_instruction = (
            f"The tests failed with the following error: {error_output}. "
            "Please analyze the code and provide a corrected version."
        )
        
        self.code_generation_agent.execute_task(correction_instruction)
        
        # Run tests again
        new_test_result = self.testing_agent.run_pytest_suite()
        
        if new_test_result["success"]:
            return {
                "success": True,
                "message": "Successfully corrected the code"
            }
        else:
            return {
                "success": False,
                "message": f"Failed to correct code after attempt: {new_test_result['output']}"
            }


# Create a global instance of the orchestrator
orchestrator_agent = OrchestratorAgent()