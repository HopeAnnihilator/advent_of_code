def day06():
    fish = [int(i) for i in open('day06/input').read().strip('\n').split(',')]
    fishies = [fish.count(0), fish.count(1), fish.count(2), fish.count(3), fish.count(4), fish.count(5), fish.count(6), fish.count(7), fish.count(8)]
    return iterate(80, fishies), iterate(256, fishies)

def iterate(years, fishies):
    for _ in range(years):
        tmp = [
            fishies[1],
            fishies[2],
            fishies[3], 
            fishies[4],
            fishies[5],
            fishies[6],
            fishies[7] + fishies[0],
            fishies[8],
            fishies[0]
        ]
        fishies = tmp
    return sum(fishies)
