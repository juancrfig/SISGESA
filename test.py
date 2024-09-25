import json
from packages import data

principal = './app_data/data.json'
asistencia = './app_data/asistencia.json'

modulo = "0001"
dia = "2024-01-15"


def alumnos_asistencia_perfecta(alumno, modulo):

    with open(asistencia) as file:
        data = json.load(file)

    for dia in data[modulo].keys():
        if alumno not in data[modulo][dia].keys():
            return False
    return True 

if data.revisar_codigo_existe(modulo, "modulos"):
    if alumnos_asistencia_perfecta("0001", modulo):
        print("Asistencia perfecta!")
    else:
        print("Asistencia no perfecta!")
else:
    print("El modulo no existe")
    
    