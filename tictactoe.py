
tic = 'X'
tac = 'O'
board = ['-', '-', '-','-', '-', '-','-', '-', '-']

def printBoard():
    print('  0  |   1   |  2  ')
    print('  ' + str(board[0]) + '  |   ' + str(board[1]) + '   |  '  + str(board[2]) + '  ')
    print('-------------------')
    print('  3  |   4   |  5  ')
    print('  ' + str(board[3]) + '  |   ' + str(board[4]) + '   |  '  + str(board[5]) + '  ')
    print('-------------------')
    print('  6  |   7   |  8  ')
    print('  ' + str(board[6]) + '  |   ' + str(board[7]) + '   |  '  + str(board[8]) + '  ')

def setPiece(play, pos):
    board[(int(pos))] = str(play)
    printBoard()

selectPositionOne = input('Player X, select an empty position: ')
setPiece(tic, int(selectPositionOne))
selectPositionTwo = input('Player O, select an empty position: ')
setPiece(tac, int(selectPositionTwo))
selectPositionThree = input('Player X, select an empty position: ')
setPiece(tic, int(selectPositionThree))
selectPositionFour = input('Player O, select an empty position: ')
setPiece(tac, int(selectPositionFour))
selectPositionFive = input('Player X, select an empty position: ')
setPiece(tic, int(selectPositionFive))
selectPositionSix = input('Player O, select an empty position: ')
setPiece(tac, int(selectPositionSix))
selectPositionSeven = input('Player X, select an empty position: ')
setPiece(tac, int(selectPositionSeven))
selectPositionEight = input('Player O, select an empty position: ')
setPiece(tic, int(selectPositionEight))
selectPositionNine = input('Player X, select an empty position: ')
setPiece(tac, int(selectPositionNine))


