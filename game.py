import math

global aiPlayer,humanPlayer,node_depth, win, lose, draw
node_depth = 0
aiPlayer = "O"
win = +10
lose = -10
draw = 0
humanPlayer = "X"


availableSpots = []


'''
DONE : checkOccupiedPos, boardis full, display board, getopponentpiece, getlegalmoves

'''

def checkOccupiedPos(board, position): #position occupied
    legal_moves = getLegalMoves(board)
    if board[position[0]][position[1]] != '_':
        return True
    '''
    for i in range(len(legal_moves)):
        if position[0]==board[i][0] and position[1]==board[i][1]:
            return False'''

    return False



def getBoardState(board, piece): #get_board_state
    opp_piece = getOpponentPiece(piece)
    pos_occupied = getOccupiedPos(board,piece)
    did_win = didWinGame(pos_occupied)
    if did_win:
        return 10
    pos_occupied = getOccupiedPos(board, opp_piece)
    did_lose = didWinGame(pos_occupied)
    if did_lose:
        return -10

    is_full = boardisFull(board)
    if is_full:
        return 0
    return 0


def displayBoard(board): #print_board
    print ("   0    1    2 ")
    col_num = [0,1,2]
    for i in board:
        print(col_num[0], end = '')
        col_num.pop(0)
        for j in i:
            print(f"|_{j}_|", end = '')
        print('\n')

def winState(): #winning_states
    
    board = [
        [[0,0], [0,1],[0,2]],[[1,0], [1,1],[1,2]],[[2,0], [2,1],[2,2]],
        [[0,0], [1,0],[2,0]],[[0,1], [1,1],[2,1]],[[0,2], [1,2],[2,2]],
        [[0,0], [1,1],[2,2]],[[2,0], [1,1],[0,2]]
    ]
    return board


def getOccupiedPos(board, piece):
    occupied_pos = []
    for i in range(3):
        for j in range(3):
            if piece == board[i][j]:
                occupied_pos.append([i,j])
    return occupied_pos

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
    win_states = winState()
    for i in range(len(win_states)):
        did_win = False
        current_state = win_states[i]
        for j in range(3):
            if current_state[j] in occupied_pos:
                index = occupied_pos.index(current_state[j])
                if not index != occupied_pos[-1]:
                    did_win = True
                    break
        if did_win:
            break
    return did_win

def getOpponentPiece(piece): #done
    if piece == humanPlayer:
        opponent_piece = aiPlayer
    else:
        opponent_piece = humanPlayer
    return opponent_piece




def minimax(board, piece, node_depth, alpha, beta):
    best_move = [-1, -1]
    if piece == aiPlayer:
        best_score =  -10
    else:
        best_score = 10
    
    if boardisFull(board) or getBoardState(board,aiPlayer)!=0:
        best_score = getBoardState(board, aiPlayer)
        return [best_score, best_move]
    legal_moves = getLegalMoves(board)
    for i in range(len(legal_moves)):
        current = legal_moves[i]
        board[current[0]][current[1]] = piece
        #max
        if piece == aiPlayer:
            score = minimax(board, humanPlayer, node_depth+1, alpha , beta)[0]
            if score > best_score:
                best_score = score - (node_depth*10)
                best_move = current
                alpha = max(alpha,best_score)
                board[current[0]][current[1]] = '_'
                if beta<=alpha:
                    break
        else: #min oponent turn
            score = minimax(board, aiPlayer, node_depth+1, alpha, beta)[0];
            if score< best_score:
                best_score = score + node_depth*10
                best_move = current
                beta = min(beta, best_score)
                board[current[0]][current[1]] = '_'
                if beta<=alpha:
                    break
        board[current[0]][current[1]] = '_'
    return [best_score, best_move]
        

def checkGameOver(board):#done
    draw = 0
    if boardisFull(board):
        return True
    elif draw!= getBoardState(board, aiPlayer):
        return True
    return False

 
def getGameState(state):
    if state == 10:
        print("you win!!")
    elif state == -10:
        print("you lose")
    else:
        print("game tied")

def main():
    board = [['_','_','_'],['_','_','_'],['_','_','_']]
    print("Human Player - X, AI Player - O")
    displayBoard(board)
    while not checkGameOver(board):
        row_inp = int(input("Select row to make move:"))
        col_inp = int(input("Select column to make move:"))
        if checkOccupiedPos(board, [row_inp,col_inp]):
            print("Position occupied, try again!")
            continue
        else:
            board[row_inp][col_inp] = humanPlayer
        ai_move = minimax(board, aiPlayer, node_depth, -10, 10)
        print(ai_move)
        board[ai_move[1][0]][ai_move[1][1]] = aiPlayer
        displayBoard(board)
    print("Game over")

if __name__ == "__main__":
    main()