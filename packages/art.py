"""Módulo 'art'.

Este módulo almacena variables y funciones que mejoran la estética del programa.
"""
from colorama import Fore, Style
import sys
import tty
import termios
import time

# Variables para personalizar la estética del texto en la terminal
negrita = "\033[1m"
blanco = "\033[37m"
rojo = "\033[31m"
verde = "\033[32m"
amarillo = "\033[33m"
azul = "\033[34m"
reset = "\033[0m"

# Variables de mensajes predefinidos
salir_tecla_espaciadora_mensaje = f'{negrita}{rojo}Para salir presione la tecla espaciadora\n{reset}'
volver_menu_principal_espaciadora = f"\n{rojo}Presione la barra espaciadora para volver al menu principal\n"
volviendo_mensaje = f'{amarillo}{negrita}Regresando al menu anterior...{reset}'
dato_invalido_mensaje = f'{rojo}{negrita}Ha ingresado un dato invalido...Vuelva a intentarlo, por favor.'
validando_mensaje = f'{amarillo}{negrita}Validando informacion\nUn momento, por favor...{reset}'
validacion_exito_mensaje = f'{verde}{negrita}\n\nValidación exitosa!{reset}'
cargando_informacion_mensaje = f'{verde}{negrita}Cargando la informacion...Un momento...{reset}'

def limpiar_pantalla():
    """Función para limpiar la pantalla de la terminal.
    
    Usar el código de espace ANSI para limpiar la pantalla, este funciona así:
        '\033c' indica a la terminal que el texto a continuación debe ser 
        interpretado como un comando, en vez de texto normal.
        'c' es el comando que la terminal leerá, el cual borra la pantalla.
    """
    print('\033c')

def colorear(texto, color, negrita=True):
    """Aplica color y/o formato en negrita a un texto dado.

    Args:
        texto (str): El texto que se desea formatear.
        color (str): El color que se aplicará al texto. Valores posibles son:
            'blanco', 'rojo', 'verde', 'amarillo' o 'azul'.
        negrita (bool, opcional): Si es True, se aplica formato en negrita. 
            El valor projoeterminado es True.

    Returns:
        str: El texto formateado con el color y/o negrita aplicados.

    Raises:
        ValueError: Si el color proporcionado no está entre los colores soportados.
    """
    colores = {
        "blanco": "\033[37m",
        "rojo": "\033[31m",
        "verde": "\033[32m",
        "amarillo": "\033[33m",
        "azul": "\033[34m"
    }
    if color not in colores:
        raise ValueError(f'Color "{color}" invalido en la funcion {colorear.__name__}')   
    formato_negrita = '\033[1m' if negrita else ''
    return f'{formato_negrita}{colores[color]}{texto}\033[0m'

def center_text(text, width=160):
    """Función para centrar cadenas de texto multilínea.

    Esta función recibe un texto y lo centra en un ancho especificado.

    Args:
        text (str): El texto que se centra, puede contener varias lineas.
        width (int): El ancho total en el que se desea centrar el texto. 

    Returns:
        str: El texto centrado, con cada línea ajustada al ancho especificado.
    """
    lines = text.splitlines() 
    centerojo_lines = [line.center(width) for line in lines] 
    return "\n".join(centerojo_lines) 

def despedida():
    """Genera una pantalla de despedida cuando el usuario sale del programa."""
    animacion_cargando(colorear("Cerrando el programa\nUn momento, por favor...", "verde"))
    limpiar_pantalla()
    print(adios)
    sys.exit()

docentes_mensaje1 = f'{negrita}{blanco}Ingrese 1 para agregar un nuevo docente\nIngrese 2 para asignar un docente existente a un modulo\nIngrese 3 para borrar modulos asociados con un docentes\n>>>{reset} '
docentes_mensaje2 = f'{negrita}{blanco}Para registrar un docente debe ingresar los siguientes datos:{reset}'
docentes_mensaje3 = f'\n{blanco}{negrita}> Cedula\n> Nombre{reset}'
docentes_mensaje4 = f'{blanco}{negrita}Ingrese la cedula ({amarillo}Debe tener entre 1 y 10 digitos{blanco})\n>>>{reset} '
docentes_mensaje5 = f'{blanco}{negrita}Ingrese el nombre del docente ({amarillo}Debe tener entre 3 y 55 letras{blanco})\n>>>{reset} '
docentes_mensaje6 = f'{blanco}{negrita}El docente tiene asignados los siguientes modulos...{reset} '
docentes_mensaje8 = f'{blanco}{negrita}El docente tiene ya asignada la cantidad maxima de modulos {amarillo}(3){blanco}!{reset} '
docentes_mensaje9 = f'{blanco}{negrita}El docente no tiene ningun modulo asignado!{blanco}!{reset} '


def tabla_menu_principal():
    """Imprime en pantalla la tabla que contiene el menú de opciones principales del programa."""
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
    print(f">>> {blanco}", end='')

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

def ingresar_clave():
    """Falta todavía entender la función!!!"""

    clave = ""
    
    while True:
        char = getch()
        if char in ('\n', '\r'):
            print() 
            break
        elif char == '\x7f':
            if clave:
                clave = clave[:-1]
                print('\b \b', end='', flush=True)
        else:
            clave += char
            print('*', end='', flush=True)

    return clave

