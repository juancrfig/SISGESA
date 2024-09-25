import json

principal = './app_data/data.json'
asistencia = './app_data/asistencia.json'

modulo = "0001"
dia = "2024-01-15"


def porcentaje_asistencias(modulo, dia):

    # Calcula la cantidad de alumnos matriculados al modulo ingresado
    with open(principal) as file:
        data = json.load(file)  
    alumnos = 0
    for codigo in data["alumnos"].keys():
        for m in data["alumnos"][codigo]["modulos"]:
            if m == modulo:
                alumnos += 1
    
    # Calcula la cantidad de estudiantes que asistieron en el dia solicitado
    with open(asistencia) as file:
        data = json.load(file)
    asistencias_dia =len(data[modulo][dia].keys())

    porcentaje_asistencia = (asistencias_dia / alumnos) * 100
    return porcentaje_asistencia

print(porcentaje_asistencias(modulo, dia))