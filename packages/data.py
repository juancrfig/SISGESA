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
from packages import art

# Creación de variables que contienen las rutas de los archivos que se usarán.
principal = './app_data/data.json'
credenciales = './app_data/credenciales.json'
      
def primera_vez(archivo=credenciales):
    """Comprueba si es la primera vez que se ejecuta el programa.

    Intenta abrir el archivo "clave" para determinar si el programa ha sido ejecutado antes. 
    Si el archivo contiene datos, se asume que no es la primera vez que se ejecuta. 
    Si el archivo está vacío o no existe, se asume que es la primera ejecución.
    En el caso que el archivo no exista, lo crea automaticamente.

    Args:
        archivo (str): La ruta del archivo que contiene la clave o información.

    Returns:
        bool: True si es la primera vez que se ejecuta el programa, False en caso contrario.
    """
    with open(archivo, 'a+') as file:
        file.seek(0)
        return not bool(file.readlines())

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

def nuevo_usuario(usuario, clave_inicial="SISGESA", archivo_final=credenciales):
    """Crea un nuevo usuario y guarda sus credenciales en un archivo JSON.

    Esta función toma el nombre de usuario y una clave inicial, y 
    guarda esta información en un archivo JSON después de encriptar la clave.

    Args:
        usuario (str): El nombre del nuevo usuario.
        clave_inicial (str, optional): La clave inicial del usuario, 
            por defecto es "SISGESA".
        archivo_final (str, optional): El nombre del archivo donde se guardarán 
            las credenciales, por defecto es 'credenciales.json'.
    
    Returns:
        str : La clave inicial del usuario
    """
    usuario_y_clave = {
        "usuario": usuario,
        "clave": encriptador(clave_inicial)
    }
    with open(archivo_final, 'w+' ) as file:
        json.dump(usuario_y_clave, file)
    
    return clave_inicial

def validacion_usuario_clave(usuario, clave):
    """Revisa si el usuario y la contraseña ingresada coinciden con la base de datos.

    Esta función abre el archivo json en el que se guardan las credenciales del usuario, de
    esta manera compara la información ingresada por el usuario para autorizar el ingreso o no.

    Args:
        usuario (str): El nombre de usuario ingresado al intentar iniciar sesión.
        clave (str): La representación hexadecimal del hash SHA-256 de la clave ingresada

    Returns:
        bool : True si la validación es exitosa, False si no. 
    """
    with open(credenciales) as file:
        data = json.load(file)  
    if usuario == data['usuario'] and encriptador(clave) == data['clave']:
        return True
    return False

def cambiar_clave(usuario, clave):
    """Cambia la clave del usuario en la base de datos. 
    
    La nueva clave es encriptada.
    
    Args:
        usuario (str): El nombre de usuario que fue ingresado en el
        menú de cambio de clave.
        clave (str): La nueva clave que desea el usuario.
    """
    
    info = {
        'usuario': usuario,
        'clave': encriptador(clave)
    }

    with open(credenciales, 'w+') as file:
        json.dump(info, file)

def revisar_codigo_existe(codigo, llave):
    """Revisa si un código, o cédula para el caso de los docentes, ya existe 
    en el archivo JSON.
    
    Args:
        codigo (str): Código ingresado por el usuario.
        llave (str): Llave en la que se desea buscar dentro del archivo JSON.

    Returns:
        bool : True si el código ya existe, de lo contrario False.
    """
    with open(principal) as file:
        data = json.load(file)
    if data[llave].get(codigo, False):
        return True
    return False

def cargar_grupo(codigo, nombre, sigla):
    """Función para añadir un grupo al archivo JSON"""
    with open(principal) as file:
        data = json.load(file)

    data["grupos"][codigo] = {"nombre": nombre, "sigla": sigla}

    with open(principal, 'w+') as file:
        json.dump(data, file, indent=4)

def cargar_modulo(codigo, nombre, duracion, horario):
    """Función para añadir un módulo al archivo JSON"""
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
    