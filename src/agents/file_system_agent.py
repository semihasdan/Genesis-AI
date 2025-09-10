"""
FileSystemAgent for the Genesis AI Framework.

This agent is responsible for:
1. Navigating the project's file structure
2. Reading file contents
3. Writing to files
4. Listing directory contents
"""

import os
from typing import List, Dict, Any
from google.adk.agents import Agent


class FileSystemAgent:
    """Agent specialized in file system operations."""
    
    def __init__(self):
        """Initialize the file system agent."""
        pass
    
    def read_file(self, filepath: str) -> str:
        """
        Read the content of a file.
        
        Args:
            filepath (str): Path to the file to read
            
        Returns:
            str: Content of the file
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"Error reading file {filepath}: {str(e)}"
    
    def write_to_file(self, filepath: str, content: str) -> bool:
        """
        Write or overwrite a file.
        
        Args:
            filepath (str): Path to the file to write
            content (str): Content to write to the file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Error writing to file {filepath}: {str(e)}")
            return False
    
    def list_directory(self, path: str) -> List[str]:
        """
        List the contents of a directory.
        
        Args:
            path (str): Path to the directory to list
            
        Returns:
            List[str]: List of items in the directory
        """
        try:
            return os.listdir(path)
        except Exception as e:
            return [f"Error listing directory {path}: {str(e)}"]
    
    def execute_task(self, instruction: str) -> Dict[str, Any]:
        """
        Execute a file system task based on natural language instruction.
        
        Args:
            instruction (str): Natural language instruction for the task
            
        Returns:
            Dict[str, Any]: Result of the task execution
        """
        # In a full implementation, this would parse the instruction
        # and call the appropriate method
        print(f"FileSystemAgent executing task: {instruction}")
        
        # For now, we'll just return a success message
        return {
            "success": True,
            "message": f"Executed file system task: {instruction}"
        }


# Create a global instance of the file system agent
file_system_agent = FileSystemAgent()