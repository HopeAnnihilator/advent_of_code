#!/usr/bin/python3

import time, sys

opCode = 0
iAmAt = 0

#read from input file
with open('input') as f:
    inputdata = f.read()
    inputdata = inputdata.replace('\n', '')
    inputdata = inputdata.split(',')

#add noun and verb as well as stop point for part 2
try:
    nounmax = abs(int(sys.argv[1]))
    verbmax = abs(int(sys.argv[2]))
    try:
        #value to stop on
        stoppoint = int(sys.argv[3])
    except TypeError:
        print('integers you ape')
    except:
        stoppoint = None
except:
    #if no noun/verb kill program
    print('give info on noun/verb and stop point if needed \nnoun is item 1 on list and verb is item 2\nif no stop point is present program will only execute the noun/verb\nif stop point is present program\nwill execute every value from 0 to noun/verb')
    exit()

#remake list with updated info as instructed
def voomList(whereTo):
    global iAmAt, data
    data = []
    iAmAt = 0
    for item in current:
        if int(iAmAt) == int(whereTo):
            data.append(output)
        elif int(iAmAt) != int(whereTo):
            data.append(item)
        iAmAt = iAmAt + 1


#run the opcode
def mainfunc():
    while True:
        try:
            global opCode, current, output, noun, verb
            current = data
            code = int(data[opCode])
            if code == 1:
                valueOne = int(data[opCode + 1])
                valueTwo =  int(data[opCode + 2])
                output = int(data[valueOne]) + int(data[valueTwo])
                whereTo = int(data[opCode + 3])
                voomList(whereTo = whereTo)
                current = data
            elif code == 2:
                valueOne = int(data[opCode + 1])
                valueTwo =  int(data[opCode + 2])
                output = int(data[valueOne]) * int(data[valueTwo])
                whereTo = int(data[opCode + 3])
                voomList(whereTo = whereTo)
                current = data
            elif code == 99:
                if not stoppoint:
                    print("answer: " + str(data[0]))
                elif int(stoppoint) == int(data[0]):
                    print("answer: " + str(noun * 100 + verb))
                    exit()
                break
            else:
                print('you fucked up')
            opCode = opCode + 4
        except IndexError:
            print('error')
            break


#if stop point check all ranges up to noun/verb
if stoppoint:
    for noun in range(0,int(nounmax) + 1):
        for verb in range(0,int(verbmax) + 1):
            opCode = 0
            data = []
            data.append(1)
            data.append(int(noun))
            data.append(int(verb))
            for item in inputdata[3:]:
                data.append(item)
            mainfunc()
#if not stop point run with 1 noun/verb
else:
    data = []
    data.append(1)
    data.append(int(nounmax))
    data.append(int(verbmax))
    for item in inputdata[3:]:
        data.append(item)
    mainfunc()



