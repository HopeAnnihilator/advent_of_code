fish = [int(i) for i in open('day06/input').read().strip('\n').split(',')]
for n in range(1, 100):
    for i in range(len(fish)):
        fish[i] -= 1
        if fish[i] < 0:
            fish[i] = 6
            fish.append(8)

    # if n % 7 == 0:
    #     print(str(n))
    #     print(len(fish))
        #print(fish)
    print([fish.count(0), [fish.count(1), fish.count(2)], [fish.count(3), fish.count(4)], [fish.count(5), fish.count(6)], [fish.count(7), fish.count(8)]])
    print()
print(len(fish))
