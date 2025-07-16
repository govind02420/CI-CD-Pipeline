# import sys
# import os

# # Add the parent directory to the Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app

def test_home():
    tester = app.app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

#------------------------------------

# import app

# def test_home_page():
#     response = app.app.test_client().get('/')
#     assert response.status_code == 200

#------------------------------------

# import app

# def test_home():
#     assert app.home() == 'Hello, Simple Python web application!'
#------------------------------------

