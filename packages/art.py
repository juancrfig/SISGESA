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
    print(Fore.CYAN + Style.BRIGHT + "╔═══════════════════════════════╗")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.WHITE + "  MENU PRINCIPAL               " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "╠═══════════════════════════════╣")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 1. Registro de grupos         " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 2. Registro de modulos        " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 3. Registro de estudiantes    " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 4. Registro de docentes       " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 5. Registro de asistencia     " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 6. Consultas de informacion   " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 7. Generacion de informes     " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.GREEN + " 8. Cambio de clave            " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.RED + " 9. Salida del sistema         " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "╚═══════════════════════════════╝")
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

registro_grupos_ascii = """

 ██████   █████                                               █████████                                         
░░██████ ░░███                                               ███░░░░░███                                        
 ░███░███ ░███  █████ ████  ██████  █████ █████  ██████     ███     ░░░  ████████  █████ ████ ████████   ██████ 
 ░███░░███░███ ░░███ ░███  ███░░███░░███ ░░███  ███░░███   ░███         ░░███░░███░░███ ░███ ░░███░░███ ███░░███
 ░███ ░░██████  ░███ ░███ ░███████  ░███  ░███ ░███ ░███   ░███    █████ ░███ ░░░  ░███ ░███  ░███ ░███░███ ░███
 ░███  ░░█████  ░███ ░███ ░███░░░   ░░███ ███  ░███ ░███   ░░███  ░░███  ░███      ░███ ░███  ░███ ░███░███ ░███
 █████  ░░█████ ░░████████░░██████   ░░█████   ░░██████     ░░█████████  █████     ░░████████ ░███████ ░░██████ 
░░░░░    ░░░░░   ░░░░░░░░  ░░░░░░     ░░░░░     ░░░░░░       ░░░░░░░░░  ░░░░░       ░░░░░░░░  ░███░░░   ░░░░░░  
                                                                                              ░███              
                                                                                              █████             
                                                                                             ░░░░░ 
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""

grupos_mensaje1 = f'{bold}{white}Para registrar un grupo debe ingresar los siguientes datos:{reset}'
grupos_mensaje2 = f'\n{white}{bold}> Codigo numerico\n> Nombre\n> Sigla\n{reset}'
grupos_mensaje3 = f'{white}{bold}Ingrese el codigo numerico ({yellow}Debe tener entre 4 y 9 digitos{white})\n>>>{reset} '
grupos_mensaje4 = f'{white}{bold}Ingrese el nombre del grupo ({yellow}Debe tener entre 4 y 9 letras{white})\n>>>{reset} '
grupos_mensaje5 = f'{white}{bold}Ingrese la sigla del grupo ({yellow}Debe tener entre 3 y 6 letras{white})\n>>>{reset} '

cargando_mensaje = f'{white}{bold}Cargando la informacion...Un momento...{reset}'
validacion_exito_mensaje = f'{white}{bold}Validación exitosa!{reset}'
seguridad_mensaje = f'{white}{bold}Por razones de seguridad, volverá al menú anterior...{reset}'


error_archivo_m1 = f'''\033c{white}{bold}Alguien a averiado el archivo en el que se guardaba la informacion!\n
No te preocupes, hemos creado un nuevo archivo para que vuelvas a intentarlo!\n
({yellow}Tenias un respaldo de la informacion, cierto? D:{white}){reset}'''

nuevo_modulo_ascii = """
 ██████   █████                                             ██████   ██████              █████            ████          
░░██████ ░░███                                             ░░██████ ██████              ░░███            ░░███          
 ░███░███ ░███  █████ ████  ██████  █████ █████  ██████     ░███░█████░███   ██████   ███████  █████ ████ ░███   ██████ 
 ░███░░███░███ ░░███ ░███  ███░░███░░███ ░░███  ███░░███    ░███░░███ ░███  ███░░███ ███░░███ ░░███ ░███  ░███  ███░░███
 ░███ ░░██████  ░███ ░███ ░███████  ░███  ░███ ░███ ░███    ░███ ░░░  ░███ ░███ ░███░███ ░███  ░███ ░███  ░███ ░███ ░███
 ░███  ░░█████  ░███ ░███ ░███░░░   ░░███ ███  ░███ ░███    ░███      ░███ ░███ ░███░███ ░███  ░███ ░███  ░███ ░███ ░███
 █████  ░░█████ ░░████████░░██████   ░░█████   ░░██████     █████     █████░░██████ ░░████████ ░░████████ █████░░██████ 
