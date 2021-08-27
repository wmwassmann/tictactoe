
tic = 'X'
tac = 'O'
board = ['-', '-', '-','-', '-', '-','-', '-', '-']


def printBoard():
    print('                   ')
    print('                   ')
    print('  0  |   1   |  2  ')
    print('  ' + str(board[0]) + '  |   ' + str(board[1]) + '   |  '  + str(board[2]) + '  ')
    print('-------------------')
    print('  3  |   4   |  5  ')
    print('  ' + str(board[3]) + '  |   ' + str(board[4]) + '   |  '  + str(board[5]) + '  ')
    print('-------------------')
    print('  6  |   7   |  8  ')
    print('  ' + str(board[6]) + '  |   ' + str(board[7]) + '   |  '  + str(board[8]) + '  ') 
printBoard()

def setPiece(play, pos):
    board[(int(pos))] = str(play)    
    printBoard()          
    
    if ((board[0] and board[1] and board[2]) == 'X' or 
        (board[0] and board[3] and board[6]) == 'X' or 
        (board[0] and board[4] and board[8]) == 'X' or
        (board[1] and board[4] and board[7]) == 'X' or
        (board[2] and board[5] and board[8]) == 'X' or
        (board[2] and board[4] and board[6]) == 'X' or
        (board[3] and board[4] and board[5]) == 'X' or
        (board[6] and board[7] and board[8]) == 'X'):
            print('Player X is the Winner!')

        
            
    # if ((board[0] and board[1] and board[2] == 'O') or 
    #     (board[0] and board[3] and board[6] == 'O') or 
    #     (board[0] and board[4] and board[8] == 'O') or
    #     (board[1] and board[4] and board[7] == 'O') or
    #     (board[2] and board[5] and board[8] == 'O') or
    #     (board[2] and board[4] and board[6] == 'O') or
    #     (board[3] and board[4] and board[5] == 'O') or
    #     (board[6] and board[7] and board[8] == 'O')):
    #         print('Player O is the Winner!')   

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







