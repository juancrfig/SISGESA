"""Módulo 'menus'.

Este módulo contiene todas las funcionalidades relacionadas con la  
visualización de menús y submenús en la aplicación. Proporciona funcionalidades
para manejar el inicio de sesión y otras interacciones con el usuario.

El módulo importa el módulo 'art' para añadir efectos estéticos a las funciones.
"""
from packages import art, data

def registro_usuario():

    art.limpiar_pantalla()
    print(art.colorear("Bienvenido a SISGESA! El software perfecto para administrar y supervisar la asistencia en su institución educativa!", "blanco"))
    print(art.center_text(art.sisgesa))
    print(art.colorear("Dado que es la primera vez que ingresa, debemos registrar el usuario que desea usar.\nIngrese a continuación el nombre de usuario\n>>> ", "blanco"), end='')
    
    usuario = input()
    clave_inicial = data.nuevo_usuario(usuario)

    print(art.colorear(f"\nUsuario registrado exitosamente!\nSu contraseña es ", "blanco"), end='')
    print(art.colorear(clave_inicial, "amarillo"), end='')
    print(art.colorear(", recomendamos cambiarla para una mayor seguridad!", "blanco"))
    print("\nPRESIONE 'C' para continuar o cualquier otra tecla para salir")
    
    if input().lower() == 'c':
        return 0
    else:
        return 1

def login():
    """Función para manejar el inicio de sesión del usuario.

    Limpia la pantalla y solicita al usuario que ingrese su nombre de usuario
    y contraseña. 

    Raises:
        ValueError: Si el nombre de usuario o la contraseña son inválidos.
    """
    art.limpiar_pantalla()
    print(art.center_text(art.sisgesa), '\n')
    user = input(art.type_user_message)
    print()
    print(art.type_password_message, end='')
    password = art.input_password()

    if data.check_correct_login(user, password) == 0:
        return 0
    else:
        return 401
    
def main():
    art.limpiar_pantalla()
    art.main_menu()
    answer = int(input())
    return answer

def registro_grupos():

    art.limpiar_pantalla()
    print(art.nuevo_grupo)
    print(art.grupos_mensaje1, art.grupos_mensaje2)
    print(art.grupos_mensaje3, end='')
    codigo = input()

    if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
        raise ValueError
    
    print(art.grupos_mensaje4, end='')
    nombre = input().strip().replace(' ', '_').upper()

    if not (not nombre.isdigit() and 4 <= len(nombre) <= 20):
        raise ValueError
    
    print(art.grupos_mensaje5, end='')
    sigla = input().strip().upper()

    if not (sigla.isalpha() and 3 <= len(sigla) <= 6):
        raise ValueError
    
    data.cargar_grupo(codigo, nombre, sigla)
    art.data_processing_animation(art.cargando_mensaje)
    return 0

def registro_modulos():
    art.limpiar_pantalla()
    print(art.nuevo_modulo)
    print(art.modulo_mensaje1, art.modulo_mensaje2)
    print(art.modulo_mensaje3, end='')
    codigo = input()

    if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
        raise ValueError

    print(art.modulo_mensaje4, end='')
    nombre = input().strip().replace(' ', '_').upper()

    if not (not nombre.isnumeric()  and 3 <= len(nombre) <= 55):
        raise ValueError
    
    print(art.modulo_mensaje5, end='')
    duracion = input()

    if not (duracion.isnumeric() and 1 <= int(duracion) <= 99):
        raise ValueError

    horario = data.pedir_horario(duracion)

    
    data.cargar_modulo(codigo, nombre, duracion, horario)
    art.data_processing_animation(art.cargando_mensaje)
    return 0

def menu_estudiantes():

    art.limpiar_pantalla()
    print(art.pregunta_menu_alumno, end='')
    answer = input()

    match answer:
        case '1':
            registro_estudiantes()
        case '2':
            art.limpiar_pantalla()
            print(art.asignacion)
            print(art.asignacion_mensaje1, end='')
            codigo = input()
            print(art.asignacion_mensaje2, end='')
            grupo = input()
            data.asignar_grupo_alumno(codigo, grupo)
            art.data_processing_animation(art.cargando_mensaje)
        case '3':
            if asignacion_modulos() == 401:
                return 401  
        case _:
            raise ValueError

def registro_estudiantes():

    art.limpiar_pantalla()
    print(art.nuevo_alumno)
    print(art.alumno_mensaje1, art.alumno_mensaje2)
    print(art.alumno_mensaje3, end='')

    codigo = input()
    if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
        raise ValueError
    
    print(art.alumno_mensaje4, end='')
    nombre = input().strip().replace(' ', '_').upper()

    if not (not nombre.isnumeric()  and 4 <= len(nombre) <= 55):
        raise ValueError
    
    print(art.alumno_mensaje5, end='')
    sexo = input().strip().upper()

    if sexo not in ('M', 'F'):
        raise ValueError
    
    print(art.alumno_mensaje6, end='')
    edad = input()

    if not (edad.isdigit() and 16 <= int(edad) <= 27):
        raise ValueError
    
    data.cargar_alumno(codigo, nombre, sexo, edad)
    art.data_processing_animation(art.cargando_mensaje)
    return 0


