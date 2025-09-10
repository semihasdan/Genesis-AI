"""
ApiAgent for the Genesis AI Framework.

This agent is responsible for:
1. Making GET requests to APIs
2. Handling API responses
"""

import requests
from typing import Dict, Any
from google.adk.agents import Agent


class ApiAgent:
    """Agent specialized in making API requests."""
    
    def __init__(self):
        """Initialize the API agent."""
        pass
    
    def make_get_request(self, url: str) -> Dict[str, Any]:
        """
        Make a GET request to the specified URL.
        
        Args:
            url (str): The URL to make the GET request to
            
        Returns:
            Dict[str, Any]: The response from the API
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            return {
                "success": True,
                "status_code": response.status_code,
                "data": response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text
            }
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": str(e)
            }


# Create a global instance of the API agent
api_agent = ApiAgent()
