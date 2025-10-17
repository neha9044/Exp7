# Assuming you applied the path fix:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import add

# 👇 Add a second blank line here
def test_add():
    assert add(2, 3) == 5