# Global startup variables

import random
import board
import gameplay
import dialogs

# Board Functions
newBoard = board.newBoard
printBoard = board.printBoard
boardCoords = board.boardCoords

# Gameplay Functions

setPiece = gameplay.setPiece
resetPiece = gameplay.resetPiece
setComputerPiece = gameplay.setComputerPiece

#Dialogs

compDialog = dialogs.compDialog
victoryCheer = dialogs.victoryCheer




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

def checkSelection(inputCheck):
    checkSelection = input('Confirm square ' + f'"{inputCheck + 1}" ' + '(Y/N) '  )
    if checkSelection.lower() == 'y':
        return True
    else:
        return False
    
        

def playAgain(board):
    answer = input('Play again? Y/N: ')

    for reset in range(0, 9):
        coordinates = boardCoords(reset) 
        resetPiece(coordinates, board)
    printBoard(board)

    while (answer.lower() != 'y') or (answer.lower() != 'n'):
        if answer.lower() == 'y':
            startGame()
        elif answer.lower() == 'n':
            print(
                'Pfft. Fine. As if there are BETTER games than console tic-tac-toe...I see how it is...')
        else:
            answer = input('Is that a no? Please confirm with, Y/N: ')



def winCondition(piece, board, turn):
    if rowWin(piece, board):
        if piece != 'Tom':
            victoryCheer(piece)
            playAgain(board)
            return True
        else:
            input('Foolish fool! None can withstand my mastery of the row!')
            playAgain(board)
            return True
    if diagonalWin(piece, board):
        victoryCheer(piece)
        playAgain(board)
        return True
    if columnWin(piece, board):
        victoryCheer(piece)
        playAgain(board)
        return True
    if draw(turn):
        print('DRAWWWWWWWWWW')
        turn += 1
        playAgain(board)
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
            inputX = int(inputX) - 1
            if checkSelection(inputX):
                if checkValidSpace(inputX) == True:
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
            if checkSelection(inputX):
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
            if checkSelection(inputO):
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
