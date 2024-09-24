"""Módulo 'menus'.

Este módulo contiene todas las funcionalidades relacionadas con la  
visualización de menús y submenús en la aplicación. Proporciona funcionalidades
para manejar el inicio de sesión y otras interacciones con el usuario.

El módulo importa el módulo 'art' para añadir efectos estéticos a las funciones.
"""
from datetime import datetime, timedelta, time
from packages import art, data

def registro_usuario():
    """Muestra las instrucciones a seguir por el usuario la primera vez que usa el programa.

    Returns:
        1 (int): Para señalar que el usuario desea continuar en el programa, en vez de salir.
    """
    while True:
        art.limpiar_pantalla()
        print(art.colorear("Bienvenido a SISGESA! El software perfecto para administrar y supervisar la asistencia en su institución educativa!", "blanco"))
        print(art.center_text(art.sisgesa))
        print(art.colorear("Para salir digite el numero 1!\n", "rojo"))
        print(art.colorear("Dado que es la primera vez que ingresa, debemos registrar el usuario que desea usar\n", "blanco"), art.colorear("\nEl nombre de usuario debe ser de al menos 4 caracteres y solo letras", "amarillo"))
        print(art.colorear("Ingrese el nombre de usuario que desea usar\n>>> ", "blanco"), end='')
        usuario = input()
        if not (usuario.isalpha() and len(usuario) > 3):
            art.animacion_cargando(art.colorear("Ha ingresado un usuario invalido! Intentelo nuevamente...", "rojo"))
            continue
        clave_inicial = data.nuevo_usuario(usuario)
        print(art.colorear(f"\nUsuario registrado exitosamente!\nSu contraseña es ", "blanco"), end='')
        print(art.colorear(clave_inicial, "amarillo"), end='')
        print(art.colorear(", recomendamos cambiarla para una mayor seguridad!", "blanco"))
        print(art.colorear("\nPRESIONE 'C' para continuar o cualquier otra tecla para salir\n>>> ", "amarillo"), end='')

        return input().lower()

def ingresar():
    """Función para manejar el inicio de sesión del usuario.

    Limpia la pantalla y solicita al usuario que ingrese su nombre de usuario
    y contraseña. 

    Raises:
        ValueError: Si el nombre de usuario o la contraseña son inválidos.
    """
    while True:
        art.limpiar_pantalla()
        print(art.center_text(art.sisgesa), '\n')
        print(art.colorear("Presione la tecla espaciadora para salir\n", "amarillo"))
        usuario = input(art.mensaje_ingresar_usuario)
        if usuario.isspace():
            art.despedida()
        print()
        print(art.mensaje_ingresar_contraseña, end='')
        clave =  art.ingresar_clave()
        if clave.isspace():
            art.despedida()
        art.animacion_barra_progreso(art.colorear(art.validando_mensaje, "amarillo"))
        if data.validacion_usuario_clave(usuario, clave):
            print(art.colorear(art.validacion_exito_mensaje, "verde"))
            art.animacion_cargando(art.colorear("Ingresando a SISGESA", "verde"))
            return True
        else:
            art.animacion_cargando(art.dato_invalido_mensaje)
            continue
    
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
    while True:
        try:
            art.limpiar_pantalla()
            print(art.nuevo_grupo)
            print(art.colorear("Recuerde que si desea volver al menu principial en cualquier momento solo debe presionar la barra espaciadora\n", "rojo"))
            print(art.colorear("Para registrar un grupo debe ingresar los siguientes datos:", "blanco"))
            print(art.colorear("> Codigo numerico\n> Nombre\n> Sigla\n", "blanco"))
            print(art.colorear("Ingrese el codigo numerico", "blanco"), art.colorear("(Debe tener entre 4 y 9 digitos)\n", "amarillo"), art.colorear(">>> ", "blanco"), end='')
            codigo = input()
            if quiere_salir(codigo):
                return 
            codigo = codigo.strip()
            if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
                        raise ValueError
            if data.revisar_codigo_existe(codigo, "grupos"):
                print(art.colorear("El codigo ingresado ya esta asignado a un grupo!\nAl continuar va a sobreescribirlo\n", "amarillo"), end='')
            print(art.colorear("Ingrese el nombre del grupo", "blanco"), art.colorear("(Debe tener entre 4 y 9 letras)", "amarillo"), art.colorear("\n>>> ", "blanco"), end='')
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
        else:   
            data.cargar_grupo(codigo, nombre, sigla)
            art.animacion_barra_progreso(art.cargando_informacion_mensaje)   
            art.animacion_cargando(art.colorear("Grupo cargado exitosamente!\nSi desea cargar otro grupo presione 1, de lo contrario volvera al menu principal.", "verde"))
            if input() == '1':
                continue
            art.animacion_cargando(art.volviendo_mensaje)
            return          

