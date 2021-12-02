def day01():
    # read file into array
    f = [int(i) for i in open('day01/input')]
    # solve and return tuple
    return solve(f, 1), solve (f, 3)

def solve(f, n):
    # solve for location i and i - n
    return [f[i] > f[i -n] for i in range(1, len(f))].count(True)
