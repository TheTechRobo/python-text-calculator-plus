from cprint import cprint
from sys import exit
def ex1():
    cprint.fatal('''File "ex.py", line 10
SyntaxError: not a chance''')
    sys.exit()
def rex():
    print()
    try:
        exNum = int(input("Number to be exponented? "))
        pwrNum = int(input("To the power of what? "))
    except ValueError:
        cprint.error("ERR CODE 3: You did not type a number! Or you typed a number with a dec point!")
    if pwrNum == 2:
        cprint.info("PLEASE NOTE: this is the same as typing in [] or sq")
    elif pwrNum == 3:
        cprint.info("PLEASE NOTE that this is the same as typing {} or cu")
    elif pwrNum == 1:
        ex1()
    print()
    result = '=', exNum ** pwrNum
    cprint.ok(result)