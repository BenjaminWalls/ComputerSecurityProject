import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes



def encryption(data):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB)
    ct_bytes = cipher.encrypt(data)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    with open('text.json', 'w') as file:
        json.dump({'iv':iv, 'ciphertext':ct}, file)
    result = json.dumps({'iv':iv, 'ciphertext':ct})

    b64 = json.loads(result)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    pt = cipher.decrypt(ct)   
    return pt.decode()
    