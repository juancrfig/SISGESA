"""Módulo "data".

Este módulo proporciona funciones para manipular y leer la información generada 
por el programa. También incluye utilidades para manejar archivos JSON, calcular
hashes y gestionar operaciones relacionadas con el tiempo.

Imports:
    json: Módulo para trabajar con archivos JSON.
    hashlib: Módulo para generar hashes (MD5, SHA, etc.).
    datetime, timedelta, time: Módulos para trabajar con fechas y tiempos.
    art: Módulo personalizado para añadir efectivos estéticos al programa.
"""
import json
import hashlib
from datetime import datetime, timedelta, time
from packages import art

# Creación de variables que contienen las rutas de los archivos que se usarán.
principal = './app_data/data.json'
clave = './app_data/password.json'
      
def primera_vez():
    """Comprueba si es la primera vez que se ejecuta el programa.

    Intenta abrir el archivo "clave" para determinar si el programa ha sido ejecutado antes. 
    Si el archivo contiene datos, se asume que no es la primera vez que se ejecuta. 
    Si el archivo está vacío o no existe, se asume que es la primera ejecución.
    En el caso que el archivo no exista, lo crea automaticamente.

    Args:
        clave (str): La ruta del archivo que contiene la clave o información.

    Returns:
        bool: True si es la primera vez que se ejecuta el programa, False en caso contrario.
    """
    with open(clave, 'a+') as pass_file:
        pass_file.seek(0)
        return not bool(pass_file.readlines())

def crear_estructura_json():
    """Crea una estructura JSON básica y la guarda en un archivo."""
    data = {
        "grupos": {},
        "modulos": {},
        "alumnos": {},
        "docentes": {},
    }
    with open(principal, 'w') as file:
        json.dump(data, file, indent=4)

def encriptador(texto):
    """Genera el hash SHA-256 de un texto.

    Esta función toma una cadena de texto, la codifica en UTF-8, y devuelve 
    su representación en hexadecimal del hash SHA-256.

    Args:
        text (str): El texto que se va a cifrar.

    Returns:
        str: La representación hexadecimal del hash SHA-256.
    """
    data = texto.encode('utf-8')
    hash_objeto = hashlib.sha256(data)
    return hash_objeto.hexdigest()

def nuevo_usuario(usuario, clave_inicial="SISGESA", archivo='credenciales.json'):
    """Crea un nuevo usuario y guarda sus credenciales en un archivo JSON.

    Esta función toma el nombre de usuario y una clave inicial, y 
    guarda esta información en un archivo JSON después de encriptar la clave.

    Args:
        usuario (str): El nombre del nuevo usuario.
        clave_inicial (str, optional): La clave inicial del usuario, 
            por defecto es "SISGESA".
        clave (str, optional): El nombre del archivo donde se guardarán 
            las credenciales, por defecto es 'credenciales.json'.
    """
    usuario_y_clave = {
        "usuario": usuario,
        "clave": encriptador(clave_inicial)
    }
    with open(archivo, 'w+' ) as file:
        json.dump(usuario_y_clave, file)

def check_correct_login(user, password):

    with open(clave) as file:
        data = json.load(file)
    
    
    if user == data['user'] and encriptador(password) == data['password']:
        return 0
    else:
        return 401

def change_password(user, password):
    
    info = {
        'user': user,
        'password': encriptador(password)
    }

    with open(clave, 'w+') as file:
        json.dump(info, file)

def cargar_grupo(codigo, nombre, sigla):

    with open(principal) as file:
        data = json.load(file)

    data["grupos"][codigo] = {"nombre": nombre, "sigla": sigla}

    with open(principal, 'w+') as file:
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

    with open(principal) as file:
        data = json.load(file)
    
    data["modulos"][codigo] = {"nombre": nombre, "duracion": int(duracion), "horario": {"inicio": horario[0], "fin": horario[1]}}

    with open(principal, 'w+') as file:
        json.dump(data, file, indent=4)

def cargar_alumno(codigo, nombre, sexo, edad):

    with open(principal) as file:
        data = json.load(file)

    data["alumnos"][codigo] = {"nombre": nombre, "edad": int(edad), "sexo": sexo, "modulos": []}

    with open(principal, 'w+') as file:
        json.dump(data, file, indent=4)

def check_alumno_exists(codigo):

    with open(principal) as file:
        data = json.load(file)
    
    if data["alumnos"].get(codigo):
        return True
    
def asignar_grupo_alumno(codigo, grupo):

    with open(principal) as file:
        data = json.load(file)

    data["alumnos"][codigo]["grupo"] = grupo

    with open(principal, 'w+') as file:
        json.dump(data, file, indent=4)

def check_student_modules(codigo):

    with open(principal) as file:
        data = json.load(file)

    return data["alumnos"][codigo].get("modulos")

def asignar_modulo(codigo, modulo):

    with open(principal) as file:
        data = json.load(file)
        
        if len(data["alumnos"][codigo]["modulos"]) < 3:
            data["alumnos"][codigo]["modulos"].append(modulo)

            with open(principal, 'w+') as file:
                json.dump(data, file, indent=4)

            return True

        else:
            return False

def cuales_modulos(codigo):

    with open(principal) as file:
        data = json.load(file)

    return art.asignacion_mensaje9 + data["alumnos"][codigo]["modulos"]

def eliminar_modulo(codigo, modulo):
    
    with open(principal) as file:
        data = json.load(file)

    data["alumnos"][codigo]["modulos"].remove(modulo)

    with open(principal, "w+") as file:
        json.dump(data, file, indent=4)

    return 0  
    
def cargar_docente(cedula, nombre):

    with open(principal) as file:
        data = json.load(file)

    data["docentes"][f'{cedula}'] = {"nombre": nombre, "modulos": []}

    with open(principal, 'w+') as file:
        json.dump(data, file, indent=4)

def cuales_modulos_docente(cedula):

    with open(principal) as file:
        data = json.load(file)

    return data["docentes"][cedula]["modulos"]

def asignar_modulo_docente(cedula, modulo):

    with open(principal) as file:
        data = json.load(file)

    data["docentes"][cedula]["modulos"].append(modulo)

    with open(principal, "w+") as file:
        json.dump(data, file, indent=4)

def borrar_modulo_docente(cedula, modulo):

    with open(principal) as file:
        data = json.load(file)

    data["docentes"][cedula]["modulos"].remove(modulo)

    with open(principal, "w+") as file:
        json.dump(data, file, indent=4)
    