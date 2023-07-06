import base64
import os
import hashlib

print(hashlib.sha256(b"password").hexdigest())

user_name = "user"
user_pass = "password"
db = {}

salt = base64.b64encode(os.urandom(32))


def get_digest(password):
    # b_password = bytes(password, 'utf-8')
    # digest = hashlib.sha256(salt + b_password).hexdigest()
    # for _ in range(10000):
    #     digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
    digest = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), salt, 10000).hex()
    return digest


db[user_name] = get_digest(user_pass)


def is_login(user_name, password):
    return db.get(user_name) == get_digest(password)


print(is_login(user_name, user_pass))
print(is_login(user_name, "password2"))