def registro_modulos():
    """Función que pide al usuario los datos requeridos para registrar un grupo."""
    while True:
        try:
            art.limpiar_pantalla()
            print(art.nuevo_modulo)
            print(art.colorear("Recuerde que si desea volver al menu principial en cualquier momento solo debe presionar la barra espaciadora\n", "rojo"))
            print(art.colorear("Para registrar un modulo debe ingresar los siguientes datos:", "blanco"))
            print(art.colorear("> Codigo numerico\n> Nombre\n> Duracion en semanas\n> Horario", "blanco"))
            print(art.colorear("Ingrese el codigo numerico", "blanco"), art.colorear("(Debe tener entre 4 y 9 digitos)", "amarillo"), art.colorear("\n>>> ", "blanco"), end='')
            codigo = input()
            if quiere_salir(codigo):
                return
            codigo = codigo.strip()
            if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
                raise ValueError
            if data.revisar_codigo_existe(codigo, "modulos"):
                print(art.colorear("El codigo ingresado ya esta asignado a un modulo!\nAl continuar va a sobreescribirlo\n>>> ", "amarillo"), end='')
            print(art.colorear("Ingrese el nombre del modulo", "blanco"), art.colorear("Debe tener entre 4 y 55 letras", "amarillo"), art.colorear("\n>>> ", "blanco"), end='')
            nombre = input()
            if quiere_salir(nombre):
                return
            nombre = nombre.strip().replace(' ', '_').upper()
            if not (not nombre.isnumeric()  and 3 <= len(nombre) <= 55):
                raise ValueError
            print(art.colorear("Ingrese la duracion del modulo en semanas", "blanco"), art.colorear("Debe tener entre 1 y 2 digitos", "amarillo"), art.colorear("\n>>> ", "blanco"), end='')
            duracion = input()
            if quiere_salir(duracion):
                return
            duracion = duracion.strip()
            if not (duracion.isnumeric() and 1 <= int(duracion) <= 99):
                raise ValueError
            print(art.colorear("\nLos modulos puede comenzar a las 06:00 y el ultimo puede empezar a las 18:00 como maximo", "amarillo"))
            print(art.colorear("Ingrese la fecha y hora de inicio del modulo", "blanco"), art.colorear("(YYYY-MM-DD HH:MM formato 24 horas)", "amarillo"), art.colorear("\n>>> ", "blanco"), end='')
            respuesta = input()
            if quiere_salir(respuesta):
                return
            fecha_hora_inicio = datetime.strptime(respuesta.strip(), "%Y-%m-%d %H:%M")
            inicio_hora = fecha_hora_inicio.time()
            if not (time(6, 0) <= inicio_hora <= time(18, 0)):
                raise ValueError
            print(art.colorear("\nLos modulos puede acabar desde las 07:00 y el ultimo puede acabar a las 23:00 como maximo", "amarillo"))
            print(art.colorear("La clase debe durar entre 1 y 5 horas", "amarillo"))
            print(art.colorear("Ingrese la hora en que acaba el modulo", "blanco"), art.colorear("(HH:MM formato 24 horas)", "amarillo"), art.colorear("\n>>> ", "blanco"), end='')
            fin_hora = input()
            if quiere_salir(fin_hora):
                return
            fin_hora = datetime.strptime(fin_hora.strip(), "%H:%M").time()
            if not (time(7, 0) <= fin_hora <= time(23, 0)):
                raise ValueError
            fin_fecha = fecha_hora_inicio + timedelta(weeks=int(duracion))
            fecha_hora_final = datetime.combine(fin_fecha.date(), fin_hora)
            if fecha_hora_final <= fecha_hora_inicio:
                raise ValueError
            hoy = datetime.today()
            tmp_inicial = datetime.combine(hoy, inicio_hora)
            tmp_final = datetime.combine(hoy, fin_hora)
            duracion_clase = tmp_final - tmp_inicial
            if timedelta(hours=1) <= duracion_clase <= timedelta(hours=8):
                horario = (str(fecha_hora_inicio), str(fecha_hora_final))
            else:
                raise ValueError
        except ValueError:
            art.animacion_cargando(art.dato_invalido_mensaje)
        else:
            data.cargar_modulo(codigo, nombre, str(duracion), horario)
            art.animacion_barra_progreso(art.cargando_informacion_mensaje)   
            art.animacion_cargando(art.colorear("Modulo cargado exitosamente!\nSi desea cargar otro presione 1, de lo contrario volvera al menu principal.", "verde"))
            if input() == '1':
                continue
            art.animacion_cargando(art.volviendo_mensaje)
            return  
  
