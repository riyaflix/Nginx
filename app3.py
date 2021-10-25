from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from app3'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5003)
