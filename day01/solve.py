def day01():
    f = [int(i) for i in open('day01/input', 'r').readlines()]
    return solve(f, 1), solve (f, 3)

def solve(f, n):
    return [f[i] > f[i -n] for i in range(1, len(f))].count(True)
