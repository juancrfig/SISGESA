"""Módulo principal del programa.

Este módulo proporciona el punto de entrada para el programa.
Importa varios módulos contenidos en el paquete 'packages'.
"""
from packages import menus, data, art

def main():
    """Función principal para iniciar el programa

    Esta función llama a la función 'login' contenida en el módulo 'menus',
    iniciando el proceso de inicio de sesión del usuario.

    Se usará el número 9 para señalar cuando el usuario quiera regresar al menú
    anterior o salir del programa.
    Se usará el numero 0 para señalar una validación de información exitosa.
    """
    while True:
        if data.check_first_time():
            if menus.first_login() == 9:
                break
        else:
            if menus.login() == 0:
                match menus.main(): 
                    case 1:
                        menus.registro_grupos()
                    case 2:
                        menus.registro_modulos()
                    case 3:
                        menus.registro_estudiantes()
                    case 4:
                        menus.registro_docentes()
                    case 5:
                        menus.registro_asistencia()
                    case 6:
                        menus.consultar_info()
                    case 7:
                        menus.generar_informe()
                    case 8:
                        menus.cambio_contra()
                    case 9:
                        break
                    case _:
                        raise ValueError
            else:
                art.data_processing_animation(art.user_pass_incorrect_message)
                continue
    art.despedida()


if __name__ == '__main__':
    main()