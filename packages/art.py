"""Módulo 'art'.

Este módulo almacena variables y funciones que mejoran la estética del programa.
"""
from colorama import Fore, Style
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

def colorear(texto, color, negrita=True):
    """Aplica color y/o formato en negrita a un texto dado.

    Args:
        texto (str): El texto que se desea formatear.
        color (str): El color que se aplicará al texto. Valores posibles son:
            'blanco', 'rojo', 'verde', 'amarillo' o 'azul'.
        negrita (bool, opcional): Si es True, se aplica formato en negrita. 
            El valor predeterminado es True.

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

# Variables para personalizar la estética del texto en la terminal
bold = "\033[1m"
white = "\033[37m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
reset = "\033[0m"

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
    centered_lines = [line.center(width) for line in lines] 
    return "\n".join(centered_lines) 

def despedida():
    """Genera una pantalla de despedida cuando el usuario sale del programa."""
    limpiar_pantalla()
    print(adios)

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
    print(f">>> {white}", end='')

cambio_clave_m1 = f'{bold}{white}Ingrese su usuario\n>>>{reset} '
cambio_clave_m2 = f'{bold}{white}Ingrese la clave actual\n>>>{reset} '
cambio_clave_m3 = f'{bold}{white}Ingrese la nueva clave\n>>>{reset} '
cambio_clave_m4 = f'{bold}{white}Se ha cambiado la clave exitosamente!\nVolviendo al menú!{reset}'
cambio_clave_m5 = f'{bold}{white}Ingrese la nueva clave otra vez\n>>>{reset} '
cambio_clave_m6 = f'{bold}{white}Las claves no coinciden!\n>>>{reset} '

cargando_mensaje = f'{white}{bold}Cargando la informacion...Un momento...{reset}'
validacion_exito_mensaje = f'{white}{bold}Validación exitosa!{reset}'
seguridad_mensaje = f'{white}{bold}Por razones de seguridad, volverá al menú anterior...{reset}'
volviendo_mensaje_mal_input = f'{white}{bold}Se ha detectado un dato invalido. Volviendo al paso anterior...{reset}'
borrando = f'{white}{bold}Borrando la informacion...{reset}'
volviendo = f'{white}{bold}Regresando al menu anterior...{reset}'


error_archivo_m1 = f'''\033c{white}{bold}Alguien a averiado el archivo en el que se guardaba la informacion!\n
No te preocupes, hemos creado un nuevo archivo para que vuelvas a intentarlo!\n
({yellow}Tenias un respaldo de la informacion, cierto? D:{white}){reset}'''



modulo_mensaje1 = f'{bold}{white}Para registrar un modulo debe ingresar los siguientes datos:{reset}'
modulo_mensaje2 = f'\n{white}{bold}> Codigo numerico\n> Nombre\n> Duracion en semanas\n> Horario{reset}'
modulo_mensaje3 = f'{white}{bold}Ingrese el codigo numerico ({yellow}Debe tener entre 4 y 9 digitos{white})\n>>>{reset} '
modulo_mensaje4 = f'{white}{bold}Ingrese el nombre del modulo ({yellow}Debe tener entre 4 y 55 letras{white})\n>>>{reset} '
modulo_mensaje5 = f'{white}{bold}Ingrese la duracion del modulo en semanas ({yellow}Debe tener entre 1 y 2 digitos{white})\n>>>{reset} '
modulo_mensaje6 = f'{white}{bold}Ingrese la fecha y hora de inicio del modulo ({yellow}"YYYY-MM-DD HH:MM" formato 24 horas"{white})\n>>>{reset} '
modulo_mensaje7 = f'{white}{bold}Ingrese el horario de fin del modulo ({yellow}"HH:MM" formato 24 horas"{white})\n>>>{reset} '
modulo_mensaje8 = f'{white}{bold}Formato invalido. Por favor, ingrese fecha y hora en formato {bold}{yellow}"YYYY-MM-DD HH:MM".{reset} '
modulo_mensaje9 = f'{white}{bold}La hora de fin de la clase no puede ser antes que la de inicio D: {bold}{yellow}.{reset} '
modulo_mensaje10 = f'{white}{bold}La clase debe durar entre 1 y 8 horas {bold}{yellow}.{reset} '
modulo_mensaje11 = f'{white}{bold}Los modulos puede comenzar a las 05:00 y el ultimo puede empezar a las 18:00 como maximo{bold}{yellow}.{reset} '
modulo_mensaje12 = f'{white}{bold}Los modulos puede acabar desde las 06:00 y el ultimo puede acabar a las 23:00 como maximo{bold}{yellow}.{reset} '





alumno_mensaje1 = f'{bold}{white}Para registrar un alumno debe ingresar los siguientes datos:{reset}'
alumno_mensaje2 = f'\n{white}{bold}> Codigo numerico\n> Nombre\n> Sexo\n> Edad{reset}'
alumno_mensaje3 = f'{white}{bold}Ingrese el codigo numerico ({yellow}Debe tener entre 4 y 9 digitos{white})\n>>>{reset} '
alumno_mensaje4 = f'{white}{bold}Ingrese el nombre del alumno ({yellow}Debe tener entre 3 y 55 letras{white})\n>>>{reset} '
alumno_mensaje5 = f'{white}{bold}Ingrese el sexo del alumno ({yellow}Debe ser F o M{white})\n>>>{reset} '
alumno_mensaje6 = f'{white}{bold}Ingrese la edad del alumno ({yellow}Debe ser entre 17 y 27{white})\n>>>{reset} '









pregunta_menu_alumno = f'{bold}{white}\nIngrese 1 para agregar un nuevo alumno\nIngrese 2 para asignar o editar el grupo asignado a un alumno\nIngrese 3 para editar los modulos asignados a un estudiante\n>>>{reset} '



asignacion_mensaje1 = f'{bold}{white}Ingrese el codigo del estudiante\n>>> {reset}'
asignacion_mensaje2 = f'{bold}{white}Ingrese el codigo del grupo al que desea asignar al alumno\n>>> {reset}'
asignacion_mensaje3 = f'{bold}{white}\nPara registrar alumno en un modulo ingrese 1\nPara eliminar modulos asociados con un estudiante escriba 2\n>>> {reset}'
asignacion_mensaje4 = f'{bold}{white}Ingrese el codigo del modulo al que desea asignar\n>>> {reset}'
asignacion_mensaje5 = f'{bold}{white}Recuerde que puede asignar hasta 3 modulos por estudiante\nPara {yellow}parar {white}de asignar modulos presione la {yellow}barra espaciadora{reset}'
asignacion_mensaje6 = f'{bold}{white}El alumno ha alcanzado el limite de modulos a los que puede estar matriculado!{reset}'
asignacion_mensaje7 = f'{bold}{white}El alumno se encuentra matriculado actualmente en al menos un modulo\n\nPara matricular al estudiante en mas modulos presione 2{reset}'
asignacion_mensaje8 = f'{bold}{white}\nIngrese el codigo del modulo que desea eliminar\nPara salir presione la tecla espaciadora\n>>> {reset}'
asignacion_mensaje9 = f'{bold}{white}El alumno esta inscrito actualmente en los siguientes modulos...\n{reset}'
asignacion_mensaje10 = f'{bold}{white}No se registran modulos asociados para el estudiante{reset}'
asignacion_mensaje11 = f'{bold}{white}Recuerde que puede asignar hasta 3 modulos por estudiante{reset}'
asignacion_mensaje12 = f'{bold}{white}El estudiante no esta asociado a ningun modulo!{reset}'
asignacion_mensaje_error1 = f'{bold}{white}El codigo de estudiante no existe!{reset}'




docentes_mensaje1 = f'{bold}{white}Ingrese 1 para agregar un nuevo docente\nIngrese 2 para asignar un docente existente a un modulo\nIngrese 3 para borrar modulos asociados con un docentes\n>>>{reset} '
docentes_mensaje2 = f'{bold}{white}Para registrar un docente debe ingresar los siguientes datos:{reset}'
docentes_mensaje3 = f'\n{white}{bold}> Cedula\n> Nombre{reset}'
docentes_mensaje4 = f'{white}{bold}Ingrese la cedula ({yellow}Debe tener entre 1 y 10 digitos{white})\n>>>{reset} '
docentes_mensaje5 = f'{white}{bold}Ingrese el nombre del docente ({yellow}Debe tener entre 3 y 55 letras{white})\n>>>{reset} '
docentes_mensaje6 = f'{white}{bold}El docente tiene asignados los siguientes modulos...{reset} '
docentes_mensaje7 = f'{white}{bold}Ingrese la cedula del docente\n>>>{reset} '
docentes_mensaje8 = f'{white}{bold}El docente tiene ya asignada la cantidad maxima de modulos {yellow}(3){white}!{reset} '
docentes_mensaje9 = f'{white}{bold}El docente no tiene ningun modulo asignado!{white}!{reset} '

salir = f'{bold}{white}Para salir presione la tecla espaciadora'

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

def animacion_barra_progreso(message, duration=3):
    print(f"\n{message}")
    width = 40
    start_time = time.time()

    while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            filled = int(width * elapsed / duration)
            bar = f"[{'=' * filled}{' ' * (width - filled)}]"
            percent = int(100 * elapsed / duration)
            print(f"\r{bar} {percent}%", end="", flush=True)
            time.sleep(0.1)

    while time.time() - start_time < duration:
            for symbol in loading_symbols:
                sys.stdout.write(f"\r{symbol}")
                sys.stdout.flush()
                time.sleep(0.2)

def animacion_cargando(message, duration=3):
    print(f"\n{message}")
    start_time = time.time()
    
    while time.time() - start_time < duration:
        for i in range(4):
            print(f"\r{'.' * i}", end="", flush=True)
            time.sleep(0.2)
        for i in range(4, 0, -1):
            print(f"\r{'.' * i}", end="", flush=True)
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


x = f'{bold}{white}Ingrese su usuario{reset}'.center(170)
prompt_symbol = f'{bold}{white}>>> {reset}'.rjust(85)
mensaje_ingresar_usuario = f'{x}\n\n{prompt_symbol}'
y = f'{bold}{white}Ingrese su contraseña{reset}'.center(170)
mensaje_ingresar_contraseña = f'{y}\n\n{prompt_symbol}'