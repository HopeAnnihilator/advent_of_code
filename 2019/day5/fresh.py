#!/usr/bin/env python3 

import time, sys

printint = None
noun = None
verb = None
inputint = input("Input given integer or noun,verb (item 1 and 2): ")

if ',' in inputint:
    inputint = inputint.split(',')
    noun = int(inputint[0])
    verb = int(inputint[1])

jumps4 = (1,2,7,8)
jumps2 = (3,4)
jankyjumps = (5,6)

with open('input') as f:
    inputdata = f.read()
    inputdata = inputdata.replace('\n', '')
    cleaninput = inputdata.split(',')
    f.close()

def resetdata():
    global data
    data = []
    for item in cleaninput:
        data.append(item)

def mainfunc():
    cord = 0
    while True:
        global opcode, printint
        opcode = data[cord]
        instset = str(opcode)
        if len(instset) < 4:
            instset = (str(0) * (4 - len(instset))  + instset)
        opcode = int(instset[-2:])
        if opcode == 99:
            break
        else:
            if int(instset[:4]) == 0:
                if opcode in (1,2):
                    int1 = int(data[int(data[cord + 1])])
                    int2 = int(data[int(data[cord + 2])])
            else:
                integers = []
                if opcode not in jumps2:
                    j = 2
                    for i in instset[:-2]:
                        currentval = int(data[cord + j])
                        if int(i) == 0:
                            integers.append(int(data[currentval]))
                        else:
                            integers.append(currentval)
                        j = j - 1
                    int1 = integers [1]
                    int2 = integers[0]

            if opcode in jumps4:
                saveint = int(data[cord + 3])
                if opcode == 1:
                    data[saveint] = int1 + int2
                elif opcode == 2:
                    data[saveint] = int1 * int2
                elif (opcode == 7 and int1 < int2) or (opcode == 8 and int1 == int2):
                    data[saveint] = 1
                else: 
                    data[saveint] = 0
                cord = cord + 4
            elif opcode in jumps2:
                saveint = int(data[cord + 1])
                if opcode == 3:
                    data[saveint] = inputint
                elif opcode == 4:
                    printint = data[saveint]
                cord = cord + 2
            elif opcode in jankyjumps:
                if (opcode == 5 and int1 != 0) or (opcode == 6 and int1 == 0):
                    cord = int2
                else:
                    cord = cord + 3
            else:
                print('Please input a valid number')
                exit()



try:
    result = sys.argv[1]
    for noun in range(0,100):
        for verb in range(0,100):
            resetdata()
            data[1] = noun
            data[2] = verb
            mainfunc()
            if int(data[0]) == int(result):
                print(noun * 100 + verb)
                exit()
    else:
        print('Combination not found')
except IndexError:
    resetdata()
    if noun:
        data[1] = noun
        data[2] = verb
    mainfunc()
    if printint:
        print(printint)
    else:
        print(data[0])