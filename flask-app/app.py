from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dosto, welcome to DevOps Zero To Hero - Batch-6'

@app.route('/health')
def health():
    return 'Server is up and running'
