def day06():
    iterations = 80
    fish = [int(i) for i in open('day06/input').read().strip('\n').split(',')]
    sub = 0


    next = []
    for n in range(7, iterations, 7):
        r = len(fish)
        for i in range(r):

            if fish[i] == 7 or fish[i] == 8:
                sub += 1

        # print("Curr Length: " + str(len(fish)))
        # print("Prediction: " + str(prevlen * 2 - sub))
        # print("Subtractions: " + str(sub))
        # print("Future Subtractions: " + str(fish.count(5) + fish.count(6)))

        print(next)
        print([fish.count(0), [fish.count(1), fish.count(2)], [fish.count(3), fish.count(4)], [fish.count(5), fish.count(6)], [fish.count(7), fish.count(8)]])
        next = ([
        fish.count(0) + fish.count(7),
        [fish.count(1) + fish.count(8), fish.count(2) + fish.count(0)], 
        [fish.count(3) + fish.count(1), fish.count(4) + fish.count(2)], 
        [fish.count(5) + fish.count(3), fish.count(6) + fish.count(4)],
        [fish.count(5), fish.count(6)]])
        print()

        for i in range(r):
            if fish[i] + 2 < 9:
                fish.append(fish[i] + 2)
            if fish[i] == 7:
                fish[i] = 0
            if fish[i] == 8:
                fish[i] = 1

        sub = 0
    print([
        next[0] + next[4][0], 
        [
            next[1][0] + next[4][1],
            next[1][1] + next[0],
        ],
        [
            next[2][0] + next[1][0],
            next[2][1] + next[1][1]
        ],
        [
            next[3][0] + next[2][0],
            next[3][1] + next[2][1]
        ],
        [
            next[3][0], next[3][1]
        ]
        ])

    for _ in range(iterations % 7):
        for n in range(len(fish)):
            fish[n] -= 1
            if fish[n] < 0:
                fish[n] = 6
                fish.append(8)
    return len(fish)





print(day06())