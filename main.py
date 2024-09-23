"""Módulo principal del programa.

Este módulo proporciona el punto de entrada para el programa.
Importa varios módulos contenidos en el paquete 'packages'.
"""
from packages import menus, data, art

def main():
    """Función principal para iniciar el programa

    Esta función llama a la función 'ingresar', iniciando el proceso de inicio 
    de sesión del usuario.

    Si es el primer ingreso al programa, se crean los archivos JSON en los que se
    almacenarán las creendenciales del usuario y toda la información de la institución.
    """
    while True:
        if data.primera_vez():
            data.crear_estructura_json()
            if menus.registro_usuario() == 1:
                break
        else:
            if menus.ingresar():
                while True:
                    try:
                        match menus.menu_principal(): 
                            case 1:
                                menus.registro_grupos()
                            case 2:
                                menus.registro_modulos()
                            case 3:
                                menus.menu_estudiantes()
                            case 4:
                                menus.docentes()
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
                            art.animacion_cargando(art.colorear("Opcion invalida. Intente nuevamente...", "rojo"))
                            continue
                        if isinstance(error, FileNotFoundError):
                            data.crear_estructura_json()
                            print(art.error_archivo_m1)
                            art.animacion_cargando('Cargando', 8)
                            continue
            else:
                art.animacion_cargando(art.colorear("Ha ingresado un usuario y/o contraseña incorrectos!\nIntente nuevamente!", "rojo"))
                continue
    art.animacion_cargando(art.colorear("Cerrando el programa\nUn momento, por favor...", "verde"))
    art.despedida()


if __name__ == '__main__':
    main()