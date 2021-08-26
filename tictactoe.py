
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
    board.insert(int(pos), str(play))      
    printBoard()
# def setPieceTwo(play): 
#     pieceOneB = play
#     printBoard(pieceOneB)


setPiece(tic, 2)
# setPieceTwo(tac)


# class Board: 
#     def _init_(self, pieceOneA, pieceOneB, pieceOneC, pieceTwoA, pieceTwoB, pieceTwoC, pieceThreeA, pieceThreeB, pieceThreeC):
#         self.pieceOneA = pieceOneA
#         self.pieceOneB = pieceOneB
#         self.pieceOneC = pieceOneC
#         self.pieceTwoA = pieceTwoA
#         self.pieceTwoB = pieceTwoB
#         self.pieceTwoC = pieceTwoC
#         self.pieceThreeA = pieceThreeA
#         self.pieceThreeB = pieceThreeB
#         self.pieceThreeC = pieceThreeC



# def printBoard(pieceOneA, pieceOneB, pieceOneC, pieceTwoA, pieceTwoB, pieceTwoC, pieceThreeA, pieceThreeB, pieceThreeC):
#     print('  ' + pieceOneA + '  |   ' + pieceOneB + '  |  '  + pieceOneC + '  ')
#     print('------------------')
#     print('  ' + pieceTwoA + '  |   ' + pieceTwoB + '  |  '  + pieceTwoC + '  ')
#     print('------------------')
#     print('  ' + pieceThreeA + '  |   ' + pieceThreeB + '  |  '  + pieceThreeC + '  ')


    # class Board: 
#     def _init_(self, pieceOneA, pieceOneB, pieceOneC, pieceTwoA, pieceTwoB, pieceTwoC, pieceThreeA, pieceThreeB, pieceThreeC):
#         self.pieceOneA = pieceOneA
#         self.pieceOneB = pieceOneB
#         self.pieceOneC = pieceOneC
#         self.pieceTwoA = pieceTwoA
#         self.pieceTwoB = pieceTwoB
#         self.pieceTwoC = pieceTwoC
#         self.pieceThreeA = pieceThreeA
#         self.pieceThreeB = pieceThreeB
#         self.pieceThreeC = pieceThreeC