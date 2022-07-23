#!/usr/bin/env python3

import re

location = {'x':0, 'y':0}
paths = {}
positions = []
i = 1
currentpath = 1

#reading input and for each newline creating a new path
with open("input", 'r') as f:
    path = f.readlines()
    for item in path:
        item = re.sub("\\n", "", item)
        paths[i] = item
        i = i + 1

#find the total number of paths
totalpaths = len(paths.keys())

#save each step taken by wire
def writepos():
    positions.append(str(location['x']) + ':' + str(location['y']))

#run instruction set
while currentpath <= totalpaths:
    trail = paths[currentpath].split(',')
    for direction in trail:
        if direction.startswith('R'):
            for value in range(0,int(direction[1:])):
                location['x'] = int(location['x']) + 1
                writepos()
        if direction.startswith('L'):
            for value in range(0,int(direction[1:])):
                location['x'] = int(location['x']) - 1
                writepos()
        if direction.startswith('U'):
            for value in range(0,int(direction[1:])):
                location['y'] = int(location['y']) + 1
                writepos()
        if direction.startswith('D'):
            for value in range(0,int(direction[1:])):
                location['y'] = int(location['y']) - 1
                writepos()
    location = {'x':0, 'y':0}
    paths[currentpath + totalpaths] = positions
    positions = []
    currentpath = currentpath + 1

lowest_intersect = 0
steps = []
first_intersect = 0

#find intersects 
intersections = set(paths[totalpaths + 1]).intersection(paths[totalpaths + 2])

#find movements 
for position in intersections:
    steps.append(str(paths[3].index(position) + 1) + ':' + str(paths[4].index(position) + 1))

#find intersection closest to 0,0
for points in intersections:
    points = points.split(':')
    total = abs(int(points[0])) + abs(int(points[1]))
    if total < lowest_intersect or lowest_intersect == 0:
        lowest_intersect = total

#find the position with the least steps total steps from both paths
for item in steps:
    z = item.split(':')
    total_steps = int(z[0]) + int(z[1])
    if total_steps < first_intersect or first_intersect == 0:
        first_intersect = total_steps

print("Closest Intersect: " + str(lowest_intersect))
print("Fewest-steps Intersect: " + str(first_intersect))