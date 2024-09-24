import json
from packages import data

cedula = "6852294"
modulo = "0009"
principal = './app_data/data.json'

def consultar_estudiantes_a_cargo_docente_en_modulo(cedula, modulo):
    """Consulta los estudiantes de los que está a cargo un docente
    en un módulo ingresado.
    
    Args:
        cedula (str): La cédula del docente.
        modulo (str): El código del módulo.

    Returns:
        alumnos (list): Una lista que contiene los alumnos que están
        asignados en el módulo ingresado y reciben clases del docente ingresado.
    """
    alumnos = []
    with open(principal) as file:
        info = json.load(file)
    if modulo in info["docentes"][cedula]["modulos"]:
        print(f"El docente {info['docentes'][cedula]['nombre']} imparte el modulo {modulo}.")
        print(f"Los estudiantes que tiene a cargo son:")
        alumnos = data.consultar_alumnos_en_modulo(modulo)
        print(', '.join(alumnos))
        print("\n\nPresione cualquier tecla para volver")
        input()
    else:
        print(f"El docente {info['docentes'][cedula]['nombre']} no imparte el modulo {modulo}")

consultar_estudiantes_a_cargo_docente_en_modulo(cedula, modulo)