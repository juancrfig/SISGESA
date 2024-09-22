"""Módulo 'menus'.

Este módulo contiene todas las funcionalidades relacionadas con la  
visualización de menús y submenús en la aplicación. Proporciona funcionalidades
para manejar el inicio de sesión y otras interacciones con el usuario.

El módulo importa el módulo 'art' para añadir efectos estéticos a las funciones.
"""
from packages import art, data

def first_login():

    art.limpiar_pantalla()
    print(art.first_login_m1)
    print(art.SISGESA)
    print(art.first_login_m2, end='')
    user = input()

    info = {
        'user': user,
        'password': 'SISGESA'
    }

    info['password'] = data.data_encryption(info['password'])
    data.register_new_user(info)

    print(art.first_login_m3)
    respuesta = input(art.mensaje_cont_salir)
    
    if respuesta.lower() == 'c':
        return 0
    else:
        return 9

def login():
    """Función para manejar el inicio de sesión del usuario.

    Limpia la pantalla y solicita al usuario que ingrese su nombre de usuario
    y contraseña. 

    Raises:
        ValueError: Si el nombre de usuario o la contraseña son inválidos.
    """
    art.limpiar_pantalla()
    print(art.SISGESA, '\n')
    user = input(art.type_user_message)
    print()
    print(art.type_password_message, end='')
    password = art.input_password()

    if data.check_correct_login(user, password) == 0:
        return 0
    else:
        return 401
    
def main():
    art.limpiar_pantalla()
    art.main_menu()
    answer = int(input())
    return answer

def registro_grupos():

    art.limpiar_pantalla()
    print(art.registro_grupos_ascii)
    print(art.grupos_mensaje1, art.grupos_mensaje2)
    print(art.grupos_mensaje3, end='')
    codigo = input()

    if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
        raise ValueError
    
    print(art.grupos_mensaje4, end='')
    nombre = input().strip().replace(' ', '_').upper()

    if not (not nombre.isdigit() and 4 <= len(nombre) <= 20):
        raise ValueError
    
    print(art.grupos_mensaje5, end='')
    sigla = input().strip().upper()

    if not (sigla.isalpha() and 3 <= len(sigla) <= 6):
        raise ValueError
    
    data.cargar_grupo(codigo, nombre, sigla)
    art.data_processing_animation(art.cargando_mensaje)
    return 0

def registro_modulos():
    art.limpiar_pantalla()
    print(art.nuevo_modulo_ascii)
    print(art.modulo_mensaje1, art.modulo_mensaje2)
    print(art.modulo_mensaje3, end='')
    codigo = input()

    if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
        raise ValueError

    print(art.modulo_mensaje4, end='')
    nombre = input().strip().replace(' ', '_').upper()

    if not (not nombre.isnumeric()  and 3 <= len(nombre) <= 55):
        raise ValueError
    
    print(art.modulo_mensaje5, end='')
    duracion = input()

    if not (duracion.isnumeric() and 1 <= int(duracion) <= 99):
        raise ValueError

    horario = data.pedir_horario(duracion)

    
    data.cargar_modulo(codigo, nombre, duracion, horario)
    art.data_processing_animation(art.cargando_mensaje)
    return 0

def registro_estudiantes():
    art.limpiar_pantalla()
    print(art.nuevo_alumno_ascii)
    print(art.alumno_mensaje1, art.alumno_mensaje2)
    print(art.alumno_mensaje3, end='')

    codigo = input()
    if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
        raise ValueError
    
    print(art.alumno_mensaje4, end='')
    nombre = input().strip().replace(' ', '_').upper()

    if not (not nombre.isnumeric()  and 4 <= len(nombre) <= 55):
        raise ValueError
    
    print(art.alumno_mensaje5, end='')
    sexo = input().strip().upper()

    if sexo not in ('M', 'F'):
        raise ValueError
    
    print(art.alumno_mensaje6, end='')
    edad = input()

    if not (edad.isdigit() and 8 <= int(edad) <= 99):
        raise ValueError
    
    data.cargar_alumno(codigo, nombre, sexo, edad)
    art.data_processing_animation(art.cargando_mensaje)
    return 0

def registro_docentes():
    art.limpiar_pantalla()
    print(art.nuevo_docente_ascii)
    input("Llegaste al registro de docentes!")

def registro_asistencia():
    art.limpiar_pantalla()
    print(art.asistencia_ascii)
    input("Llegaste al registro de asistencia!")

def consultar_info():
    art.limpiar_pantalla()
    print(art.consultas_ascii)
    input("Llegaste a la consulta de información!")

def generar_informe():
    art.limpiar_pantalla()
    print(art.generar_informe_ascii)
    input("Llegaste a la generación de informes!")

def cambio_contra():

    art.limpiar_pantalla()
    print(art.cambio_contra_ascii)
    print(art.cambio_clave_m1, end='')
    user = input()
    print(art.cambio_clave_m2, end='')
    password = art.input_password()

    if data.check_correct_login(user, password) == 0:
        print(art.validacion_exito_mensaje)
        print(art.cambio_clave_m3, end='')
        password = art.input_password()
        data.change_password(user, password)
        print(art.cambio_clave_m4)
        art.data_processing_animation('')
        return 0

    else:
        print(art.seguridad_mensaje)
        art.data_processing_animation(art.user_invalid_input_message)
        return 401