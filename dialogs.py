


import board
import gameplay

printBoard = board.printBoard
boardCoords = board.boardCoords
resetPiece = gameplay.resetPiece


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


def victoryCheer(piece):
    print('Player ' + f'{piece}' + 'wins!')
