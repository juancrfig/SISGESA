import json
import hashlib
import sys

def crear_estructura_json():
    data = {
        "grupos": {}
    }
    with open('./app_data/data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def check_first_time():
    with open('./app_data/password.json', 'a+') as pass_file:
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
    with open('./app_data/password.json', 'w+' ) as file:
        json.dump(info, file)

def check_correct_login(user, password):

    with open('./app_data/password.json') as file:
        data = json.load(file)
    
    
    if user == data['user'] and data_encryption(password) == data['password']:
        return 0
    else:
        return 401

def change_password(user, password):
    
    info = {
        'user': user,
        'password': data_encryption(password)
    }

    with open('./app_data/password.json', 'w+') as file:
        json.dump(info, file)

def cargar_grupo(codigo, nombre, sigla):

    with open('./app_data/data.json') as file:
        data = json.load(file)

    data["grupos"][codigo] = [nombre, sigla]

    with open('./app_data/data.json', 'w+') as file:
        json.dump(data, file, indent=4)