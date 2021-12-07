def day07():
    # read data to array of ints
    crabs = [int(x) for x in open('day07/input').read().split(',')]
    
    # sort array to find median
    crabs.sort()
    median = int(len(crabs) / 2)

    # calculate the costs for part 1 including variation for arrays of even size into an array
    costs1 = [
        sum([
            # find median of the 3 possible fuel values: median - 1, median, median + 1
            sum([
                # calculate all fuels to reach median while accounting for variation
                abs(crab - crabs[median + variation])
            ]) for crab in crabs
            ]) for variation in range(-1, 2)
        ]

    # calculate average of array
    # using proof https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/
    # based on proof the optimal fuel is always bounded by +- 0.5 of average, or in this case +- 1 so account for variation
    average = int(sum(crabs) / len(crabs))
    # calculate costs for part 2 into array including variation to account for bounds of optimal fuel
    costs2 = [
        sum([
            # calculate the sum for fuel where the cost increases by 1 for each unit moved using the 3 values mean - 1, mean, mean + 1
            sum(range(abs(crab - average + variation) + 1)
        ) for crab in crabs
        ]) for variation in range(-1, 2)
    ]

    # return the minimum of the sum of costs for each equation
    return min(costs1), min(costs2)