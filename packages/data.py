import json
import hashlib
from datetime import datetime, timedelta
from packages import art

def crear_estructura_json():
    data = {
        "grupos": {},
        "modulos": {},
        "alumnos": {},

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

    data["grupos"][codigo] = {"nombre": nombre, "sigla": sigla}

    with open('./app_data/data.json', 'w+') as file:
        json.dump(data, file, indent=4)

def pedir_horario():

    while True:

        print(art.modulo_mensaje6, end='')
        user_input_inicio = input()

        try:
            # Parse the input using strptime with the correct format
            inicio_clase = datetime.strptime(user_input_inicio, "%Y-%m-%d %H:%M")
            while True:

                print(art.modulo_mensaje7, end='')
                fin_clase = datetime.strptime(input(), "%Y-%m-%d %H:%M")

                if fin_clase <= inicio_clase:
                    art.data_processing_animation(art.modulo_mensaje9)
                    raise ValueError
                else:
                    duracion = fin_clase - inicio_clase
                    if timedelta(hours=1) <= duracion <= timedelta(hours=8):

                        inicio_clase, fin_clase = str(inicio_clase), str(fin_clase)
                        return (inicio_clase, fin_clase)
                    else:
                        art.data_processing_animation(art.modulo_mensaje10)
                        raise ValueError


        except ValueError:
            # Catch any format errors and ask again
            art.data_processing_animation(art.modulo_mensaje8)


def cargar_modulo(codigo, nombre, duracion, horario):

    with open('./app_data/data.json') as file:
        data = json.load(file)
    
    data["modulos"][codigo] = {"nombre": nombre, "duracion": duracion, "horario": {"inicio": horario[0], "fin": horario[1]}}

    with open('./app_data/data.json', 'w+') as file:
        json.dump(data, file, indent=4)

def cargar_alumno(codigo, nombre, sexo, edad):

    with open('./app_data/data.json') as file:
        data = json.load(file)

    data["alumnos"][codigo] = {"nombre": nombre, "edad": edad, "sexo": sexo}

    with open('./app_data/data.json', 'w+') as file:
        json.dump(data, file, indent=4)

    