def animacion_barra_progreso(message, duration=3):
    print(f"\n{message}")
    width = 38
    start_time = time.time()

    # Progress bar animation
    while time.time() - start_time < duration:
        elapsed = time.time() - start_time
        filled = int(width * elapsed / duration)
        bar = f"[{'=' * filled}{' ' * (width - filled)}]"
        percent = min(100, int(100 * elapsed / duration))  # Ensures it never goes beyond 100%
        print(f"\r{bar} {percent}%", end="", flush=True)
        time.sleep(0.1)

    bar = f"[{'=' * width}]"
    print(f"\r{bar} 100%")


def animacion_cargando(message, duration=1):
    print(f"\n{message}\n")
    marcador = ['⬛⬛⬛', '⬛⬛⬜', '⬛⬜⬛', '⬜⬛⬛']
    start_time = time.time()

    while time.time() - start_time < duration:
        for char in marcador:
            sys.stdout.write(f"\r{char}")
            sys.stdout.flush()
            time.sleep(0.2)

# Arte ASCII para los diferentes menus del programa.
sisgesa = """
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
borrar_modulo = """
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐ ███████████                                                      ██████   ██████              █████            ████          ▌
▐░░███░░░░░███                                                    ░░██████ ██████              ░░███            ░░███          ▌
▐ ░███    ░███  ██████  ████████  ████████   ██████   ████████     ░███░█████░███   ██████   ███████  █████ ████ ░███   ██████ ▌
▐ ░██████████  ███░░███░░███░░███░░███░░███ ░░░░░███ ░░███░░███    ░███░░███ ░███  ███░░███ ███░░███ ░░███ ░███  ░███  ███░░███▌
▐ ░███░░░░░███░███ ░███ ░███ ░░░  ░███ ░░░   ███████  ░███ ░░░     ░███ ░░░  ░███ ░███ ░███░███ ░███  ░███ ░███  ░███ ░███ ░███▌
▐ ░███    ░███░███ ░███ ░███      ░███      ███░░███  ░███         ░███      ░███ ░███ ░███░███ ░███  ░███ ░███  ░███ ░███ ░███▌
▐ ███████████ ░░██████  █████     █████    ░░████████ █████        █████     █████░░██████ ░░████████ ░░████████ █████░░██████ ▌
▐░░░░░░░░░░░   ░░░░░░  ░░░░░     ░░░░░      ░░░░░░░░ ░░░░░        ░░░░░     ░░░░░  ░░░░░░   ░░░░░░░░   ░░░░░░░░ ░░░░░  ░░░░░░  ▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
"""
asignacion =r"""
/================================================================================================\
||   █████████            ███                                          ███                      ||
||  ███░░░░░███          ░░░                                          ░░░                       ||
|| ░███    ░███   █████  ████   ███████ ████████    ██████    ██████  ████   ██████  ████████   ||
|| ░███████████  ███░░  ░░███  ███░░███░░███░░███  ░░░░░███  ███░░███░░███  ███░░███░░███░░███  ||
|| ░███░░░░░███ ░░█████  ░███ ░███ ░███ ░███ ░███   ███████ ░███ ░░░  ░███ ░███ ░███ ░███ ░███  ||
|| ░███    ░███  ░░░░███ ░███ ░███ ░███ ░███ ░███  ███░░███ ░███  ███ ░███ ░███ ░███ ░███ ░███  ||
|| █████   █████ ██████  █████░░███████ ████ █████░░████████░░██████  █████░░██████  ████ █████ ||
||░░░░░   ░░░░░ ░░░░░░  ░░░░░  ░░░░░███░░░░ ░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░  ||
||                             ███ ░███                                                         ||
||                            ░░██████                                                          ||
||                             ░░░░░░                                                           ||
\================================================================================================/
"""
generar_informe = """
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
consultas = """
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
asistencia = """
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
nuevo_docente = """
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
nuevo_alumno = """
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
nuevo_modulo = """
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
nuevo_grupo = """

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
cambio_de_clave = """

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


x = f'{negrita}{blanco}Ingrese su usuario{reset}'.center(170)
prompt_symbol = f'{negrita}{blanco}>>> {reset}'.rjust(85)
mensaje_ingresar_usuario = f'{x}\n\n{prompt_symbol}'
y = f'{negrita}{blanco}Ingrese su contraseña{reset}'.center(170)
mensaje_ingresar_contraseña = f'{y}\n\n{prompt_symbol}'

tabla_consultas = """
┌──────────────────────────────────────────────────────────────────────────────┐
│                           \033[1;34mOpciones de consulta\033[0m                               │
├──────────────────────────────────────────────────────────────────────────────┤
│ \033[1;37m1  - Consultar los estudiantes matriculados en un grupo\033[0m                      │
│ \033[1;37m2  - Consultar los estudiantes inscritos en un módulo\033[0m                        │
│ \033[1;37m3  - Consultar los docentes que imparten un módulo\033[0m                           │
│ \033[1;37m4  - Consultar los estudiantes a cargo de un docente en un módulo\033[0m            │
└──────────────────────────────────────────────────────────────────────────────┘
"""