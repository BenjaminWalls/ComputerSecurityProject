import json
from flask import Flask, render_template
from flask_socketio import SocketIO, send

from AES import encryption

app = Flask(__name__)
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)
    encryption(b'hi')
    if message != "User connected!":
        send(message, broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host="localhost")
