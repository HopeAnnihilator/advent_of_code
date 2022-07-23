#!/usr/bin/python3

import math

output = []
total = 0

#read input from files
with open('input') as f:
    data = f.read().splitlines()

def mainfunc(thing, code):
    # equation to run
    item = thing / 3
    item = math.trunc(item)
    item = int(item)
    item = item - 2
    if code == 2 and item > 0:
        #change the script to follow rules of puzzle 2
        mainfunc(thing = item, code = code)
        output.append(item)
    elif code == 1:
        output.append(item)

#run through 2 puzzles
for x in range(1,3):
    global item
    #read each unit from list to run
    for item in data:
        item = int(item)
        mainfunc(thing = item, code = x)
    #add output for total number
    for value in output:
        total = int(total) + int(value)
    print("puzzle" + str(x) + ": " + str(total))
    total = 0
    output = []