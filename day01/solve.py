def day01_01(f):
    return [f[i] > f[i - 1] for i in range(1, len(f))].count(True)

def day01_02(f):
    return [f[i] > f[i -3] for i in range(1, len(f))].count(True)