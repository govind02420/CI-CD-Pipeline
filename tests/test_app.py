# import app

# def test_home():
#     assert app.home() == 'Hello, Simple Python web application!'
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import app
