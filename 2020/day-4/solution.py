#!/usr/bin/env python3

import json
import time
import numpy


data = {}

with open("day-3/data") as f:
    data["gps"] = f.read().splitlines() 

data["slopes"] = [
    [1,1],
    [3, 1],
    [5,1],
    [7,1],
    [1,2]
]

data["totalHits"] = []

for slope in data["slopes"]:
    data["treesHit"] = 0
    data["position"] = [0, 0]
    while abs(data["position"][1]) < len(data["gps"]):
        line = data["gps"][data["position"][1]]
        if line[data["position"][0]] == "#":
            data["treesHit"] += 1
        data["position"][1] += slope[1]
        data["position"][0] += slope[0]
        if data["position"][0] >= len(data["gps"][0]):
            data["position"][0] -= len(data["gps"][0])
    data["totalHits"].append(data["treesHit"])


print(json.dumps(data, indent = 2))
print(numpy.prod(data["totalHits"]))