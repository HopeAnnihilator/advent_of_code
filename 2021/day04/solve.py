def day04():
    f = open('day04/input')
    
    verWins = [[i + j for j in range(0, 25, 5)] for i in range(5)]
    hozWins = [[j + i for j in range(5)] for i in range(0, 25, 5)]
    diagWins = [[i for i in range(0, 25, 6)], [i for i in range(4, 21, 4)]]
    
    data = {
        'randints': [int(i) for i in f.readline().strip('\n').split(',')],
        'boards': [],
        'wins': verWins + hozWins ,
        'solveTimes': []
    }

    for i in f:
        board = [int(j) for j in i.strip('\n').split(' ') if j]
        if not board:
            data['boards'].append([])
        else:
            data['boards'][-1].append(board)

    for board in data['boards']:
        data['solveTimes'].append(solve(board, data['randints'], data['wins']))

    return min(data['solveTimes'])[-1], max(data['solveTimes'])[-1]

def solve(board, randints, wins):
    board = [item for nest in board for item in nest]
    for i in randints:
        if i in board:
            board[board.index(i)] = None
            if check(board, wins):
                return randints.index(i), i, sum([i for i in board if i]), i * sum([i for i in board if i])

def check(board, wins):
    marks = [index for index, element in enumerate(board) if element == None]
    for win in wins:
        if set(win) <= set(marks):
            return True
    return False

