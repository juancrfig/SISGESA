import json

modulo = "0003"
principal = './app_data/data.json'

def consultar_alumnos_en_modulo(modulo):
    """Consulta los alumnos registrados en un modulo elegido.
    
    Args:
        modulo (str): El codigo del modulo que se desea consultar.

    Returns:
        alumnos (list): La lista con los codigos de los alumnos
        registrados en el módulo elegido.
    """
    alumnos = []
    with open(principal) as file:
        data = json.load(file)
    for codigo in data["alumnos"].keys():
        modulos_alumno = data["alumnos"][codigo].get("modulos")
        if modulo in modulos_alumno:
            alumnos.append(codigo)
    return alumnos
        
consultar_alumnos_en_modulo(modulo)