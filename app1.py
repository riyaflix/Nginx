from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Server 1'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)