░░░░░    ░░░░░   ░░░░░░░░  ░░░░░░     ░░░░░     ░░░░░░     ░░░░░     ░░░░░  ░░░░░░   ░░░░░░░░   ░░░░░░░░ ░░░░░  ░░░░░░  
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""

modulo_mensaje1 = f'{bold}{white}Para registrar un grupo debe ingresar los siguientes datos:{reset}'
modulo_mensaje2 = f'\n{white}{bold}> Codigo numerico\n> Nombre\n> Duracion en semanas\n> Horario{reset}'
modulo_mensaje3 = f'{white}{bold}Ingrese el codigo numerico ({yellow}Debe tener entre 4 y 9 digitos{white})\n>>>{reset} '
modulo_mensaje4 = f'{white}{bold}Ingrese el nombre del modulo ({yellow}Debe tener entre 4 y 55 letras{white})\n>>>{reset} '
modulo_mensaje5 = f'{white}{bold}Ingrese la duracion del modulo en semanas ({yellow}Debe tener entre 1 y 2 digitos{white})\n>>>{reset} '
modulo_mensaje6 = f'{white}{bold}Ingrese el horario de inicio ({yellow}"YYYY-MM-DD HH:MM" formato 24 horas"{white})\n>>>{reset} '
modulo_mensaje7 = f'{white}{bold}Ingrese el horario de fin de la clase ({yellow}"YYYY-MM-DD HH:MM" formato 24 horas"{white})\n>>>{reset} '
modulo_mensaje8 = f'{white}{bold}Formato invalido. Por favor, ingrese fecha y hora en formato {bold}{yellow}"YYYY-MM-DD HH:MM".{reset} '
modulo_mensaje9 = f'{white}{bold}La hora de fin de la clase no puede ser antes que la de inicio D: {bold}{yellow}.{reset} '
modulo_mensaje10 = f'{white}{bold}La clase debe durar entre 1 y 8 horas {bold}{yellow}.{reset} '



nuevo_alumno_ascii = """
 ██████   █████                                               █████████   ████                                                
░░██████ ░░███                                               ███░░░░░███ ░░███                                                
 ░███░███ ░███  █████ ████  ██████  █████ █████  ██████     ░███    ░███  ░███  █████ ████ █████████████   ████████    ██████ 
 ░███░░███░███ ░░███ ░███  ███░░███░░███ ░░███  ███░░███    ░███████████  ░███ ░░███ ░███ ░░███░░███░░███ ░░███░░███  ███░░███
 ░███ ░░██████  ░███ ░███ ░███████  ░███  ░███ ░███ ░███    ░███░░░░░███  ░███  ░███ ░███  ░███ ░███ ░███  ░███ ░███ ░███ ░███
 ░███  ░░█████  ░███ ░███ ░███░░░   ░░███ ███  ░███ ░███    ░███    ░███  ░███  ░███ ░███  ░███ ░███ ░███  ░███ ░███ ░███ ░███
 █████  ░░█████ ░░████████░░██████   ░░█████   ░░██████     █████   █████ █████ ░░████████ █████░███ █████ ████ █████░░██████ 
░░░░░    ░░░░░   ░░░░░░░░  ░░░░░░     ░░░░░     ░░░░░░     ░░░░░   ░░░░░ ░░░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░  
══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""

alumno_mensaje1 = f'{bold}{white}Para registrar un alumno debe ingresar los siguientes datos:{reset}'
alumno_mensaje2 = f'\n{white}{bold}> Codigo numerico\n> Nombre\n> Sexo\n> Edad{reset}'
alumno_mensaje3 = f'{white}{bold}Ingrese el codigo numerico ({yellow}Debe tener entre 4 y 9 digitos{white})\n>>>{reset} '
alumno_mensaje4 = f'{white}{bold}Ingrese el nombre del alumno ({yellow}Debe tener entre 4 y 55 letras{white})\n>>>{reset} '
alumno_mensaje5 = f'{white}{bold}Ingrese el sexo del alumno ({yellow}Debe ser F o M{white})\n>>>{reset} '
alumno_mensaje6 = f'{white}{bold}Ingrese la edad del alumno ({yellow}Debe ser entre 8 y 99{white})\n>>>{reset} '

nuevo_docente_ascii = """
 ██████   █████                                             ██████████                                          █████            
