"""Módulo 'art'.

Este módulo almacena variables y funciones que mejoran la estética del programa.
"""

import sys
import tty
import termios

def limpiar_pantalla():
    """Función para limpiar la pantalla de la terminal.
    
    Usar el código de espace ANSI para limpiar la pantalla, este funciona así:
        '\033c' indica a la terminal que el texto a continuación debe ser 
        interpretado como un comando, en vez de texto normal.
        'c' es el comando que la terminal leerá, el cual borra la pantalla.
    """
    print('\033c')
    return 0

# Variables para personalizar la estética del texto en la terminal
bold = "\033[1m"
white = "\033[37m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
reset = "\033[0m"

#  Arte ASCII del acrónimo del nombre del programa.
SISGESA_base = """
++----------------------------------------------------------------------------------++
++----------------------------------------------------------------------------------++
||                                                                                  ||
||   █████████  █████  █████████    █████████  ██████████  █████████    █████████   ||
||  ███░░░░░███░░███  ███░░░░░███  ███░░░░░███░░███░░░░░█ ███░░░░░███  ███░░░░░███  ||
|| ░███    ░░░  ░███ ░███    ░░░  ███     ░░░  ░███  █ ░ ░███    ░░░  ░███    ░███  ||
|| ░░█████████  ░███ ░░█████████ ░███          ░██████   ░░█████████  ░███████████  ||
||  ░░░░░░░░███ ░███  ░░░░░░░░███░███    █████ ░███░░█    ░░░░░░░░███ ░███░░░░░███  ||
||  ███    ░███ ░███  ███    ░███░░███  ░░███  ░███ ░   █ ███    ░███ ░███    ░███  ||
|| ░░█████████  █████░░█████████  ░░█████████  ██████████░░█████████  █████   █████ ||
||  ░░░░░░░░░  ░░░░░  ░░░░░░░░░    ░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░  ░░░░░   ░░░░░  ||
||                                                                                  ||
++----------------------------------------------------------------------------------++
++----------------------------------------------------------------------------------++
"""

first_login_m1 = f'{bold}{white}Bienvenido a SISGESA! El software perfecto para administrar y supervisar la asistencia en su institución educativa!{reset}'
first_login_m2 = f'{bold}{white}Dado que es la primera vez que ingresa, debemos registrar el usuario que desea usar.\nIngrese a continuación el nombre de usuario\n>>> {reset}'
first_login_m3 =  f'{bold}{white}\nUsuario registrado exitosamente!\nSu contraseña es {blue}"SISGESA"{white}{bold}, recomendamos cambiarla para una mayor seguridad!{reset}'
mensaje_cont_salir = f'\nPRESIONE "C" para continuar o cualquier otra tecla para salir\n{bold}>>> '


def center_text(text, width):
    """Función para centrar cadenas de texto multilínea.

    Esta función recibe un texto y lo centra en un ancho especificado.

    Args:
        text (str): El texto que se centra, puede contener varias lineas.
        width (int): El ancho total en el que se desea centrar el texto. 

    Returns:
        str: El texto centrado, con cada línea ajustada al ancho especificado.
    """
    lines = text.splitlines() 
    centered_lines = [line.center(width) for line in lines] 
    return "\n".join(centered_lines) 


terminal_width = 160
SISGESA = center_text(SISGESA_base, terminal_width)

user_prompt = f'{bold}{white}Ingrese su usuario{reset}'.center(170)
prompt_symbol = f'{bold}{white}>>> {reset}'.rjust(85)
type_user_message = f'{user_prompt}\n\n{prompt_symbol}'
pass_prompt = f'{bold}{white}Ingrese su contraseña{reset}'.center(170)
type_password_message = f'{pass_prompt}\n\n{prompt_symbol}'

def getch():
    """Recibe carácteres del usuario sin mostrarlos en pantalla.
    
    Hablando de forma más técnica, esta función recibe un carácter a la vez
    del 'standard input'.

    Falta todavía entender la función!!!
    El logo ASCII del programa se distorsiona si cambio el nombre de la funcion!!!????
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def input_password():
    """Falta todavía entender la función!!!"""

    password = ""
    
    while True:
        char = getch()
        if char in ('\n', '\r'):
            print() 
            break
        elif char == '\x7f':
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)

    return password

adios = r"""

   █████████       █████  ███                   ███
  ███░░░░░███     ░░███  ░░░                   ░███
 ░███    ░███   ███████  ████   ██████   █████ ░███
 ░███████████  ███░░███ ░░███  ███░░███ ███░░  ░███
 ░███░░░░░███ ░███ ░███  ░███ ░███ ░███░░█████ ░███
 ░███    ░███ ░███ ░███  ░███ ░███ ░███ ░░░░███░░░ 
 █████   █████░░████████ █████░░██████  ██████  ███
░░░░░   ░░░░░  ░░░░░░░░ ░░░░░  ░░░░░░  ░░░░░░  ░░░ 

"""

def despedida():
    """Genera una pantalla de despedida cuando el usuario sale del programa."""
    limpiar_pantalla()
    print(adios)
