#!/usr/bin/env python3

with open("day-1/data") as f:
    expenses = f.readlines()

founditems = []
def accounting(i):
    for j in expenses:
        j = int(j.strip('\n'))
        for x in expenses:
            x = int(x.strip('\n'))
            if i + j + x == 2020 and i * j * x not in founditems:
                print("3-sum: " + str(i * j * x))
                founditems.append(i * j * x)
        if i + j == 2020 and i * j not in founditems:
            print("2-sum: " + str(i * j))
            founditems.append(i * j)
        
for i in expenses:
    i = int(i.strip('\n'))
    accounting(i = i)
    
