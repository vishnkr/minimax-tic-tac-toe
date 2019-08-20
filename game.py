import math

global aiPlayer
global humanPlayer
aiPlayer = "O"
win = +10
lose = -10
draw = 0
humanPlayer = "X"


availableSpots = []


'''
DONE : checkOccupiedPos, boardis full, display board, getopponentpiece, getlegalmoves

'''
    
def checkOccupiedPos(board, position):
    legal_moves = getLegalMoves(board)
    for i in range(len(legal_moves)):
        if position[0]==board[i][0] and position[1]==board[i][1]:
            return False
    return True


def findWin():

    pass

def displayBoard(board):
    print ("   1    2    3 ")
    col_num = [1,2,3]
    for i in board:
        print(col_num[0], end = '')
        col_num.pop(0)
        for j in i:
            print(f"|_{j}_|", end = '')
        print('\n')

def winState():
    board = []
    for row in range(3):
        temp = []
        for col in range(3):
            temp.append([row,col])
        board.append(temp)
    for col in range(3):
        temp = []
        for row in range(3):
            temp.append([col,row])
        board.append(temp)
    board.append([[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]])
    return board


def getLegalMoves(board):
    legal_moves =[]
    for i in range(3):
        for j in range(3):
            if board[i][j]!=aiPlayer and board[i][j]!=humanPlayer:
                legal_moves.append([i,j])
    return legal_moves
        
def boardisFull(board):
    legal_moves = getLegalMoves(board)
    if not len(legal_moves):
        return True
    else:
        return False
    

def didWinGame(occupied_pos):
    win_state = winState()
    for i in range(len(win_state)):
        won_game = True
        current_state = win_state[i]
        for j in range(3):
            if current_state[j] in occupied_pos:
                cur_index = occupied_pos.index(current_state[j])
                if not (cur_index!=occupied_pos[-1]):
                    won_game = False
                    break
    return won_game

df
def getOpponentPiece(piece):
    if piece == humanPlayer:
        opponent_piece = aiPlayer
    else:
        opponent_piece = humanPlayer
    return opponent_piece

def checkBoardState(board, piece):
    opponent = getOpponentPiece(piece)
    occupiedPos = getOccupiedPos(board, piece)


def minimax(board, piece, node_depth, alpha, beta):
    best_move = [-1, -1]
    if piece == aiPlayer:
        best_score =  -10
    else:
        best_score = 10
    
    if boardisFull(board)
    pass

def checkGameOver(board):
    draw = 0
    if boardisFull(board):
        return True
    elif draw!= getBoardState(board, AI_marker):
        return True
    return False

 
def getGameState(state):
    if state == 'win':
        print("you win!!")
    elif state == 'loss':
        print("you lose")
    else:
        print("game tied")

def main():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    print("Human Player - X, AI Player - O")
    displayBoard(board)
    '''
    while not checkGameOver(board):
        row_inp = int(input("Select row to make move:"))
        col_inp = int(input("Select column to make move:"))'''

if __name__ == "__main__":
    main()