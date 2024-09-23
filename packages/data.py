import json
import hashlib
from datetime import datetime, timedelta, time
from packages import art

data_json = './app_data/data.json'
pass_json = './app_data/password.json'

def crear_estructura_json():
    data = {
        "grupos": {},
        "modulos": {},
        "alumnos": {},
        "docentes": {},
    }
    with open(data_json, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def check_first_time():
    with open(pass_json, 'a+') as pass_file:
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
    with open(pass_json, 'w+' ) as file:
        json.dump(info, file)

def check_correct_login(user, password):

    with open(pass_json) as file:
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

    with open(pass_json, 'w+') as file:
        json.dump(info, file)

def cargar_grupo(codigo, nombre, sigla):

    with open(data_json) as file:
        data = json.load(file)

    data["grupos"][codigo] = {"nombre": nombre, "sigla": sigla}

    with open(data_json, 'w+') as file:
        json.dump(data, file, indent=4)

def pedir_horario(weeks):

    while True:

        print(art.modulo_mensaje6, end='')
        user_input_inicio = input()

        try:
            # Parse the input using strptime with the correct format
            inicio_clase = datetime.strptime(user_input_inicio, "%Y-%m-%d %H:%M")
            inicio_hora = inicio_clase.time()
            
            if not (time(5, 0) <= inicio_hora <= time(18, 0)): 
                art.data_processing_animation(art.modulo_mensaje11)
                raise ValueError           
            while True:

                print(art.modulo_mensaje7, end='')

                fin_hora = datetime.strptime(input(), "%H:%M").time()
                if not (time(6, 0) <= fin_hora <= time(23, 0)):
                    art.data_processing_animation(art.modulo_mensaje12)
                    raise ValueError

                fin_fecha = inicio_clase + timedelta(weeks=int(weeks))

                fin_clase = datetime.combine(fin_fecha.date(), fin_hora)

                if fin_clase <= inicio_clase:
                    art.data_processing_animation(art.modulo_mensaje9)
                    raise ValueError
                else:

                    hoy = datetime.today()
                    tmp_inicial = datetime.combine(hoy, inicio_hora)
                    tmp_final = datetime.combine(hoy, fin_hora)
                    duracion = tmp_final - tmp_inicial

                    if timedelta(hours=1) <= duracion <= timedelta(hours=8):

                        inicio_clase, fin_clase = str(inicio_clase), str(fin_clase)
                        return (inicio_clase, fin_clase)
                    else:
                        art.data_processing_animation(art.modulo_mensaje10)
                        raise ValueError


        except ValueError:
            # Catch any format errors and ask again
            art.data_processing_animation(art.volviendo_mensaje_mal_input)


def cargar_modulo(codigo, nombre, duracion, horario):

    with open(data_json) as file:
        data = json.load(file)
    
    data["modulos"][codigo] = {"nombre": nombre, "duracion": int(duracion), "horario": {"inicio": horario[0], "fin": horario[1]}}

    with open(data_json, 'w+') as file:
        json.dump(data, file, indent=4)

def cargar_alumno(codigo, nombre, sexo, edad):

    with open(data_json) as file:
        data = json.load(file)

    data["alumnos"][codigo] = {"nombre": nombre, "edad": int(edad), "sexo": sexo, "modulos": []}

    with open(data_json, 'w+') as file:
        json.dump(data, file, indent=4)

def check_alumno_exists(codigo):

    with open(data_json) as file:
        data = json.load(file)
    
    if data["alumnos"].get(codigo):
        return True
    
def asignar_grupo_alumno(codigo, grupo):

    with open(data_json) as file:
        data = json.load(file)

    data["alumnos"][codigo]["grupo"] = grupo

    with open(data_json, 'w+') as file:
        json.dump(data, file, indent=4)

def check_student_modules(codigo):

    with open(data_json) as file:
        data = json.load(file)

    return data["alumnos"][codigo].get("modulos")

def asignar_modulo(codigo, modulo):

    with open(data_json) as file:
        data = json.load(file)
        
        if len(data["alumnos"][codigo]["modulos"]) < 3:
            data["alumnos"][codigo]["modulos"].append(modulo)

            with open(data_json, 'w+') as file:
                json.dump(data, file, indent=4)

            return True

        else:
            return False

def cuales_modulos(codigo):

    with open(data_json) as file:
        data = json.load(file)

    return art.asignacion_mensaje9 + data["alumnos"][codigo]["modulos"]

def eliminar_modulo(codigo, modulo):
    
    with open(data_json) as file:
        data = json.load(file)

    data["alumnos"][codigo]["modulos"].remove(modulo)

    with open(data_json, "w+") as file:
        json.dump(data, file, indent=4)

    return 0  
    
def cargar_docente(cedula, nombre):

    with open(data_json) as file:
        data = json.load(file)

    data["docentes"][f'{cedula}'] = {"nombre": nombre, "modulos": []}

    with open(data_json, 'w+') as file:
        json.dump(data, file, indent=4)

def cuales_modulos_docente(cedula):

    with open(data_json) as file:
        data = json.load(file)

    return data["docentes"][cedula]["modulos"]

def asignar_modulo_docente(cedula, modulo):

    with open(data_json) as file:
        data = json.load(file)

    data["docentes"][cedula]["modulos"].append(modulo)

    with open(data_json, "w+") as file:
        json.dump(data, file, indent=4)

def borrar_modulo_docente(cedula, modulo):

    with open(data_json) as file:
        data = json.load(file)

    data["docentes"][cedula]["modulos"].remove(modulo)

    with open(data_json, "w+") as file:
        json.dump(data, file, indent=4)
    