
tic = 'X'
tac = 'O'


board = [' ', ' ', ' ', ' ', ' ', ' ',  ' ', ' ', ' ']


def printBoard():
    print('  ' + str(board[0]) + '  |   ' + str(board[1]) + '  |  '  + str(board[2]) + '  ')
    print('------------------')
    print('  ' + str(board[3]) + '  |   ' + str(board[4]) + '  |  '  + str(board[5]) + '  ')
    print('------------------')
    print('  ' + str(board[6]) + '  |   ' + str(board[7]) + '  |  '  + str(board[8]) + '  ')



def setPiece(play, pos):
    board[(int(pos))] = str(play)
    printBoard()





def setPieceTwo(play, pos):
    board[(int(pos))] = str(play)     
    printBoard()




def setPieceThree(play, pos):
    board[(int(pos))] = str(play) 
    printBoard()


setPiece(tic, 2)
setPieceTwo(tac, 1)
setPieceThree(tic, 0)
