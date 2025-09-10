"""
Web application for the Genesis AI Framework.

This module provides a web interface that exposes the OrchestratorAgent
and allows users to interact with the Genesis AI system through a web UI.
"""

import json
from typing import Dict, Any
from flask import Flask, request, jsonify, render_template_string

# Import our agents
from src.agents.orchestrator_agent import orchestrator_agent

app = Flask(__name__)

# Simple HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Genesis AI Framework</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; text-align: center; }
        textarea { width: 100%; height: 100px; padding: 10px; border: 1px solid #ddd; border-radius: 4px; margin: 10px 0; }
        button { background-color: #4CAF50; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer; width: 100%; }
        button:hover { background-color: #45a049; }
        .result { margin-top: 20px; padding: 15px; background-color: #e9f7ef; border-left: 6px solid #4CAF50; }
        .task-history { margin-top: 30px; }
        .task-item { padding: 10px; border-bottom: 1px solid #eee; }
        pre { white-space: pre-wrap; word-wrap: break-word; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Genesis AI Framework</h1>
        <p>Enter a task for the Genesis AI system:</p>
        
        <form id="taskForm">
            <textarea id="taskInput" placeholder="Example: Add a function named calculate_factorial to the utils.py file and write a test for it."></textarea>
            <button type="submit">Submit Task</button>
        </form>
        
        <div id="result" class="result" style="display: none;">
            <h3>Result:</h3>
            <pre id="resultContent"></pre>
        </div>
        
        <div class="task-history">
            <h3>Task History:</h3>
            <div id="taskHistory"></div>
        </div>
    </div>

    <script>
        document.getElementById('taskForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const taskInput = document.getElementById('taskInput').value;
            if (!taskInput.trim()) return;
            
            // Show loading
            document.getElementById('result').style.display = 'block';
            document.getElementById('resultContent').textContent = 'Processing task...';
            
            // Send task to backend
            fetch('/api/task', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ task: taskInput })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('resultContent').textContent = JSON.stringify(data, null, 2);
                updateTaskHistory();
            })
            .catch(error => {
                document.getElementById('resultContent').textContent = 'Error: ' + error;
            });
        });
        
        function updateTaskHistory() {
            fetch('/api/history')
            .then(response => response.json())
            .then(data => {
                const historyDiv = document.getElementById('taskHistory');
                historyDiv.innerHTML = '';
                
                data.forEach(task => {
                    const taskDiv = document.createElement('div');
                    taskDiv.className = 'task-item';
                    taskDiv.innerHTML = '<strong>Task:</strong> ' + task.task + '<br><strong>Status:</strong> ' + task.status;
                    if (task.result) {
                        taskDiv.innerHTML += '<br><strong>Result:</strong> ' + JSON.stringify(task.result);
                    }
                    historyDiv.appendChild(taskDiv);
                });
            });
        }
        
        // Load task history on page load
        updateTaskHistory();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Serve the main web interface."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/task', methods=['POST'])
def execute_task():
    """Execute a task using the OrchestratorAgent."""
    try:
        data = request.get_json()
        task = data.get('task', '')
        
        if not task:
            return jsonify({'error': 'No task provided'}), 400
        
        # Use the orchestrator agent to process the task
        result = orchestrator_agent.receive_task(task)
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history')
def get_task_history():
    """Get the task history from the OrchestratorAgent."""
    try:
        return jsonify(orchestrator_agent.task_history)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/agents')
def list_agents():
    """List all available agents."""
    try:
        agents = [
            'OrchestratorAgent',
            'FileSystemAgent',
            'CodeGenerationAgent',
            'TestingAgent',
            'GitAgent'
        ]
        return jsonify({'agents': agents})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)