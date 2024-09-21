import sys, tty, termios

def limpiar_pantalla():
    print('\033c')
    return 0

SISGESA_base = """
++----------------------------------------------------------------------------------++
++----------------------------------------------------------------------------------++
||                                                                                  ||
||   █████████  █████  █████████    █████████  ██████████  █████████    █████████   ||
||  ███░░░░░███░░███  ███░░░░░███  ███░░░░░███░░███░░░░░█ ███░░░░░███  ███░░░░░███  ||
|| ░███    ░░░  ░███ ░███    ░░░  ███     ░░░  ░███  █ ░ ░███    ░░░  ░███    ░███  ||
|| ░░█████████  ░███ ░░█████████ ░███          ░██████   ░░█████████  ░███████████  ||
||  ░░░░░░░░███ ░███  ░░░░░░░░███░███    █████ ░███░░█    ░░░░░░░░███ ░███░░░░░███  ||
||  ███    ░███ ░███  ███    ░███░░███  ░░███  ░███ ░   █ ███    ░███ ░███    ░███  ||
|| ░░█████████  █████░░█████████  ░░█████████  ██████████░░█████████  █████   █████ ||
||  ░░░░░░░░░  ░░░░░  ░░░░░░░░░    ░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░  ░░░░░   ░░░░░  ||
||                                                                                  ||
++----------------------------------------------------------------------------------++
++----------------------------------------------------------------------------------++
"""

def center_text(text, width):
    lines = text.splitlines()  # Split the text into lines
    centered_lines = [line.center(width) for line in lines]  # Center each line
    return "\n".join(centered_lines)  # Join the centered lines back together

# Adjust the width based on your terminal or preferred width
terminal_width = 155
SISGESA = center_text(SISGESA_base, terminal_width)

# Bold text
bold = "\033[1m"
reset = "\033[0m"

# Colors
white = "\033[37m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"

type_user_message = f'{bold}{white}Ingrese su usuario{reset}' + '\n' + f'{bold}{white}>>> {reset}'
type_password_message = f'{bold}{white}Ingrese su contraseña{reset}' + '\n' + f'{bold}{white}>>> {reset}'

def getch():
    """Get a single character from standard input without echoing."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def input_password(prompt=f"{white}{bold}Ingrese su contraseña\n>>> {reset}"):
    print(prompt, end='', flush=True)
    password = ""
    
    while True:
        char = getch()
        if char in ('\n', '\r'):  # Enter key
            print()  # Newline
            break
        elif char == '\x7f':  # Backspace key
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)  # Remove last asterisk
        else:
            password += char
            print('*', end='', flush=True)  # Display an asterisk for each character

    return password