def menu_estudiantes():
    """Ofrece al usuario las opciones de agregar un nuevo alumno, asignar o editar
    el grupo que tiene asignado, y editar sus módulos asignados.
    """
    while True:
        try:
            art.limpiar_pantalla()
            print(art.colorear("Ingrese 1 para agregar un nuevo alumno\nIngrese 2 para asignar o editar el grupo asignado a un alumno\nIngrese 3 para editar los modulos asignados a un estudiante", "blanco"), art.colorear("\nPresione la barra espaciadora para volver al menu principal\n", "rojo"), art.colorear(">>> ", "blanco"), end='')
            answer = input()
            if quiere_salir(answer):
                return
            match answer:
                case '1':
                    registro_estudiantes()
                case '2':
                    while True:
                        try:
                            art.limpiar_pantalla()
                            print(art.asignacion)
                            print(art.volver_menu_principal_espaciadora)
                            print(art.colorear("Ingrese el codigo del estudiante\n>>> ", "blanco"), end='')
                            codigo = input()
                            if quiere_salir(codigo):
                                return
                            if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
                                raise ValueError
                            print(art.colorear("Ingrese el codigo del grupo al que desea asignar al alumno\n>>> ", "blanco"), end='')
                            grupo = input()
                            if quiere_salir(grupo):
                                return
                            if not (grupo.isdigit() and 4 <= len(codigo) <= 9):
                                raise ValueError
                        except ValueError:
                            art.animacion_cargando(art.dato_invalido_mensaje)
                        else:
                            data.asignar_grupo_alumno(codigo.strip(), grupo.strip())
                            art.animacion_barra_progreso(art.cargando_informacion_mensaje)   
                            art.animacion_cargando(art.colorear("Grupo cargado exitosamente!\nSi desea cargar otro presione 1, de lo contrario volvera al menu principal.", "verde"))
                            if input() == '1':
                                continue
                            art.animacion_cargando(art.volviendo_mensaje)
                            return 
                case '3':
                    asignacion_modulos()
                case _:
                    raise ValueError
        except ValueError:
            art.animacion_cargando(art.dato_invalido_mensaje)

