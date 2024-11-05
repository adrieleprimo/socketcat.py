from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

keySize = 32

class aesCipher:
    def __init__(self, key):
        self.key = key[:keySize].ljust(keySize, b'\0')
    
    def encrypt(self, data):
        iv = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encryptedData = cipher.encrypt(pad(data.encode(), AES.block_size))
        return base64.b64encode(iv + encryptedData).decode()
    
    def decrypt(self, encryptedData):
        rawData = base64.b64decode(encryptedData)
        iv = rawData[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(encryptedData), AES.block_size).decode()