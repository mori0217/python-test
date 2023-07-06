from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Padding
from hashlib import pbkdf2_hmac


def encrypt(text, passPhrase):
    salt = get_random_bytes(16)
    iv = get_random_bytes(16)
    # AESキーの生成(128bit、5万回)
    key = pbkdf2_hmac('sha256', bytes(passPhrase, encoding='utf-8'), salt, 50000, int(128 / 8))
    # 暗号
    aes = AES.new(key, AES.MODE_CBC, iv)
    data = Padding.pad(text.encode('utf-8'), AES.block_size, 'pkcs7')
    encrypted = aes.encrypt(data)

    return {
        'salt': salt,
        'iv': iv,
        'encrypted': encrypted
    }


def decrypt(encryptedData, passPhrase):
    # AESキーの生成(128bit、5万回)
    key = pbkdf2_hmac('sha256', bytes(passPhrase, encoding='utf-8'), encryptedData['salt'], 50000, int(128 / 8))
    # 復号
    aes = AES.new(key, AES.MODE_CBC, encryptedData['iv'])
    plaintext = aes.decrypt(encryptedData['encrypted'])
    return plaintext.decode(encoding='utf-8')


targetText = "Hello World!"
passPhrase = "password123"

encryptedData = encrypt(targetText, passPhrase)
print(encryptedData)
decrypted = decrypt(encryptedData, passPhrase)
print(decrypted)
