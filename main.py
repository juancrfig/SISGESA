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
            data.crear_estructura_json()
            if menus.first_login() == 9:
                break
        else:
            if menus.login() == 0:
                while True:
                    try:
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
                                art.despedida()
                                return 0
                            case _:
                                raise ValueError
                    except (ValueError, FileNotFoundError) as error:

                        if isinstance(error, ValueError):

                            art.data_processing_animation(art.user_invalid_input_message)
                            continue

                        if isinstance(error, FileNotFoundError):

                            data.crear_estructura_json()
                            print(art.error_archivo_m1)
                            art.data_processing_animation('Cargando', 8)
                            continue
                        
                        else:

                            print(f"Ha ocurrido el error {error}.\nComuniquese con el desarrollador...")
                            return 401
            else:

                art.data_processing_animation(art.user_pass_incorrect_message)
                continue

    art.despedida()

if __name__ == '__main__':
    main()