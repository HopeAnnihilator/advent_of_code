def day09():
    f = [[int(n) for n in i.strip('\n')] for i in open('day09/input').readlines()]
    return day09_01(f), day09_02(f)


def day09_01(f):
    lows = []
    for row in range(len(f)):
        for col in range(len(f[row])):
            edges = find_edges(f, row, col)
            if f[row][col] < min(edges):
                lows.append(f[row][col] + 1)
    return sum(lows)

def day09_02(f):
    row = 0
    col = 0
    basins = [] 
    while row < len(f):
        basin = []
        edges = find_edges(f, row, col)
        if sum(f[row]) == 9 * len(f[row]):
            row += 1
            col = 0
        elif f[row][col] == 9:
            col += 1
        else:
            if sum(edges) == 9 * 4:
                row += 1
            elif f[row][col] < min(edges):
                trace(f, row, col, basin)
                col = 0
                basins.append(len(basin))
            else:
                match edges.index(min(edges)):
                    case 0:
                        col -= 1
                    case 1:
                        col += 1
                    case 2:
                        row -= 1
                    case 3:
                        row += 1
    total = 1
    for _ in range(3):
        largest = basins.index(max(basins))
        total *= basins[largest]
        basins.pop(largest)
    return total

def trace(f, row, col, basin):
    if f[row][col] == 9:
        return
    basin.append(f[row][col])
    f[row][col] = 9
    edges = find_edges(f, row, col)
    if sum(edges) == 9 * 4:
        return
    for i in range(len(edges)):
        if edges[i] != 9:
            match i:
                case 0:
                    trace(f, row, col - 1, basin)
                case 1:
                    trace(f, row, col + 1, basin)
                case 2:
                    trace(f, row - 1, col, basin)
                case 3:
                    trace(f, row + 1, col, basin)
            trace(f, row, col, basin)

def find_edges(f, row, col):
    edges = []
    add_edge(f, row, col - 1, edges)
    add_edge(f, row, col + 1, edges)
    add_edge(f, row - 1, col, edges)
    add_edge(f, row + 1, col, edges)
    return edges

    
def add_edge(f, row, col, edges):
    if row < 0 or col < 0:
        edges.append(9)
        return
    try:
        edges.append(f[row][col])
    except:
        edges.append(9)

print(day09())