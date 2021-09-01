
import board

printBoard = board.printBoard

def setPiece(coordinates, board, turn):
    row = coordinates[0]
    column = coordinates[1]
    if (turn % 2) == 0:
        board[row][column] = '-o- '
        printBoard(board)

    else:
        board[row][column] = '-x- '
        printBoard(board)


def resetPiece(coordinates, board):
    row = coordinates[0]
    column = coordinates[1]
    board[row][column] = '--- '
    


def setComputerPiece(coordinates, board):
    row = coordinates[0]
    column = coordinates[1]
    board[row][column] = '-o- '
    printBoard(board)

