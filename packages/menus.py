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
        'user': f'{user}',
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
    input("Llegaste al registro de grupos!")

def registro_modulos():
    art.limpiar_pantalla()
    input("Llegaste al registro de modulos!")


def registro_estudiantes():
    art.limpiar_pantalla()
    input("Llegaste al registro de estudiantes!")

def registro_docentes():
    art.limpiar_pantalla()
    input("Llegaste al registro de docentes!")

def registro_asistencia():
    art.limpiar_pantalla()
    input("Llegaste al registro de asistencia!")

def consultar_info():
    art.limpiar_pantalla()
    input("Llegaste a la consulta de información!")

def generar_informe():
    art.limpiar_pantalla()
    input("Llegaste a la generación de informes!")

def cambio_contra():
    art.limpiar_pantalla()
    input("Llegaste al cambio de contraseña!")

