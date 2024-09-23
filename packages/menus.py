"""Módulo 'menus'.

Este módulo contiene todas las funcionalidades relacionadas con la  
visualización de menús y submenús en la aplicación. Proporciona funcionalidades
para manejar el inicio de sesión y otras interacciones con el usuario.

El módulo importa el módulo 'art' para añadir efectos estéticos a las funciones.
"""
from packages import art, data

def registro_usuario():
    """Muestra las instrucciones a seguir por el usuario la primera vez que usa el programa.

    Returns:
        1 (int): Para señalar que el usuario desea continuar en el programa, en vez de salir.
    """
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
    
    if not input().lower() == 'c':
        return 1

def ingresar():
    """Función para manejar el inicio de sesión del usuario.

    Limpia la pantalla y solicita al usuario que ingrese su nombre de usuario
    y contraseña. 

    Raises:
        ValueError: Si el nombre de usuario o la contraseña son inválidos.
    """
    art.limpiar_pantalla()
    print(art.center_text(art.sisgesa), '\n')
    usuario = input(art.mensaje_ingresar_usuario)
    print()
    print(art.mensaje_ingresar_contraseña, end='')

    if data.validacion_usuario_clave(usuario, art.ingresar_clave()):
        return True
    return False
    
def menu_principal():
    """Función que imprime en pantalla el menú principal del programa.

    Returns:
        answer (str): La respuesta del usuario cuando se le pregunta a qué submenú quiere acceder.
    """
    art.limpiar_pantalla()
    art.tabla_menu_principal()
    answer = int(input())
    return answer

def quiere_salir(text):
    """Comprueba si el usuario quiere salir al menú principal.
    
    Args:
        text (str): Representa la última respuesta dada por el usuario.

    Returns:
        bool: True si el usuario indicó que quiere salir, False de lo contrario.
    """
    if text.isspace():
        art.animacion_cargando(art.volviendo_mensaje)
        return True
    return False

def registro_grupos():
    """Función que pide al usuario los datos requeridos para registrar un grupo."""
    art.limpiar_pantalla()
    print(art.nuevo_grupo)
    print(art.colorear("Recuerde que si desea volver al menu principial en cualquier momento solo debe presionar la barra espaciadora\n", "rojo"))
    print(art.colorear("Para registrar un grupo debe ingresar los siguientes datos:", "blanco"))
    print(art.colorear("> Codigo numerico\n> Nombre\n> Sigla\n", "blanco"))
    print(art.colorear("Ingrese el codigo numerico", "blanco"), art.colorear("(Debe tener entre 4 y 9 digitos)\n", "amarillo"), art.colorear(">>> ", "blanco"), end='')

    while True:
        try:
            codigo = input()
            if quiere_salir(codigo):
                return 
            if not (codigo.strip().isdigit() and 4 <= len(codigo.strip()) <= 9):
                raise ValueError
            print(art.colorear("Ingrese el nombre del grupo", "blanco"), art.colorear("(Debe tener entre 4 y 9 letras)\n", "amarillo"), art.colorear(">>> ", "blanco"), end='')
            nombre = input()
            if quiere_salir(nombre):
                return
            nombre = nombre.strip().replace(' ', '_').upper()
            if not (not nombre.isdigit() and 4 <= len(nombre) <= 20):
                raise ValueError
            print(art.colorear("Ingrese la sigla del grupo", "blanco"), art.colorear("(Debe tener entre 3 y 6 letras)\n", "amarillo"), art.colorear(">>> ", "blanco"), end='')
            sigla = input()
            if quiere_salir(sigla):
                return
            sigla = sigla.strip().upper()
            if not (sigla.isalpha() and 3 <= len(sigla) <= 6):
                raise ValueError
        except ValueError:
            art.animacion_cargando(art.dato_invalido_mensaje)
            continue
    
    data.cargar_grupo(codigo, nombre, sigla)
    art.animacion_cargando(art.cargando_informacion_mensaje)
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
    art.animacion_cargando(art.cargando_informacion_mensaje)
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
            art.animacion_cargando(art.cargando_informacion_mensaje)
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
    art.animacion_cargando(art.cargando_informacion_mensaje)
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
                       
                    print(art.volviendo_mensaje)
                    art.animacion_cargando(art.asignacion_mensaje6)
                    return 401
                
        elif answer == '2':

            while True:

                art.limpiar_pantalla()
                print(art.borrar_modulo)

                if len(data.check_student_modules(codigo)) == 0:

                    print(art.asignacion_mensaje12)
                    art.animacion_cargando(art.volviendo_mensaje)
                    return 401
                
                print(art.asignacion_mensaje9)
                print('-'.join(data.check_student_modules(codigo)))
                print(art.asignacion_mensaje8, end='')
                modulo = input()

                if modulo.isspace():
                    art.animacion_cargando(art.volviendo_mensaje)
                    return 401

                data.eliminar_modulo(codigo, modulo)
                art.animacion_cargando(art.borrando)

def asignar_modulo_docente():
    
    while True:

        art.limpiar_pantalla()
        print(art.asignacion)
        print(art.salir_tecla_espaciadora_mensaje)
        print(art.docentes_mensaje7, end='')
        cedula = input()

        if cedula.isspace():
            break

        if len(data.cuales_modulos_docente(cedula)) == 3:
            print(art.docentes_mensaje8)
            art.animacion_cargando(art.volviendo_mensaje)
            return 401
        else:
            print(art.asignacion_mensaje4, end='')
            modulo = input()
            data.asignar_modulo_docente(cedula, modulo)
            art.animacion_cargando(art.cargando_informacion_mensaje)

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
            art.animacion_cargando(art.volviendo_mensaje)
            return 401
        
        print(art.docentes_mensaje6)
        print('-'.join(data.cuales_modulos_docente(cedula)))
        print(art.asignacion_mensaje8, end='')
        modulo = input()

        if modulo.isspace():
            return 401
        
        data.borrar_modulo_docente(cedula, modulo)
        art.animacion_cargando(art.borrando)




  

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
    art.animacion_cargando(art.cargando_informacion_mensaje)
    return 0    

def registro_asistencia():

    art.limpiar_pantalla()
    print(art.asistencia)
    print(art.colorear("Ingresa el codigo del estudiante\n>>> ", "blanco"))
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
    password = art.ingresar_clave()

    if data.validacion_usuario_clave(user, password) == 0:
        print(art.validacion_exito_mensaje)
        print(art.cambio_clave_m3, end='')
        new_pass = art.ingresar_clave()
        print(art.cambio_clave_m5, end='')
        new_pass2 = art.ingresar_clave()

        if new_pass != new_pass2:
            print(art.seguridad_mensaje)
            art.animacion_cargando(art.cambio_clave_m6)
            return 401
        
        data.change_password(user, new_pass)
        print(art.cambio_clave_m4)
        art.animacion_cargando('')
        return 0

    else:
        print(art.seguridad_mensaje)
        art.animacion_cargando(art.error_archivo_m1)
        return 401