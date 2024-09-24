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
from datetime import datetime, timedelta
from packages import art

# Creación de variables que contienen las rutas de los archivos que se usarán.
principal = './app_data/data.json'
credenciales = './app_data/credenciales.json'
asistencia = './app_data/asistencia.json'
      
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
    with open(principal, "+a") as file:
        file.seek(0)
        json.dump(data, file, indent=4)

    asistencia_estructura_json = {}
    with open(asistencia, "+w") as file:
        json.dump(asistencia_estructura_json, file, indent=4)

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
    """Función para añadir un grupo al archivo JSON."""
    with open(principal) as file:
        data = json.load(file)

    data["grupos"][codigo] = {"nombre": nombre, "sigla": sigla}

    with open(principal, 'w+') as file:
        json.dump(data, file, indent=4)

def cargar_modulo(codigo, nombre, duracion, horario):
    """Función para añadir un módulo al archivo JSON.
    
    Args:
        codigo (str): Codigo del modulo que se desea agregar.
        nombre (str): Nombre del modulo que se desea agregar.
        duracion (str): Duracion del modulo en semanas.
        horario (tuple): Contiene primero el valor de inicio del modulo, y
        de segundo el valor de fin del modulo.
        Ambos en formato YYYY-MM-DD HH:MM:SS .
    """
    with open(principal) as file:
        data = json.load(file)
    
    data["modulos"][codigo] = {"nombre": nombre, "duracion": int(duracion), "horario": {"inicio": horario[0], "fin": horario[1]}}

    with open(principal, 'w+') as file:
        json.dump(data, file, indent=4)

def cargar_alumno(codigo, nombre, sexo, edad):
    """Función para añadir un alumno al archivo JSON."""

    with open(principal) as file:
        data = json.load(file)

    data["alumnos"][codigo] = {"nombre": nombre, "edad": int(edad), "sexo": sexo, "modulos": []}

    with open(principal, 'w+') as file:
        json.dump(data, file, indent=4)

def revisa_alumno_existe(codigo):
    """Chequea si un alumno existe."""

    with open(principal) as file:
        data = json.load(file)
    
    if data["alumnos"].get(codigo, False):
        return True
    return False
    
def asignar_grupo_alumno(codigo, grupo):

    with open(principal) as file:
        data = json.load(file)

    data["alumnos"][codigo]["grupo"] = grupo

    with open(principal, 'w+') as file:
        json.dump(data, file, indent=4)

def revisa_alumno_cuantos_modulos(codigo, person="alumnos"):
    """Revisa si el alumno esta asignado a mas de 3 modulos."""
    with open(principal) as file:
        data = json.load(file)

    return data[person][codigo].get("modulos")

def asignar_modulo(codigo, modulo):
    """Asigna módulo a un alumno"""

    with open(principal) as file:
        data = json.load(file)
        
        if len(data["alumnos"][codigo]["modulos"]) < 3:
            data["alumnos"][codigo]["modulos"].append(modulo)

            with open(principal, 'w+') as file:
                json.dump(data, file, indent=4)

            with open(asistencia) as file:
                data = json.load(file)

            for clase in data[modulo]:
                data[modulo][clase][codigo] = {}
            
            with open(asistencia, "+w") as file:
                json.dump(data, file, indent=4)
            return True
        else:
            return False

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

def docente_existe(cedula):
    """Retorna la lista de modulos del docente"""
    with open(principal) as file:
        data = json.load(file)
    
    if data["docentes"].get(cedula, False):
        return True
    return False

def cuales_modulos_docente(cedula):
    with open(principal) as file:
        data = json.load(file)
    
    return data["docentes"][cedula]

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

def generar_dias_modulo(inicio, fin):
    """Genera una lista que contiene los dias que se dictará el módulo
    
    Args:
        inicio (str): Fecha en formato YYYY-MM-DD HH:MM:SS que simboliza el dia
        y hora de inicio del módulo.
        fin (str): Fecha en formato YYYY-MM-DD HH:MM:SS que simboliza el dia y 
        hora de finalización del módulo.

    Returns:
        dias (list): Una lista que contiene los dias que se dictará el módulo,
        sin contar los días que sean fin de semana.
    """
    dias = []
    fecha_actual = inicio
    while fecha_actual <= fin:
        # Revisa si es un dia de la semana (Lunes=0, Domingo=6)
        if fecha_actual.weekday() < 5:  # Monday to Friday
            dias.append(fecha_actual.strftime("%Y-%m-%d"))
        # Se mueve al siguiente día
        fecha_actual += timedelta(days=1)
    return dias

