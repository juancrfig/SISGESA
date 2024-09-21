"""Módulo 'menus'.

Este módulo contiene todas las funcionalidades relacionadas con la  
visualización de menús y submenús en la aplicación. Proporciona funcionalidades
para manejar el inicio de sesión y otras interacciones con el usuario.

El módulo importa el módulo 'art' para añadir efectos estéticos a las funciones.
"""
from packages import art

def first_login():

    art.limpiar_pantalla()
    print(art.first_login_m1)
    print(art.SISGESA)
    print(art.first_login_m2, end='')
    user = input()
    print(art.first_login_m3)
    respuesta = input(art.mensaje_cont_salir)
    
    if respuesta.lower() == 'c':
        return 0
    else:
        return 1


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