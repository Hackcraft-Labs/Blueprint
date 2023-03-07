from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from os import urandom
import hashlib

FILTER_NAME = "aes"
KEY = None
IV = None


def init():
    global KEY
    global IV

    KEY = bytes(urandom(16))
    IV = bytes(urandom(16))

    key_str = ""
    for b in KEY:
        key_str += "{:02x}".format(b)

    iv_str = ""
    for b in IV:
        iv_str += "{:02x}".format(b)

    print("[*] Generated random AES Key: " + key_str)
    print("[*] Generated random AES IV: " + iv_str)


def variables(variables: dict):
    global KEY
    global IV

    variables["AES_KEY"] = KEY
    variables["AES_IV"] = IV

    return variables


def filter(input) -> str:
    global KEY
    global IV

    print("[DBG] Running aes.")

    plain_padded = pad(input, 16)
    cipher = AES.new(hashlib.sha256(KEY).digest(), AES.MODE_CBC, IV)
    cipher_text = cipher.encrypt(plain_padded)

    return cipher_text
