import app

def test_home():
    tester = app.app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

#------------------------------------
#------------------------------------

# import app

# def test_home():
#     assert app.home() == 'Hello, Simple Python web application!'
#------------------------------------

