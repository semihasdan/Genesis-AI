"""
Main entry point for the Genesis AI Framework web application.
"""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.web_app import app

if __name__ == '__main__':
    print("Starting Genesis AI Framework web interface...")
    print("Access the interface at http://127.0.0.1:8000")
    app.run(host='127.0.0.1', port=8000, debug=True)