def day01_01():
    f = [int(i) for i in open('day01/input', 'r').readlines()]
    return [f[i] > f[i - 1] for i in range(1, len(f))].count(True)

def day01_02():
    f = [int(i) for i in open('day01/input', 'r').readlines()]
    return [f[i] + f[i - 1] + f[i - 2] > f[i - 1] + f[i - 2] + f[i -3] for i in range(1, len(f))].count(True)