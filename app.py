from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Simple Python web application!'

# Only run the app when executed directly (not during testing)
if __name__ == '__main__':
    app.run(debug=True)

