#!/usr/bin/env python3

#range of numbers for input
datarange = "147981-691423"
#split the range for min/max
datarange = datarange.split('-')
minnum = int(datarange[0])
maxnum = int(datarange[1])
total1 = 0
total2 = 0
#check each value in range of possible numbers
for number in range(minnum,maxnum + 1):
    previtem = 0
    success = 0
    i = 0
    digits = []
    #evaluate each digit of each number
    for item in str(number):
        #if the current digit less than previous digit go next
        if int(item) < previtem:
            break
        else:
            previtem = int(item)
            success = success + 1
        #if all 6 digits are great than or equal to the previous digit continue
        if success == 6:
            for digit in str(number):
                #find if previous digit matches current digit
                if i == int(digit):
                    total1 = total1 + 1
                    #if there is at least 1 pair of digits, check the number to ensure there is one group of 2 for puzzle #2
                    for digit in str(number):
                        digits.append(str(number).count(str(digit)))
                    #if there is 1 pair add to total2
                    if 2 in digits:
                        total2 = total2 + 1
                    break
                else:
                    i = int(digit)
print("puzzle1: " + str(total1))
print("puzzle2: " + str(total2))
