# Global startp variables



tic = '-x- '
tac = '-o- '

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
printBoard(newBoard)



# def setPiece(play, pos, board):   
#     board[(int(pos))] = str(play)
#     printBoard(board)
def setPiece(coordinates, board, turn):   
    row = coordinates[0]
    column = coordinates[1]       
    if (turn % 2) == 0: 
        board[row][column] = '-o- '
        printBoard(board)
        print(turn)
    else:
       board[row][column] = '-x- '
       printBoard(board)
       print(turn) 

def boardCoords(input):
    row = int(input / 3)
    column = input
    if column > 2: column = int(column % 3)
    return(row, column)

def checkSpace(coordinates, board):
    row = coordinates[0]
    column = coordinates[1] 
    if board[row][column] == '--- ':
       return False
    else:
        print('Please select a different position')
        return True 
         

def twoPlayerGame(board):
    # I want to loop through something to only have a single input.  I think a while loop will work as I don't know how long the game will last.
    # Issue falls in when I don't know which player is up.  May need two while loops.


    turn = 0

    while board:
        
        
        if (turn % 2) == 0: 
           inputO = input('Player O, please select a position: ')     
           inputO = int(inputO) - 1   
           coordinates = boardCoords(inputO)
           if checkSpace(coordinates, newBoard):               
               continue
           else:
               turn = turn + 1
           setPiece(coordinates, newBoard, turn)
           
          
        else:
           inputX = input('Player X, please select a position: ')
           inputX = int(inputX) - 1
           coordinates = boardCoords(inputX)
           if checkSpace(coordinates, newBoard):
               continue
           else: 
               turn = turn + 1
           setPiece(coordinates, newBoard, turn)

          






def startGame():

    intro = input('Welcome to Tic Tac Toe! How many players: ')
    if intro == '2':
        printBoard(newBoard)
        twoPlayerGame(newBoard)
    # else:
    #     singleplayerGame()
        

startGame()














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
