import time, os

from day01.solve import *

header = '''
WELCOME TO THE CONTROL CENTER
PREPARING SUITABLE ENVIRONMENT
INITILIAZING ELVES
BOOTING......
CONSOLE READY'''

help = '''
HELP - DISPLAY HELP MENU
SOLVE - SOLVE PROBLEM OF THE DAY
    EX: SOLVE DAY01
'''

days = {
    'day01': [day01_01(), day01_02()]
}

def printer(menu):
    if type(menu) == str:
        for line in menu.split('\n'):
            print(line)
            time.sleep(0.5)
    else:
        for i in range(len(menu)):
            print('SOLUTION ' + str(i + 1) + ' IS ' + str(menu[i]))
            time.sleep(0.5)


def init():
    os.system('cls' if os.name=='nt' else 'clear')
    printer(header)

def help_menu():
    printer(help)

def solve_day(s):
    printer(days[s])
    print('\r')

def command_and_control():
    print('AWAITING USER INPUT\n')
    time.sleep(0.5)
    s = input("")
    match s.lower().split(' ')[0]:
        case "help":
            help_menu()
        case "solve":
            try:
                solve_day(s.lower().split(' ')[1])
            except:
                printer('\nYOU FUCKED IT UP >:(')
                printer('YOU TYPED: ' + s)
                printer('THIS IS NOT A VALID DAY')
                help_menu()
        case _:
            printer('\nYOU FUCKED IT UP >:(')
            printer('YOU TYPED: ' + s)
            printer('THIS IS UNACCEPTABLE')
            help_menu()


init()
while True:
    command_and_control()