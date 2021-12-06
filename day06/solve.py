def day06():
    fish = [int(i) for i in open('day06/input').read().strip('\n').split(',')]
    fishies = [fish.count(0), fish.count(1), fish.count(2), fish.count(3), fish.count(4), fish.count(5), fish.count(6), fish.count(7), fish.count(8)]
    return tuple(i for i in iterate((80, 256), fishies))

def iterate(years, fishies):
    for year in range(1, max(years) + 1):
        fishies.append(fishies[0])
        fishies[7] += fishies[0]
        fishies.pop(0)
        if year in years:
            yield sum(fishies)