def registrar_dias_modulo(modulo, dias):
    """Registra en la estructura JSON de asistencia los días de cada módulo
    
    Args:
        dias (list): Una lista que contiene los dias que se dictará cada módulo.
    """
    dias = {date: {} for date in dias}

    try:
        with open(asistencia, "a+") as file:
            file.seek(0)
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[modulo] = dias
    with open(asistencia, "w+") as file:
        json.dump(data, file, indent=4)

def registrar_hora_asistencia(codigo, modulo, contexto):
    """Registra automáticamente en el JSON la asistencia del estudiante.
    
    Usa la hora actual para registrar ya sea la hora de entrada del estudiante
    y/o la hora de salida.

    Args:
        codigo (str): Codigo del estudiante.
        modulo (str): Codigo del módulo.
        contexto (str): Determina si se registrará la llegada o la salida.
        Solo toma dos posibles valores: 'llegada' o 'salida'.
    """
    dia_actual = datetime.today().strftime('%Y-%m-%d')
    if contexto == 'llegada':
        with open(asistencia) as file:
            data = json.load(file)
        data[modulo][dia_actual][codigo]["llegada"] = datetime.today().strftime('%H:%M:%S')
        with open(asistencia, "w+") as file:
            json.dump(data, file, indent=4)
            return True
    if contexto == 'salida':
        with open(asistencia) as file:
            data = json.load(file)
            data[modulo][dia_actual][codigo]["salida"] = datetime.today().strftime('%H:%M:%S')
            with open(asistencia, "w+") as file:
                json.dump(data, file, indent=4)
                return True
            
def revisar_datos_asistencia(modulo, fecha, alumno):
    """Revisa si un estudiante ya registró su hora de llegada y/o de salida.
    
    Args:
        modulo (str): El código del módulo que se desea revisar.
        alumno (str): El código del alumno que se desea revisar.

    Returns:
        tuple: La tupla contiene las cadenas "salida" y/o "llegada"
        simbolizando los datos de asistencia que faltan del alumno.
        Si la tupla está vacia significa que no hacen falta datos.
        bool: Regresa False si no hacen falta datos para registrar
        la asistencia del estudiante.
    """
    with open(asistencia) as file:
        data = json.load(file)

    match len(data[modulo][fecha][alumno].keys()):
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return False
        
def consultar_alumnos_en_grupo(grupo):
    """Consulta qué alumnos están en un grupo.
    
    Args:
        grupo (str): El código del grupo.
    
    Returns:
        alumnos (lista): Una lista que contiene los codigos de todos
        los estudiantes que pertenecen al grupo ingresado.
    """
    alumnos = []
    with open(principal) as file:
        data = json.load(file)
    for codigo in data["alumnos"].keys():
        if data["alumnos"][codigo].get("grupo") == grupo:
            alumnos.append(codigo)
    return alumnos

def consultar_alumnos_en_modulo(modulo):
    """Consulta los alumnos registrados en un modulo elegido.
    
    Args:
        modulo (str): El codigo del modulo que se desea consultar.

    Returns:
        alumnos (list): La lista con los codigos de los alumnos
        registrados en el módulo elegido.
    """
    alumnos = []
    with open(principal) as file:
        data = json.load(file)
    for codigo in data["alumnos"].keys():
        modulos_alumno = data["alumnos"][codigo].get("modulos")
        if modulo in modulos_alumno:
            alumnos.append(codigo)
    return alumnos

def consultar_docentes_imparten_modulo(modulo):
    """Consulta los docentes que imparten un modulo elegido.
    
    Args:
        modulo (str): El codigo del modulo que se desea consultar.

    Returns:
        alumnos (list): La lista con los codigos de los docentes
        registrados en el módulo elegido.
    """
    docentes = []
    with open(principal) as file:
        data = json.load(file)
    for codigo in data["docentes"].keys():
        modulos_alumno = data["docentes"][codigo].get("modulos")
        if modulo in modulos_alumno:
            docentes.append(codigo)
    return docentes

def consultar_estudiantes_a_cargo_docente_en_modulo(cedula, modulo):
    """Consulta los estudiantes de los que está a cargo un docente
    en un módulo ingresado.
    
    Args:
        cedula (str): La cédula del docente.
        modulo (str): El código del módulo.

    Returns:
        alumnos (list): Una lista que contiene los alumnos que están
        asignados en el módulo ingresado y reciben clases del docente ingresado.
    """
    alumnos = []
    with open(principal) as file:
        info = json.load(file)
    if modulo in info["docentes"][cedula]["modulos"]:
        print(f"El docente {info['docentes'][cedula]['nombre']} imparte el modulo {modulo}.")
        print(f"Los estudiantes que tiene a cargo son:")
        alumnos = consultar_alumnos_en_modulo(modulo)
        print(', '.join(alumnos))
        print("\n\nPresione cualquier tecla para volver")
        input()
    else:
        print(f"El docente {info['docentes'][cedula]['nombre']} no imparte el modulo {modulo}")
    