import time, os, random, getpass

from day01.solve import *

term_delay = 0.5

header = '''
WELCOME TO THE CONTROL CENTER
PREPARING SUITABLE ENVIRONMENT
INITILIAZING ELVES
BOOTING......
CONSOLE READY

'''

help = '''
HELP - DISPLAY HELP MENU
SOLVE - SOLVE PROBLEM OF THE DAY
    EX: SOLVE DAY01
CLEAR - CLEAR CONSOLE

'''

days = {
    'day01': [day01_01(), day01_02()]
}

def printer(menu):
    counter = random.randint(0, 1)
    if type(menu) == str:
        for i in menu:
            if counter % 2:
                print(i.upper(), end = '')
            else:
                print(i.lower(), end = '')
            if i == '\n':
                time.sleep(term_delay)
            counter += 1
    else:
        for i in range(len(menu)):
            printer('SOLUTION ' + str(i + 1) + ' IS ' + str(menu[i]) + '\n')



def init():
    os.system('cls' if os.name=='nt' else 'clear')
    printer(header)

def help_menu():
    printer(help)

def solve_day(s):
    time.sleep(term_delay)
    printer(days[s])
    print('\r')

def command_and_control():
    printer('AWAITING USER INPUT\n\n')
    s = input('')
    time.sleep(term_delay)
    match s.lower().split(' ')[0]:
        case "help":
            help_menu()
        case "solve":
            try:
                solve_day(s.lower().split(' ')[1])
            except:
                printer('''\nYOU FUCKED IT UP >:(
                    \rYOU TYPED: ''' + s + '''
                    \rTHIS IS NOT A VALID DAY
                ''')
                help_menu()
        case "clear":
            printer('\nPREPARING TO CLEAR\n\n')
            time.sleep(term_delay * 3)
            printer('CLEARING\n\r')
            time.sleep(term_delay)
            os.system('cls' if os.name=='nt' else 'clear')
            time.sleep(0.5)
        case _:
            printer('''\nYOU FUCKED IT UP >:(
                \rYOU TYPED: ''' + s + '''
                \rTHIS IS UNACCEPTABLE
            ''')
            help_menu()


init()
while True:
    command_and_control()