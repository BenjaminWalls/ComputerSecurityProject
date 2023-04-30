import json
from flask import Flask, render_template
from flask_socketio import SocketIO, send
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


app = Flask(__name__)
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)
    data = bytes(message, encoding= 'utf-8')
    
    
    key = get_random_bytes(16)
    # change key to be the message padded?


    cipher = AES.new(key, AES.MODE_CFB)
    ct_bytes = cipher.encrypt(data)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    with open('text.json', 'w') as file:
        json.dump({'iv':iv, 'ciphertext':ct}, file)
    result = json.dumps({'iv':iv, 'ciphertext':ct})

    
    with open('text.json', 'r') as myfile:
        text=myfile.read()
    b64 = json.loads(text)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    pt = cipher.decrypt(ct)

    mess = pt.decode() + " " + str(b64['ciphertext'])

    if message != "User connected!":
        send(mess, broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host="localhost")


