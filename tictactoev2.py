# Global startp variables


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

def checkSpace(coordinates, board, input):
    row = coordinates[0]
    column = coordinates[1] 
    if board[row][column] == '--- ':
       return False
    else:
        print("Position " + f'{input + 1} ' + "is already being occupied.")
        print('Please select a different position')
        return True 

def checkValidSpace(input):
    try:
        int(input)       
        return True
    except:        
        print(f"'{input}' is not a valid input. Please enter a numeric value of 1-9")  
        return False

# def winCondition():

         

def twoPlayerGame(board):
    # I want to loop through something to only have a single input.  I think a while loop will work as I don't know how long the game will last.
    # Issue falls in when I don't know which player is up.  May need two while loops.


    turn = 0

    while turn < 9:
        
        
        if (turn % 2) == 0: 
           inputO = input('Player O, please select a position: ')   
          
        #    checkValidSpace(inputO)
           if checkValidSpace(inputO) == True:
              inputO = int(inputO) - 1   
              coordinates = boardCoords(inputO)
              if checkSpace(coordinates, newBoard, inputO):               
                  continue
              else:
                  turn = turn + 1
              setPiece(coordinates, newBoard, turn)
                
          
        else:
           inputX = input('Player X, please select a position: ')
           inputX = int(inputX) - 1
           checkValidSpace(inputX)
           if checkValidSpace(inputX):
               coordinates = boardCoords(inputX)
               if checkSpace(coordinates, newBoard, inputX):
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

