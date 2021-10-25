from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Server 3'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5003)
