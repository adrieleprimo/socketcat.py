import bcrypt

def setPassword(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    with open('passwordHash.txt', 'wb') as f:
        f.write(hashed)
    print('Password successfully configured!')

password = input('Password: ')
setPassword(password)