def registro_estudiantes():
    """Muestra las instrucciones en pantalla para registrar un alumno."""
    while True:
        try:
            art.limpiar_pantalla()
            print(art.nuevo_alumno)
            print(art.volver_menu_principal_espaciadora)
            print(art.colorear("Para registrar un alumno debe ingresar los siguientes datos:", "blanco"))
            print(art.colorear("> Codigo numerico\n> Nombre\n> Sexo\n> Edad", "blanco"))
            print(art.colorear("Ingrese el codigo numerico", "blanco"), art.colorear("\nDebe tener entre 4 y 9 digitos", "amarillo"), art.colorear("\n>>> ", "blanco"), end='')
            codigo = input()
            if quiere_salir(codigo):
                return
            if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
                raise ValueError
            if data.revisar_codigo_existe(codigo, "alumnos"):
                print(art.colorear("El codigo ingresado ya esta asignado a un alumno!\nAl continuar va a sobreescribirlo\n>>> ", "amarillo"), end='')
            print(art.colorear("Ingrese el nombre del alumno", "blanco"), art.colorear("Debe tener entre 3 y 55 letras", "amarillo"), art.colorear("\n>>> ", "blanco"), end='')
            nombre = input()
            if quiere_salir(nombre):
                return
            nombre = nombre.strip().replace(' ', '_').upper()
            if not (not nombre.isnumeric()  and 3 <= len(nombre) <= 55):
                raise ValueError
            print(art.colorear("Ingrese el sexo del alumno", "blanco"), art.colorear("Debe tener ser F o M", "amarillo"),  art.colorear("\n>>> ", "blanco"), end='')
            sexo = input()
            if quiere_salir(sexo):
                return
            sexo = sexo.strip().upper()
            if sexo not in ('M', 'F'):
                raise ValueError
            print(art.colorear("Ingrese la edad del alumno", "blanco"), art.colorear("Debe tener entre 16 y 27 años", "amarillo"),  art.colorear("\n>>> ", "blanco"), end='')
            edad = input()
            if quiere_salir(edad):
                return
            edad = edad.strip()
            if not (edad.isdigit() and 16 <= int(edad) <= 27):
                raise ValueError
        except ValueError:
            art.animacion_cargando(art.dato_invalido_mensaje)
        else:
            data.cargar_alumno(codigo.strip(), nombre, sexo, edad)
            art.animacion_barra_progreso(art.cargando_informacion_mensaje)   
            art.animacion_cargando(art.colorear("Alumno cargado exitosamente!\nSi desea cargar otro presione 1, de lo contrario volvera al menu anterior.", "verde"))
            if input() == '1':
                continue
            return

