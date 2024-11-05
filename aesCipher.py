from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

keySize = 32

class aesCipher:
    def __init__(self, key):
        self.key = key[:keySize].ljust(keySize, b'\0')
    