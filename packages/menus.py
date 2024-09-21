from packages import art

def login():
    art.limpiar_pantalla()
    print(art.SISGESA, '\n')
    user = input(art.type_user_message)
    password = art.input_password()