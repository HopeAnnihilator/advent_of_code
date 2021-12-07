def day06():
    f = [int(x) for x in open('day07/input').read().split(',')]
    f.sort()
    median = int(len(f) / 2)
    costs1 = [sum([
        sum([
            abs(i - f[median + variation])
        ]) for i in f]) 
        for variation in range(-1, 2)]

    mean = int(sum(f) / len(f))
    costs2 = [sum([
        sum(range(abs(i - mean + variation) + 1))
        for i in f])
        for variation in range(-1, 2)]

    return min(costs1), min(costs2)