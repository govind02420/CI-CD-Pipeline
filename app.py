from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Simple Python web application!'

# Only run the app when executed directly (not during testing)
if __name__ == '__main__':
    app.run(debug=True)

# Test function (can be discovered by pytest)
def test_math():
    assert 1 + 1 == 2
