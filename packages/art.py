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

# Variables para personalizar la estética del texto en la terminal
bold = "\033[1m"
white = "\033[37m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
reset = "\033[0m"

user_prompt = f'{bold}{white}Ingrese su usuario{reset}'.center(170)
prompt_symbol = f'{bold}{white}>>> {reset}'.rjust(85)
type_user_message = f'{user_prompt}\n\n{prompt_symbol}'
pass_prompt = f'{bold}{white}Ingrese su contraseña{reset}'.center(170)
type_password_message = f'{pass_prompt}\n\n{prompt_symbol}'

def getch():
    """Get a single character from standard input without echoing."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def input_password():

    password = ""
    
    while True:
        char = getch()
        if char in ('\n', '\r'):  # Enter key
            print()  # Newline
            break
        elif char == '\x7f':  # Backspace key
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)  # Remove last asterisk
        else:
            password += char
            print('*', end='', flush=True)  # Display an asterisk for each character

    return password