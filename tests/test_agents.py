"""
Test cases for agent initialization.
"""

import pytest


def test_orchestrator_agent_import():
    """Test that the OrchestratorAgent can be imported."""
    from src.agents.orchestrator_agent import orchestrator_agent
    assert orchestrator_agent is not None


def test_file_system_agent_import():
    """Test that the FileSystemAgent can be imported."""
    from src.agents.file_system_agent import file_system_agent
    assert file_system_agent is not None


def test_code_generation_agent_import():
    """Test that the CodeGenerationAgent can be imported."""
    from src.agents.code_generation_agent import code_generation_agent
    assert code_generation_agent is not None


def test_testing_agent_import():
    """Test that the TestingAgent can be imported."""
    from src.agents.testing_agent import testing_agent
    assert testing_agent is not None


def test_git_agent_import():
    """Test that the GitAgent can be imported."""
    from src.agents.git_agent import git_agent
    assert git_agent is not None