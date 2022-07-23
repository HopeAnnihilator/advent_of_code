def day05():
    graph = {}
    lines = [[[int(n) for n in j.split(',')] for j in i.strip('\n').split(' -> ')] for i in open('day05/input').readlines()]
    return day05_01(lines, graph), day05_02(lines, graph)


    

def day05_01(lines, graph):
    for line in lines:
        points = line[0], line[1]
        if points[0][0] == points[1][0]:
            lineRange = [points[0][1], points[1][1]]
            line = [[points[0][0], i] for i in range(min(lineRange), max(lineRange) + 1)]
            write_graph(line, graph)

        elif points[0][1] == points[1][1]:
            lineRange = [points[0][0], points[1][0]]
            line = [[i, points[0][1]] for i in range(min(lineRange), max(lineRange) + 1)]
            write_graph(line, graph)
    return len([i for i in graph if graph[i] > 1])

def day05_02(lines, graph):
    for line in lines:
        points = line[0], line[1]
        if  points[0][0] != points[1][0] and points[0][1] != points[1][1]:
            lineRange = [[points[0][0], points[1][0]], [points[0][1], points[1][1]]]
            subline = [i for i in range(min(lineRange[0]), max(lineRange[0]) + 1)]
            subline2 = [i for i in range(min(lineRange[1]), max(lineRange[1]) + 1)]
            if [subline[0], subline2[0]] not in points:
                subline2.reverse()
            line = [[subline[i], subline2[i]] for i in range(len(subline))]
            write_graph(line, graph)
    return len([i for i in graph if graph[i] > 1])

def write_graph(line, graph):
    for point in line:
        if str(point) not in graph:
            graph[str(point)] = 1
        else:
            graph[str(point)] += 1
