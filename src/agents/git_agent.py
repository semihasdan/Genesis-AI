"""
GitAgent for the Genesis AI Framework.

This agent is responsible for:
1. Handling all interactions with Git
2. Creating branches
3. Staging changes
4. Committing changes
"""

import subprocess
import sys
import os
from typing import Dict, Any, Union
from google.adk.agents import Agent


class GitAgent:
    """Agent specialized in Git operations."""
    
    def __init__(self):
        """Initialize the Git agent."""
        pass
    
    def create_new_branch(self, branch_name: str) -> str:
        """
        Create and checkout a new git branch.
        
        Args:
            branch_name (str): Name of the branch to create
            
        Returns:
            str: Result of the branch creation
        """
        try:
            # Check if we're in a git repository
            if not self._is_git_repository():
                return "Error: Not in a git repository"
            
            # Create and checkout the new branch
            result = subprocess.run(
                ["git", "checkout", "-b", branch_name],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                return f"Successfully created and switched to branch: {branch_name}"
            else:
                # If branch already exists, just switch to it
                switch_result = subprocess.run(
                    ["git", "checkout", branch_name],
                    capture_output=True,
                    text=True
                )
                
                if switch_result.returncode == 0:
                    return f"Switched to existing branch: {branch_name}"
                else:
                    return f"Error creating/switching to branch: {result.stderr}"
                    
        except Exception as e:
            return f"Error creating branch {branch_name}: {str(e)}"
    
    def add_all_changes_to_staging(self) -> bool:
        """
        Execute git add . to stage all changes.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Check if we're in a git repository
            if not self._is_git_repository():
                print("Error: Not in a git repository")
                return False
            
            result = subprocess.run(
                ["git", "add", "."],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("Successfully staged all changes")
                return True
            else:
                print(f"Error staging changes: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"Error staging changes: {str(e)}")
            return False
    
    def commit_changes(self, commit_message: str) -> bool:
        """
        Execute git commit with the provided message.
        
        Args:
            commit_message (str): The commit message
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Check if we're in a git repository
            if not self._is_git_repository():
                print("Error: Not in a git repository")
                return False
            
            result = subprocess.run(
                ["git", "commit", "-m", commit_message],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"Successfully committed changes: {commit_message}")
                return True
            else:
                print(f"Error committing changes: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"Error committing changes: {str(e)}")
            return False
    
    def _is_git_repository(self) -> bool:
        """
        Check if the current directory is a git repository.
        
        Returns:
            bool: True if in a git repository, False otherwise
        """
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except:
            return False
    
    def execute_task(self, instruction: str) -> Dict[str, Any]:
        """
        Execute a Git task based on natural language instruction.
        
        Args:
            instruction (str): Natural language instruction for the task
            
        Returns:
            Dict[str, Any]: Result of the task execution
        """
        print(f"GitAgent executing task: {instruction}")
        
        # In a full implementation, this would parse the instruction
        # and call the appropriate method
        return {
            "success": True,
            "message": f"Executed Git task: {instruction}"
        }


# Create a global instance of the Git agent
git_agent = GitAgent()