def asignacion_modulos():
    """Muestra los pasos a seguir para asignar modulos a un alumno."""
    while True:
        try:
            art.limpiar_pantalla()
            print(art.asignacion)
            print(art.salir_tecla_espaciadora_mensaje)
            print(art.colorear("Recuerde que puede asignar hasta 3 modulos por estudiante", "amarillo"))
            print(art.colorear("Ingrese el codigo del alumno\n>>> ", "blanco"), end='')
            codigo = input()
            if quiere_salir(codigo):
                return
            codigo = codigo.strip()
            if not (codigo.isdigit() and 4 <= len(codigo) <= 9):
                raise ValueError
            if data.revisa_alumno_existe(codigo):
                print(art.colorear("Para registrar alumno en un modulo ingrese 1\nPara eliminar modulos asociados con un alumno escriba 2\n>>> ", "blanco"), end='')
                answer = input()
                if quiere_salir(answer):
                    return
                if answer == '1':
                    while True:
                        modulos_actuales = data.revisa_alumno_cuantos_modulos(codigo)
                        if len(modulos_actuales) == 3:
                            art.animacion_cargando(art.colorear("El alumno ha alcanzado el limite de modulos a los que puede estar matriculado!", "rojo"))
                            art.animacion_cargando("Saliendo...")
                            return
                        print(art.colorear("Para dejar de asignar modulos presione la barra espaciadora!", "rojo"))                   
                        if len(data.revisa_alumno_cuantos_modulos(codigo)) >= 3:
                            art.animacion_cargando(art.colorear("El alumno ha alcanzado el limite de modulos a los que puede estar matriculado!", "rojo"))
                            print(art.colorear("Intentelo nuevamente", "amarillo"))
                            print("Presione cualquier tecla para salir")
                            input()
                            return
                        else:
                            print(f"El alumno esta inscrito en los siguientes modulos: ", '-'.join(modulos_actuales))
                            print(art.colorear("Ingrese el codigo del modulo en el que desea matricular al alumno\n>>> ", "blanco"), end='')
                            modulo = input()
                            if quiere_salir(modulo):
                                return
                            data.asignar_modulo(codigo.strip(), modulo.strip())
                            art.animacion_barra_progreso(art.colorear("Asignando modulo...Un momento.", "verde"))

                elif answer == '2':
                    while True:
                        try:
                            art.limpiar_pantalla()
                            print(art.borrar_modulo)
                            modulos_actuales = data.revisa_alumno_cuantos_modulos(codigo)
                            print(art.salir_tecla_espaciadora_mensaje)
                            print(f"El alumno esta inscrito en los siguientes modulos: ", '-'.join(modulos_actuales))
                            print(art.colorear("Ingrese el codigo del modulo que desea eliminar\n>>> ", "blanco"), end='')
                            modulo = input()
                            if quiere_salir(modulo):
                                return
                            data.eliminar_modulo(codigo.strip(), modulo.strip())
                            art.animacion_barra_progreso(art.colorear("Borrando modulo...Un momento.", "verde"))
                        except ValueError:
                            print(art.colorear("Intentelo nuevamente", "blanco"))
                            art.animacion_cargando(art.dato_invalido_mensaje)
                else:
                    raise ValueError
            else:
                art.animacion_cargando(art.colorear("El codigo de estudiante no existe! Intentelo de nuevo", "rojo"))
        except ValueError:
            print(art.colorear("Intentelo nuevamente", "blanco"))
            art.animacion_cargando(art.dato_invalido_mensaje)

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

def cambio_clave():
    """Función que pide al usuario los datos requeridos para cambiar la clave."""
    while True:
        try:
            art.limpiar_pantalla()
            print(art.cambio_de_clave)
            print(art.salir_tecla_espaciadora_mensaje)
            print(art.colorear("Ingrese su usuario\n>>> ", "blanco"), end='')
            usuario = input()
            if quiere_salir(usuario):
                break
            print(art.colorear("Ingrese la clave actual\n>>> ", "blanco"), end='')
            clave = art.ingresar_clave()
            if quiere_salir(clave):
                break
            art.animacion_barra_progreso(art.validando_mensaje)
            if data.validacion_usuario_clave(usuario, clave):
                print(art.validacion_exito_mensaje)
                print(art.colorear("La clave solo puede tener caracteres alfanumericos y debe ser de al menos 4 caracteres", "amarillo"))
                print(art.colorear("\nIngrese la nueva clave\n>>> ", "blanco"), end='')
                nueva_clave = art.ingresar_clave()
                if quiere_salir(nueva_clave):
                    break
                print(art.colorear("\nIngrese la nueva clave otra vez\n>>> ", "blanco"), end='')
                nueva_clave2 = art.ingresar_clave()                           
                if quiere_salir(nueva_clave2):
                    break
                if not (nueva_clave.isalnum() and nueva_clave2.isalnum() and len(nueva_clave) >= 4 and len(nueva_clave2) >= 4):
                    print(art.colorear("Ha ingresado una clave invalida! Intente nuevamente", "rojo"))
                if nueva_clave != nueva_clave2:
                    art.animacion_cargando(art.colorear("Las claves no coinciden!\nIntentelo nuevamente...", "rojo"))
                    continue
                data.cambiar_clave(usuario, nueva_clave)
                art.animacion_cargando(art.colorear("Se ha cambiado la clave exitosamente!\nVolviendo al menú!", "verde"))
                break
            else:
                art.animacion_cargando(art.colorear("Ha ingresado un usuario y/o clave incorrecto!\nIntentelo nuevamente!", "rojo"))
        except ValueError:
            art.animacion_cargando(art.dato_invalido_mensaje)