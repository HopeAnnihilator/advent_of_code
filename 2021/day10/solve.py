import json
def day10():
    f = [i.strip('\n') for i in open('day10/input')]
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    for line in f:
        print(json.loads(line))

    

print(day10())