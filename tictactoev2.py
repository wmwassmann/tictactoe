# Global startp variables
tic = 'X'
tac = 'O'
newBoard = [
    ['-', '-', '-'], 
    ['-', '-', '-'],
    ['-', '-', '-']
]

def printBoard(board):
    for row in board:
        print(row)
    

printBoard(newBoard)


















# # Takes an automatic play depending on which input function is called. Position is player controlled on input
# def setPiece(play, pos):
#     if board[pos] != '-':
#         print('Please select a different space')
#         multiplayerGame()
#         return
#     else:
#         board[(int(pos))] = str(play)
#         printBoard()
        

#     if ((board[0] == 'X') and (board[1] == 'X') and (board[2] == 'X') or
#         (board[0] == 'X') and (board[3] == 'X') and (board[6] == 'X') or
#         (board[0] == 'X') and (board[4] == 'X') and (board[8] == 'X') or
#         (board[1] == 'X') and (board[4] == 'X') and (board[7] == 'X') or
#         (board[2] == 'X') and (board[5] == 'X') and (board[8] == 'X') or
#         (board[2] == 'X') and (board[4] == 'X') and (board[6] == 'X') or
#         (board[3] == 'X') and (board[4] == 'X') and (board[5] == 'X') or
#         (board[6] == 'X') and (board[7] == 'X') and (board[8] == 'X')):
#             print('Player X is the Winner!')
#             startUp()
#     if ((board[0] == 'O') and (board[1] == 'O') and (board[2] == 'O') or 
#         (board[0] == 'O') and (board[3] == 'O') and (board[6] == 'O') or 
#         (board[0] == 'O') and (board[4] == 'O') and (board[8] == 'O') or
#         (board[1] == 'O') and (board[4] == 'O') and (board[7] == 'O') or
#         (board[2] == 'O') and (board[5] == 'O') and (board[8] == 'O') or
#         (board[2] == 'O') and (board[4] == 'O') and (board[6] == 'O') or
#         (board[3] == 'O') and (board[4] == 'O') and (board[5] == 'O') or
#         (board[6] == 'O') and (board[7] == 'O') and (board[8] == 'O')):
#             print('Player O is the Winner!')
#             startUp()


# # These functions alternate players. It's sloppy, but it gets the job done.  To be reworked as I learn more about Python.
# def multiplayerGame():  
#     printBoard()
#     selectPositionOne = input('Player X, select an empty position: ')    
#     setPiece(tic, int(selectPositionOne))
#     selectPositionTwo = input('Player O, select an empty position: ')
#     setPiece(tac, int(selectPositionTwo))
#     selectPositionThree = input('Player X, select an empty position: ')
#     setPiece(tic, int(selectPositionThree))
#     selectPositionFour = input('Player O, select an empty position: ')
#     setPiece(tac, int(selectPositionFour))
#     selectPositionFive = input('Player X, select an empty position: ')
#     setPiece(tic, int(selectPositionFive))
#     selectPositionSix = input('Player O, select an empty position: ')
#     setPiece(tac, int(selectPositionSix))
#     selectPositionSeven = input('Player X, select an empty position: ')
#     setPiece(tic, int(selectPositionSeven))
#     selectPositionEight = input('Player O, select an empty position: ')
#     setPiece(tac, int(selectPositionEight))
#     selectPositionNine = input('Player X, select an empty position: ')
#     setPiece(tic, int(selectPositionNine))


# def printBoard():
#     print('                   ')
#     print('                   ')
#     print('  0  |   1   |  2  ')
#     print('  ' + str(board[0]) + '  |   ' + str(board[1]) + '   |  ' + str(board[2]) + '  ')
#     print('-------------------')
#     print('  3  |   4   |  5  ')
#     print('  ' + str(board[3]) + '  |   ' + str(board[4]) + '   |  ' + str(board[5]) + '  ')
#     print('-------------------')
#     print('  6  |   7   |  8  ')
#     print('  ' + str(board[6]) + '  |   ' + str(board[7]) + '   |  ' + str(board[8]) + '  ')

# # Initialize Board


# def startUp():

#     intro = input('Welcome to Tic Tac Toe! How many players: ')
#     if intro == '2':
#         printBoard()
#         multiplayerGame()
        

# startUp()
