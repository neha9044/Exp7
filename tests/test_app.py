# Modified tests/test_app.py
import sys
import os

# Get the path to the project root (one level up from 'tests')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now, import app
from app import add

def test_add():
    assert add(2, 3) == 5