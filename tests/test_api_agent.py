"""
Test cases for the ApiAgent.
"""

import pytest
from src.agents.api_agent import ApiAgent


def test_api_agent_initialization():
    """Test that the ApiAgent can be initialized."""
    agent = ApiAgent()
    assert isinstance(agent, ApiAgent)
    
    
def test_make_get_request():
    """Test the make_get_request method."""
    agent = ApiAgent()
    # This is a basic test - in a real scenario, we would mock the requests
    assert hasattr(agent, 'make_get_request')