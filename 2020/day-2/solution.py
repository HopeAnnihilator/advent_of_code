#!/usr/bin/env python3

with open("day-2/data") as f:
    database = f.read().splitlines() 

total = 0
total2 = 0
for i in database:
    i = i.split(' ')
    letterCount = i[0].split('-')
    MAX = int(letterCount[1])
    MIN = int(letterCount[0])
    letter = i[1][0]
    password = i[2]
    valid = password.count(letter)
    if valid >= MIN and valid <= MAX:
        total += 1
    if (password[MIN - 1] == letter or password[MAX - 1] == letter) and (password[MIN - 1] != password[MAX - 1]):
        total2 += 1
print(total)
print(total2)
    
