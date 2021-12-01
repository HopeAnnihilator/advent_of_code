def day01_01():
    total = 0
    f = [int(i) for i in open('day01/input', 'r').readlines()]
    for i in range(1, len(f)):
        if (f[i] > f[i - 1]):
            total += 1
    return total

def day01_02():
    total = 0
    f = [int(i) for i in open('day01/input', 'r').readlines()]
    for i in range(3, len(f)):
        prevWindow = f[i - 1] + f[i - 2]
        currWindow = f[i] + prevWindow
        prevWindow += f[i - 3]
        if (currWindow > prevWindow):
            total += 1
    return total