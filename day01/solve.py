def day01_01():
    # empty array
    depths = []

    # read input
    with open ('day01/input') as f:
        data = f.readlines()

    # parse data
    for i in data:
        depths.append(int(i.strip('\n')))

    # find totals for node increases
    total = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            total += 1
    return total

def day01_02():
    # empty array
    depths = []

    # read input
    with open ('day01/input') as f:
        data = f.readlines()

    # parse data
    for i in data:
        depths.append(int(i.strip('\n')))
    # find total for window increases
    total = 0
    for i in range(3, len(depths)):
        prevWindow = depths[i - 1] + depths [i - 2]
        currWindow = depths[i] + prevWindow
        prevWindow += depths[i - 3]
        if currWindow > prevWindow:
            total += 1
    return total