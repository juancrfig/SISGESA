import json
import hashlib

def check_first_time():
    with open('password.json', 'a+') as pass_file:
        pass_file.seek(0)
        lines = pass_file.readlines()
        if lines:
            return False
        else:
            return True

def data_encryption(text):

    data = text.encode('utf-8')
    hash_objeto = hashlib.sha256(data)
    hash_hex = hash_objeto.hexdigest()
    return hash_hex

def register_new_user(info):
    with open('password.json', 'w+' ) as file:
        json.dump(info, file)
        
