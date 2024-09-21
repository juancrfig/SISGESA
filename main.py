"""Módulo principal del programa.

Este módulo proporciona el punto de entrada para el programa.
Importa varios módulos contenidos en el paquete 'packages'.
"""
from packages import menus, data, art

def main():
    """Función principal para iniciar el programa

    Esta función llama a la función 'login' contenida en el módulo 'menus',
    iniciando el proceso de inicio de sesión del usuario.
    """
    while True:
        if data.first_time():
            if menus.first_login() == 1:
                break
        else:
            menus.login()
    art.despedida()


if __name__ == '__main__':
    main()