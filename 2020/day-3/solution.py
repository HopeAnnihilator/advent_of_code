#!/usr/bin/env python3

import json
import time
import numpy

data = {}
with open("day-3/data") as f:
    scanInput = f.read()
data["input"] = scanInput.split('\n\n')
data["total"] = 0
data["required"] = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid"
]

for i in data["input"]:
    tmplist = list(data["required"])
    i = i.replace('\n', ' ')
    i = i.split(' ')
    for x in i:
        tmplist.pop(tmplist.index(x.split(':')[0]))
    if not tmplist:
        print(tmplist)
        data["total"] += 1

print(data)