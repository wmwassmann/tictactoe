# Global startp variables
import random


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
    printBoard(board)



def setComputerPiece(coordinates, board):
    row = coordinates[0]
    column = coordinates[1]
    board[row][column] = '-o- '
    printBoard(board)


def compDialog(turn):
    if turn == 1:
        input('Tom the Tictactical Terror - Ahh, a decent start')
        input('Tom the Tictactical Terror - I counter with...')
    if turn == 3:
        input('Tom the Tictactical Terror - Hmmm... I see what you are doing...')
        input('Tom the Tictactical Terror - And I won\'t work!')
    if turn == 5:
        input('Tom the Tictactical Terror - Coming in for the win I see.')
        input('Tom the Tictactical Terror - Well I still have a few tricks up my sleeve!')
    if turn == 7:
        input('I am still here! You haven\'t beaten me yet!')
    if turn == 9:
        input('It seems you and I are at an impasse...')
        input('Care to play again?')
    


def boardCoords(input):    
    row = int(input / 3)
    column = input
    if column > 2:
        column = int(column % 3)
    return(row, column)

def checkSpace(coordinates, board, input):
    row = coordinates[0]
    column = coordinates[1]
    if (board[row][column] == '--- '):
        return False
    else:
        print("Position " + f'{input + 1} ' + "is already being occupied.")
        print('Please select a different position')
        return True

def checkValidSpace(input): 
    try:
        (int(input) in range(1, 9)) and int(input)
        return True
    except:
        print(f"'{input}' is not a valid input. Please enter a numeric value of 1-9")
        return False


def victoryCheer(piece):
    print('Player ' + f'{piece}' + 'wins!')


def playAgain(board, turn):     
    # reset = 10
    
    answer = input('Play again? Y/N: ')
    for reset in range(0, 9): 
        coordinates = boardCoords(reset)
        print(coordinates)
        resetPiece(coordinates, board)
  
             
    while (answer.lower() != 'y') or (answer.lower() != 'n'):
        if answer.lower() == 'y':        
            startGame()
        elif answer.lower() == 'n':
            print('Pfft. Fine. As if there are BETTER games than console tic-tac-toe...I see how it is...')    
        else: 
            answer = input('Is that a no? Please confirm with, Y/N: ')


def winCondition(piece, board, turn):
    if rowWin(piece, board):
        if piece != 'Tom':
            victoryCheer(piece)
            playAgain(board, turn)
            return True
        else: 
            input('Foolish fool! None can withstand my mastery of the row!')
            playAgain(board, turn)
            return True
    if diagonalWin(piece, board):
        victoryCheer(piece)
        playAgain(board, turn)
        return True
    if columnWin(piece, board):
        victoryCheer(piece)
        playAgain(board, turn)
        return True
    if draw(turn):      
        print('DRAWWWWWWWWWW')  
        turn += 1
        playAgain(board, turn)
    return False


def rowWin(piece, board):
    for row in board:
        rowWin = True
        for pos in row:
            if pos != piece:
                rowWin = False
                break
        if rowWin:
            return True
    return False


def diagonalWin(piece, board):
    if (board[0][0] == piece) and (board[1][1] == piece) and (board[2][2] == piece):
        return True
    elif (board[2][0] == piece) and (board[1][1] == piece) and (board[0][2] == piece):
        return True
    return False


def columnWin(piece, board):
    # piece = '-x- ' or '-o- '
    if (board[0][0] == piece) and (board[1][0] == piece) and (board[2][0] == piece):
        return True
    elif (board[0][1] == piece) and (board[1][1] == piece) and (board[2][1] == piece):
        return True
    elif (board[0][2] == piece) and (board[1][2] == piece) and (board[2][2] == piece):
        return True
    return False

def draw(turn):
    if turn == 9: 
        return True
    return False

def singlePlayerGame(board):
    input('Single Player Selected!')
    input('Tom the Tictactical Terror Has Joined the Game!')
    input('Tom the Tictactical Terror - Prepare to feel my wrath!')
    printBoard(board)
    turn = 0

    while turn < 9:  
        playerX = '-x- '
        playerComp = 'Tom'

        if (turn % 2) == 0:    
            inputX = input('Player X, please select an empty position 1-9: ')
           
            if checkValidSpace(inputX) == True:
                inputX = int(inputX) - 1
                coordinates = boardCoords(inputX)
                if checkSpace(coordinates, newBoard, inputX):
                    continue
                else: 
                    turn = turn + 1
                setPiece(coordinates, newBoard, turn)  
                compDialog(turn)       
            if winCondition(playerX, newBoard, turn):
                break

        else:           
            
            inputO = random.randint(0, 8)
            if checkValidSpace(inputO) != True:  
                inputO = random.randint(0, 8)              
            else:
                coordinates = boardCoords(inputO)
                if checkSpace(coordinates, newBoard, inputO):
                    continue
                else: 
                    turn = turn + 1
                setComputerPiece(coordinates, newBoard)                
            if winCondition(playerComp, newBoard, turn):
                break


def twoPlayerGame(board):
    input('Two Player Selected!')
    input('May the best player win!')
    turn = 0

    while turn < 9:
        playerO = '-o- '
        playerX = '-x- '

        if (turn % 2) == 0:
            inputX = input('Player X, please select an empty position 1-9: ')
            inputX = int(inputX) - 1
            checkValidSpace(inputX)
            if checkValidSpace(inputX):
                coordinates = boardCoords(inputX)
                if checkSpace(coordinates, newBoard, inputX):
                    continue
                else:
                    turn = turn + 1
                setPiece(coordinates, newBoard, turn)
            if winCondition(playerX, newBoard, turn):
                break

        else:
            inputO = input('Player O, please select an empty position 1-9: ')
            inputO = int(inputO) - 1
            if checkValidSpace(inputO) == True:
                coordinates = boardCoords(inputO)
                if checkSpace(coordinates, newBoard, inputO):
                    continue
                else:
                    turn = turn + 1
                setPiece(coordinates, newBoard, turn)
            if winCondition(playerO, newBoard, turn):
                break


def startGame():

    intro = input('Welcome to Tic Tac Toe! How many players: ')
    while (intro != '1') or (intro != '2'):
        if intro == '1':
            printBoard(newBoard)
            singlePlayerGame(newBoard)
        elif intro == '2':
            printBoard(newBoard)
            twoPlayerGame(newBoard)
        else:
            intro = input('Please select a number between 1-2: ')

startGame()
