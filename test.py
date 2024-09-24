import json

grupo = "0001"
principal = './app_data/data.json'

def consultar_alumnos_en_grupo(grupo):
    """Consulta qué alumnos están en un grupo.
    
    Args:
        grupo (str): El código del grupo.
    
    Returns:
        alumnos (lista): Una lista que contiene los codigos de todos
        los estudiantes que pertenecen al grupo ingresado.
    """
    alumnos = []
    with open(principal) as file:
        data = json.load(file)
    for codigo in data["alumnos"].keys():
        if data["alumnos"][codigo].get("grupo") == grupo:
            alumnos.append(codigo)
    return alumnos



consultar_alumnos_en_grupo(grupo)