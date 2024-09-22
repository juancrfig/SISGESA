"""Módulo 'art'.

Este módulo almacena variables y funciones que mejoran la estética del programa.
"""
from colorama import Fore, Back, Style, init
import sys
import tty
import termios
import time

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

user_pass_incorrect_message = f'Ha ingresado un usuario y/o contraseña incorrectos!'
user_invalid_input_message = f'Ha ingresado un dato invalido!'

def data_processing_animation(message, duration=3):
    print(f"{white}{bold}{message}")
    loading_symbols = ['/', '|', '\\', '-']  # Reverse spinner
    start_time = time.time()
    
    while time.time() - start_time < duration:
        for symbol in loading_symbols:
            sys.stdout.write(f"\r{symbol}")
            sys.stdout.flush()
            time.sleep(0.2)


def main_menu():
    print(Fore.CYAN + Style.BRIGHT + "╔═════════════════════════════════╗")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.WHITE + "  MENÚ PRINCIPAL               " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "╠═════════════════════════════════╣")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 1. Registro de grupos         " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 2. Registro de módulos        " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 3. Registro de estudiantes    " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 4. Registro de docentes       " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 5. Registro de asistencia     " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 6. Consultas de información   " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 7. Generación de informes     " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 8. Cambio de clave            " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.RED + " 9. Salida del sistema         " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "╚═════════════════════════════════╝")
    print()
    print("Ingrese el número de la opción deseada")
    print(">>> ", end='')

cambio_contra_ascii = """

   █████████                            █████      ███                  █████               █████████  ████                                
  ███░░░░░███                          ░░███      ░░░                  ░░███               ███░░░░░███░░███                                
 ███     ░░░   ██████   █████████████   ░███████  ████   ██████      ███████   ██████     ███     ░░░  ░███   ██████   █████ █████  ██████ 
░███          ░░░░░███ ░░███░░███░░███  ░███░░███░░███  ███░░███    ███░░███  ███░░███   ░███          ░███  ░░░░░███ ░░███ ░░███  ███░░███
░███           ███████  ░███ ░███ ░███  ░███ ░███ ░███ ░███ ░███   ░███ ░███ ░███████    ░███          ░███   ███████  ░███  ░███ ░███████ 
░░███     ███ ███░░███  ░███ ░███ ░███  ░███ ░███ ░███ ░███ ░███   ░███ ░███ ░███░░░     ░░███     ███ ░███  ███░░███  ░░███ ███  ░███░░░  
 ░░█████████ ░░████████ █████░███ █████ ████████  █████░░██████    ░░████████░░██████     ░░█████████  █████░░████████  ░░█████   ░░██████ 
  ░░░░░░░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░░░░  ░░░░░  ░░░░░░      ░░░░░░░░  ░░░░░░       ░░░░░░░░░  ░░░░░  ░░░░░░░░    ░░░░░     ░░░░░░ 
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""

cambio_clave_m1 = f'{bold}{white}Ingrese su usuario\n>>>{reset} '
cambio_clave_m2 = f'{bold}{white}Ingrese la clave actual\n>>>{reset} '
cambio_clave_m3 = f'{bold}{white}Ingrese la nueva clave\n>>>{reset} '
cambio_clave_m4 = f'{bold}{white}Se ha cambiado la clave exitosamente!\nVolviendo al menú!{reset}'
grupos_mensaje1 = f'{bold}{white}Para registrar un grupo debe ingresar los siguientes datos:'
grupos_mensaje2 = '\n> Codigo numerico\n> Nombre\n> Sigla'

validacion_exito_mensaje = f'{white}{bold}Validación exitosa!{reset}'
seguridad_mensaje = f'{white}{bold}Por razones de seguridad, volverá al menú anterior...{reset}'



