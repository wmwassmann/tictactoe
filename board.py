newBoard = [
    ['--- ', '--- ', '--- '],
    ['--- ', '--- ', '--- '],
    ['--- ', '--- ', '--- ']
]


def printBoard(board):
    for row in board:
        for pos in row:
            print(pos, end='')
        print()
# printBoard(newBoard)


def boardCoords(input):
    row = int(input / 3)
    column = input
    if column > 2:
        column = int(column % 3)
    return(row, column)

