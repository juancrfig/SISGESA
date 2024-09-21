import json

def check_first_time():
    with open('password.json', 'a+') as pass_file:
        pass_file.seek(0)
        lines = pass_file.readlines()
        if lines:
            return False
        else:
            return True

def register_new_user(info):
    with open('password.json', 'w+' ) as file:
        json.dump(info, file)
        
