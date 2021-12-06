years = 80 - 1
original = [1, 1, 2, 1, 0, 0, 0, 0, 0]
for _ in range(years):
    tmp = [
        original[1],
        original[2],
        original[3], 
        original[4],
        original[5],
        original[6],
        original[7] + original[0],
        original[8],
        original[0]
    ]
    original = tmp
print(sum(original))