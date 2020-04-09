xAxis = [8, 7, 6, 5, 4, 3, 2, 1]
yAxis = ["a", "b", "c", "d", "e", "f", "g", "h"]

def createBoard():
    global xAxis,yAxis
    for y in yAxis:
        for x in xAxis:
            if x == 1:
                if y == "a":
                    board[str(x) + str(y)] = "wrook"
                elif y == "b":
                    board[str(x) + str(y)] = "wknight"
                elif y == "c":
                    board[str(x) + str(y)] = "wbishop"
                elif y == "d":
                    board[str(x) + str(y)] = "wqueen"
                elif y == "e":
                    board[str(x) + str(y)] = "wking"
                elif y == "f":
                    board[str(x) + str(y)] = "wbishop"
                elif y == "g":
                    board[str(x) + str(y)] = "wknight"
                elif y == "h":
                    board[str(x) + str(y)] = "wrook"
            elif x == 2:
                board[str(x) + str(y)] = "wpawn"
            elif x == 7:
                board[str(x) + str(y)] = "bpawn"
            elif x == 8:
                if y == "a":
                    board[str(x) + str(y)] = "brook"
                elif y == "b":
                    board[str(x) + str(y)] = "bknight"
                elif y == "c":
                    board[str(x) + str(y)] = "bbishop"
                elif y == "d":
                    board[str(x) + str(y)] = "bqueen"
                elif y == "e":
                    board[str(x) + str(y)] = "bking"
                elif y == "f":
                    board[str(x) + str(y)] = "bbishop"
                elif y == "g":
                    board[str(x) + str(y)] = "bknight"
                elif y == "h":
                    board[str(x) + str(y)] = "brook"
            else:
                board[str(x) + str(y)] = None
    return(board)

def isValidChessBoard(board):
    global xAxis,yAxis
    piecesCount = {"b": 0, "w": 0}
    pawnCount = {"b": 0, "w": 0}
    hasKing = {"b": False, "w": False}
    pieceColor = ["b","w"]
    pieceType = ["pawn","knight","bishop","rook","queen","king"]

    for k, v in board.items():
        if int(k[0]) not in xAxis:
            return False

        if k[1] not in yAxis:
            return False

        if v is not None:
            if v[0] not in pieceColor:
                return False

            thisPieceColor = v[0]
            piecesCount[thisPieceColor] += 1

            if piecesCount[thisPieceColor] >= 17:
                return False

            thisPieceType = v[1:]

            if thisPieceType not in pieceType:
                return False

            elif thisPieceType == "pawn":
                pawnCount[thisPieceColor] += 1

                if pawnCount[thisPieceColor] >= 9:
                    return False

            elif thisPieceType == "king":
                if hasKing[thisPieceColor] == True:
                    return False
                else:
                    hasKing[thisPieceColor] = True

    if list(hasKing.values()) != [True, True]:
        return False

    return True


board = {}
createBoard()
print(isValidChessBoard(board))