import numpy as np

def boardState(board):
    
    for row in range(3):
        if (board[row][0]==board[row][1] and board[row][1]==board[row][2]):
            if board[row][0] == 'x':
                return 1
            elif board[row][0] == 'o':
                return -1 
    
    for col in range(3):
        if (board[0][col]==board[1][col] and board[1][col]==board[2][col]):
            if board[0][col] == 'x':
                return 1
            elif board[0][col] == 'o':
                return -1 
    
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0] == 'x':
            return 1
        elif board[0][0] == 'o':
            return -1
    elif board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        if board[0][2] == 'x':
            return 1
        elif board[0][2] == 'o':
            return -1
    
    return 0

def movesLeft(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                return True
    
    return False

def minimax(board,d,isMaximising):
    if boardState(board) == 1:
        return 1
    if boardState(board) == -1:
        return -1
    if not movesLeft(board):
        return 0
    
    if(isMaximising):
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'x'
                    best = max(best,minimax(board,d+1,False))
                    board[i][j] = '_'
        
        return best
    
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'o'
                    best = min(best,minimax(board,d+1,True))
                    board[i][j] = '_'

        return best

def getBestMove(board):
    best = -1000
    bestMove = (-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'x'
                moveVal = minimax(board,0,False)
                board[i][j] = '_'
                if moveVal>best:
                    best = moveVal
                    bestMove = (i,j)
    
    return bestMove

def getPlayerMove():
    pMove = (int(input("ROW: ")),int(input("COL: ")))
    return pMove

def play(board):
    while(True):
        print("\n\n")
        print(np.matrix(board))
        

        if(boardState(board)==1):
            print("COMPUTER WINS")
            break
        elif(boardState(board)==-1):
            print("PLAYER WINS")
            break
        elif(not movesLeft(board)):
            if(boardState(board)==0):
                print("TIE")
                break


        if(movesLeft(board)):
            pMove = getPlayerMove()
            board[pMove[0]][pMove[1]] = 'o'
        if(movesLeft(board)):
            cMove = getBestMove(board)
            board[cMove[0]][cMove[1]] = 'x'

board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

if __name__ == '__main__':
    play(board)
