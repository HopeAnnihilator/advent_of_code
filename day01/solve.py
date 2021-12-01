def day01_01():
    total = 0

    # read input
    f = open('day01/input', 'r')

    depths = [int(f.readline())]

    # solve shits
    for line in zip(f):
        depths.append(int(line[0]))
        if depths[0] < depths[1]:
            total += 1
        depths.pop(0)
    return total

def day01_02():
    depths = []
    total = 0

    # read input
    f = open('day01/input', 'r')

    # setup 
    for i in range(3):
        depths.append(int(f.readline()))

    # solve shit
    for line in zip(f):
        depths.append(int(line[0]))
        prevWindow = depths[1] + depths[2]
        currWindow = depths[3] + prevWindow
        prevWindow += depths[0]
        if currWindow > prevWindow:
            total += 1
        depths.pop(0)

    return total
