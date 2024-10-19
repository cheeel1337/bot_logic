import random

def gen_pass(pass_lenght):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_lenght):
        password += random.choice(elements)
    return password

def flip():
    emblem = ''
    flip = random.randint(1, 5)
    if flip == 1 or flip == 2:
        emblem = 'орёл'
    elif flip == 3 or flip == 4:
        emblem = 'решка'
    else:
        emblem = 'монетка приземлилась ребром'
    return emblem

def helpful():
    supported_commands = '/hello, /bye, /pass, /heh, /coin'
    return supported_commands
