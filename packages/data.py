def first_time():
    with open('password.json', 'a+') as pass_file:
        lines = pass_file.readlines()
        if lines:
            return False
        else:
            return True
        