def asignacion_modulos():

    art.limpiar_pantalla()
    print(art.asignacion)
    print(art.asignacion_mensaje1, end='')
    codigo = input()

    if data.check_alumno_exists(codigo):
        print(art.asignacion_mensaje3, end='')
        answer = input()

        if answer == '1':
            while True:

                if len(data.check_student_modules(codigo)) >= 3:
                       
                    print(art.volviendo)
                    art.data_processing_animation(art.asignacion_mensaje6)
                    return 401
                
        elif answer == '2':

            while True:

                art.limpiar_pantalla()
                print(art.borrar_modulo)

                if len(data.check_student_modules(codigo)) == 0:

                    print(art.asignacion_mensaje12)
                    art.data_processing_animation(art.volviendo)
                    return 401
                
                print(art.asignacion_mensaje9)
                print('-'.join(data.check_student_modules(codigo)))
                print(art.asignacion_mensaje8, end='')
                modulo = input()

                if modulo.isspace():
                    art.data_processing_animation(art.volviendo)
                    return 401

                data.eliminar_modulo(codigo, modulo)
                art.data_processing_animation(art.borrando)

def asignar_modulo_docente():
    
    while True:

        art.limpiar_pantalla()
        print(art.asignacion)
        print(art.salir)
        print(art.docentes_mensaje7, end='')
        cedula = input()

        if cedula.isspace():
            break

        if len(data.cuales_modulos_docente(cedula)) == 3:
            print(art.docentes_mensaje8)
            art.data_processing_animation(art.volviendo)
            return 401
        else:
            print(art.asignacion_mensaje4, end='')
            modulo = input()
            data.asignar_modulo_docente(cedula, modulo)
            art.data_processing_animation(art.cargando_mensaje)

def docentes():

    art.limpiar_pantalla()
    print(art.nuevo_docente)
    print(art.docentes_mensaje1, end='')
    answer = input()

    if answer == '1':

        registro_docente()

    elif answer == '2':

        asignar_modulo_docente()
        return 401
    
    elif answer == '3':

        eliminar_modulo_docente()
        return 401

    else:
        raise ValueError


def eliminar_modulo_docente():

    art.limpiar_pantalla()
    print(art.borrar_modulo)
    print(art.docentes_mensaje7, end='')
    cedula = input()

    while True:

        art.limpiar_pantalla()
        print(art.borrar_modulo)
        if len(data.cuales_modulos_docente(cedula)) == 0:

            print(art.docentes_mensaje9)
            art.data_processing_animation(art.volviendo)
            return 401
        
        print(art.docentes_mensaje6)
        print('-'.join(data.cuales_modulos_docente(cedula)))
        print(art.asignacion_mensaje8, end='')
        modulo = input()

        if modulo.isspace():
            return 401
        
        data.borrar_modulo_docente(cedula, modulo)
        art.data_processing_animation(art.borrando)




  

def registro_docente():

    art.limpiar_pantalla()
    print(art.nuevo_docente)
    print(art.docentes_mensaje2, art.docentes_mensaje3)
    print(art.docentes_mensaje4, end='')
    cedula = input()

    if not (cedula.isdigit() and 1 <= len(cedula) <= 10):
        raise ValueError
    
    print(art.docentes_mensaje5,end='')
    nombre = input().strip().replace(' ', '_').upper()

    if not (not nombre.isdigit() and 3 <= len(nombre) <= 55):
        raise ValueError
    
    data.cargar_docente(cedula, nombre)
    art.data_processing_animation(art.cargando_mensaje)
    return 0    

def registro_asistencia():

    art.limpiar_pantalla()
    print(art.asistencia)
    print(art.colorear("Ingresa el codigo del estudiante\n>>> ", "white"))
    codigo = input()

def consultar_info():
    art.limpiar_pantalla()
    print(art.consultas)
    input("Llegaste a la consulta de información!")

def generar_informe():
    art.limpiar_pantalla()
    print(art.generar_informe)
    input("Llegaste a la generación de informes!")

def cambio_contra():

    art.limpiar_pantalla()
    print(art.cambio_de_clave)
    print(art.cambio_clave_m1, end='')
    user = input()
    print(art.cambio_clave_m2, end='')
    password = art.input_password()

    if data.check_correct_login(user, password) == 0:
        print(art.validacion_exito_mensaje)
        print(art.cambio_clave_m3, end='')
        new_pass = art.input_password()
        print(art.cambio_clave_m5, end='')
        new_pass2 = art.input_password()

        if new_pass != new_pass2:
            print(art.seguridad_mensaje)
            art.data_processing_animation(art.cambio_clave_m6)
            return 401
        
        data.change_password(user, new_pass)
        print(art.cambio_clave_m4)
        art.data_processing_animation('')
        return 0

    else:
        print(art.seguridad_mensaje)
        art.data_processing_animation(art.user_invalid_input_message)
        return 401