░░██████ ░░███                                             ░░███░░░░███                                        ░░███             
 ░███░███ ░███  █████ ████  ██████  █████ █████  ██████     ░███   ░░███  ██████   ██████   ██████  ████████   ███████    ██████ 
 ░███░░███░███ ░░███ ░███  ███░░███░░███ ░░███  ███░░███    ░███    ░███ ███░░███ ███░░███ ███░░███░░███░░███ ░░░███░    ███░░███
 ░███ ░░██████  ░███ ░███ ░███████  ░███  ░███ ░███ ░███    ░███    ░███░███ ░███░███ ░░░ ░███████  ░███ ░███   ░███    ░███████ 
 ░███  ░░█████  ░███ ░███ ░███░░░   ░░███ ███  ░███ ░███    ░███    ███ ░███ ░███░███  ███░███░░░   ░███ ░███   ░███ ███░███░░░  
 █████  ░░█████ ░░████████░░██████   ░░█████   ░░██████     ██████████  ░░██████ ░░██████ ░░██████  ████ █████  ░░█████ ░░██████ 
░░░░░    ░░░░░   ░░░░░░░░  ░░░░░░     ░░░░░     ░░░░░░     ░░░░░░░░░░    ░░░░░░   ░░░░░░   ░░░░░░  ░░░░ ░░░░░    ░░░░░   ░░░░░░  
══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
"""

asistencia_ascii = """
   █████████            ███           █████                                  ███           
  ███░░░░░███          ░░░           ░░███                                  ░░░            
 ░███    ░███   █████  ████   █████  ███████    ██████  ████████    ██████  ████   ██████  
 ░███████████  ███░░  ░░███  ███░░  ░░░███░    ███░░███░░███░░███  ███░░███░░███  ░░░░░███ 
 ░███░░░░░███ ░░█████  ░███ ░░█████   ░███    ░███████  ░███ ░███ ░███ ░░░  ░███   ███████ 
 ░███    ░███  ░░░░███ ░███  ░░░░███  ░███ ███░███░░░   ░███ ░███ ░███  ███ ░███  ███░░███ 
 █████   █████ ██████  █████ ██████   ░░█████ ░░██████  ████ █████░░██████  █████░░████████
░░░░░   ░░░░░ ░░░░░░  ░░░░░ ░░░░░░     ░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░  ░░░░░░░░ 
═══════════════════════════════════════════════════════════════════════════════════════════
"""

consultas_ascii = """
   █████████                                         ████   █████                     
  ███░░░░░███                                       ░░███  ░░███                      
 ███     ░░░   ██████  ████████    █████  █████ ████ ░███  ███████    ██████    █████ 
░███          ███░░███░░███░░███  ███░░  ░░███ ░███  ░███ ░░░███░    ░░░░░███  ███░░  
░███         ░███ ░███ ░███ ░███ ░░█████  ░███ ░███  ░███   ░███      ███████ ░░█████ 
░░███     ███░███ ░███ ░███ ░███  ░░░░███ ░███ ░███  ░███   ░███ ███ ███░░███  ░░░░███
 ░░█████████ ░░██████  ████ █████ ██████  ░░████████ █████  ░░█████ ░░████████ ██████ 
  ░░░░░░░░░   ░░░░░░  ░░░░ ░░░░░ ░░░░░░    ░░░░░░░░ ░░░░░    ░░░░░   ░░░░░░░░ ░░░░░░  
═══════════════════════════════════════════════════════════════════════════════════════════
"""

generar_informe_ascii = """
   █████████                                                              █████             ██████                                          
  ███░░░░░███                                                            ░░███             ███░░███                                         
 ███     ░░░   ██████  ████████    ██████  ████████  ██████  ████████     ░███ ████████   ░███ ░░░██████  ████████  █████████████    ██████ 
░███          ███░░███░░███░░███  ███░░███░░███░░███░░░░░███░░███░░███    ░███░░███░░███ ███████ ███░░███░░███░░███░░███░░███░░███  ███░░███
░███    █████░███████  ░███ ░███ ░███████  ░███ ░░░  ███████ ░███ ░░░     ░███ ░███ ░███░░░███░ ░███ ░███ ░███ ░░░  ░███ ░███ ░███ ░███████ 
░░███  ░░███ ░███░░░   ░███ ░███ ░███░░░   ░███     ███░░███ ░███         ░███ ░███ ░███  ░███  ░███ ░███ ░███      ░███ ░███ ░███ ░███░░░  
 ░░█████████ ░░██████  ████ █████░░██████  █████   ░░█████████████        █████████ █████ █████ ░░██████  █████     █████░███ █████░░██████ 
  ░░░░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░     ░░░░░░░░░░░░░        ░░░░░░░░░ ░░░░░ ░░░░░   ░░░░░░  ░░░░░     ░░░░░ ░░░ ░░░░░  ░░░░░░  
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

"""



