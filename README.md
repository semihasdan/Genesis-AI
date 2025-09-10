# Genesis AI Framework

## Project Concept

Genesis AI is a self-expanding, multi-agent software development framework built using Python and the Google Agent Development Kit (ADK). Its core capability is not only to perform software development tasks but also to autonomously create new agents with new tools, thereby expanding its own skillset. The system operates on a continuous feedback loop of coding, testing, and self-correction.

## Core Philosophy & Design Principles

1. **Separation of Concerns**: Each agent has a single, well-defined responsibility. An agent that writes code should not be the same agent that runs tests.

2. **Orchestration-Driven**: A central [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) manages the high-level plan, delegates tasks to specialist agents, and processes their results.

3. **Tool-Augmented Agents**: Agents do not perform complex logic within their prompts. Instead, they are given access to powerful Python functions (tools) that they can call to interact with the environment.

4. **Test-Driven Development (TDD) as a Core Loop**: The system must never commit code without first writing a test and successfully running it. If a test fails, the system must enter a self-correction loop.

5. **Metaprogramming & Self-Expansion**: The ultimate goal is for the system to be able to write the code for new agents and their corresponding tools, effectively teaching itself new skills.

## Technology Stack

- Language: Python 3.10+
- Framework: Google Agent Development Kit (ADK)
- Testing: Pytest
- Version Control: Git

## Directory Structure

```
genesis-ai/
├── README.md
├── requirements.txt
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── orchestrator_agent.py
│   │   ├── file_system_agent.py
│   │   ├── code_generation_agent.py
│   │   ├── testing_agent.py
│   │   └── git_agent.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── file_system_tools.py
│   │   ├── testing_tools.py
│   │   └── git_tools.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_utils.py
│   ├── test_file_system_tools.py
│   ├── test_testing_tools.py
│   └── test_git_tools.py
└── examples/
    └── factorial_task.py
```

## Key Agent Architecture

### OrchestratorAgent
- **Role**: The project manager that takes high-level user goals, breaks them down into a step-by-step plan, delegates tasks to specialist agents, and manages the state of the overall task.
- **Tools**: This agent does not have external tools. Its "tool" is its ability to invoke other agents.

### FileSystemAgent
- **Role**: The expert on navigating and manipulating the project's file structure.
- **Tools**:
  - `read_file(filepath: str) -> str`: Reads the content of a file.
  - `write_to_file(filepath: str, content: str) -> bool`: Writes or overwrites a file.
  - `list_directory(path: str) -> List[str]`: Lists the contents of a directory.

### CodeGenerationAgent
- **Role**: The programmer that writes new Python code based on specifications.
- **Tools**: Primarily uses the FileSystemAgent's tools to write its output.

### TestingAgent
- **Role**: The Quality Assurance specialist that runs the test suite.
- **Tools**:
  - `run_pytest_suite() -> Dict[str, Union[bool, str]]`: Executes pytest and returns structured results.

### GitAgent
- **Role**: The version control manager that handles all Git interactions.
- **Tools**:
  - `create_new_branch(branch_name: str) -> str`: Creates and checks out a new git branch.
  - `add_all_changes_to_staging() -> bool`: Executes `git add .`
  - `commit_changes(commit_message: str) -> bool`: Executes `git commit -m "message"`

## Key Workflows

### Workflow 1: Standard Development Task - "Code-Test-Correct Loop"

1. User Goal: "Add a function named calculate_factorial to the utils.py file and write a test for it."
2. [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) receives goal, creates a plan.
3. [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) → [GitAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/git_agent.py#L11-L65): "Create a new branch named feature/factorial-function."
4. [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) → [CodeGenerationAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/code_generation_agent.py#L10-L55): "Write a Python function calculate_factorial in the file src/utils.py."
5. [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) → [CodeGenerationAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/code_generation_agent.py#L10-L55): "Write a pytest test case in tests/test_utils.py."
6. [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) → [TestingAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/testing_agent.py#L11-L55): "Run the test suite."
7. Conditional Logic:
   - If successful: Commit changes and report completion
   - If failed: Loop back to correction

### Workflow 2: Meta-Development Task - "Self-Expansion"

1. User Goal: "Create a new agent called ApiAgent with a GET request tool."
2. [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) creates a plan for self-modification.
3. [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) → [GitAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/git_agent.py#L11-L65): "Create branch feature/create-api-agent."
4. [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) → [FileSystemAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/file_system_agent.py#L10-L60): "Analyze project structure."
5. [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) → [CodeGenerationAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/code_generation_agent.py#L10-L55): Create new agent file and update requirements.
6. [OrchestratorAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/orchestrator_agent.py#L10-L70) → [TestingAgent](file:///Users/semihasdan/Documents/software/python/adk/src/agents/testing_agent.py#L11-L55): "Run the test suite."
7. If successful: Stage and commit changes.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run an example:
   ```bash
   python examples/factorial_task.py
   ```

## Development Guidelines

1. All agents must follow the single responsibility principle
2. All code must be test-driven (write tests first)
3. All changes must be made in feature branches
4. All agents must be self-contained and well-documented