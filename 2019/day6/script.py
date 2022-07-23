#!/usr/bin/env python3

import time, json

orbits = {}
primary = 'COM'
orbitvalues = {}
movefrom = 'YOU'
moveto = 'SAN'

with open('day6/input') as f:
    inputdata = f.readlines()
    f.close()

for line in inputdata:
    line = line.strip('\n')
    line = line.split(')')
    orbitee = line[0]
    orbiter = line[1]
    orbitlist = []
    orbitlist.append(orbitee)
    if orbiter == movefrom or orbiter == moveto:
        orbitlist.append(({"value" + orbiter : 0, 'path' + orbiter : []}))
    else:
        orbitlist.append({"value" + orbiter : 0})
    orbits[orbiter] = orbitlist

        

def evalfromprimary():
    for item in orbits:
        path = []
        path.append(item)
        thing = orbits[item][0]
        while thing != primary:
            path.append(thing)
            thing = orbits[thing][0]
        orbits[item][1]['value' + item] = len(path)
        if item in (moveto, movefrom):
            orbits[item][1]['path' + item] = path

evalfromprimary()

total = 0
for item in orbits:
    total = total + orbits[item][1]['value' + item]
print('Total orbits: ' + str(total))


intersections = set(orbits[moveto][1]['path' + moveto]).intersection(orbits[movefrom][1]['path' + movefrom])
lowestval = 1 * 10 ** 100
for item in intersections:
    itemval = orbits[item][1]['value' + item]
    movefromval = orbits[movefrom][1]['value' + movefrom] - itemval
    movetoval = orbits[moveto][1]['value' + moveto] - itemval
    if (movefromval + movetoval - 2) <= lowestval:
        lowestval = movefromval + movetoval - 2

print('Movement from ' + movefrom + ' to ' + moveto + ': ' + str(lowestval))

