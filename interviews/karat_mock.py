# Karat practice interview on 8/1/2018 using coderpad.io

# We are designing a 2D game and we have a game map that we represent by an integer matrix. For now, each cell can be a wall (denoted by -1) or a blank space (0).

# board = [
#     [ 0,  0,  0, 0, -1 ],
#     [ 0, -1, -1, 0,  0 ],
#     [ 0,  0,  0, 0,  0 ],
#     [ 0, -1,  0, 0,  0 ],
#     [ 0,  0,  0, 0,  0 ],
#     [ 0,  0,  0, 0,  0 ],
# ]

# The player can move 1 space at a time up, down, left, or right. The player can't go through walls or land on a wall, or go through the edges of the board.

# Write a function that, given a board and a player starting position (represented as a row-column pair), returns all of the possible next positions for the player.

# Expected output (in any order):
# board, (3, 2):
#   (2, 2), (3, 3), (4, 2)

# board, (5, 0):
# (4, 0), (5, 1)

board = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]

# need width and height of board
# compare starting position with indices on board to see if valid move

def moves(board, start_position):
    height = len(board)
    width = len(board[0])
    poss_moves = []

    ######## start Jamie's code ##############

    row, col = start_position
    
    moves1 = []
    moves1.append([row +1, col])
    moves1.append([row -1, col])
    moves1.append([row, col-1])
    moves1.append([row, col+1])
    
    for m in moves1:
        if m[0] == -1 or\
           m[0] == height or\
           m[1] == -1 or\
           m[1] == width:
            continue
        if board[m[0]][m[1]] == 0:
            poss_moves.append([m[0], m[1]])
    print(poss_moves)
    return

    ######## end Jamie's code ##############
    

    # bottom edge case
    if start_position[0] == height - 1:
        # top move
        if board[start_position[0] - 1][start_position[1]] == 0:
            poss_moves.append([start_position[0] - 1, start_position[1]])
    # top edge case
    elif start_position[0] == 0:
        # bottom move
        if board[start_position[0] + 1][start_position[1]] == 0:
            poss_moves.append([start_position[0] + 1, start_position[1]])
    
    else:
        # bottom move
        if board[start_position[0] + 1][start_position[1]] == 0:
            poss_moves.append([start_position[0] + 1, start_position[1]])
        # top move
        if board[start_position[0] - 1][start_position[1]] == 0:
            poss_moves.append([start_position[0] - 1, start_position[1]])
    
    # not left or right edge case
    if start_position[1] != width - 1 and start_position[1] != 0:
        # right move
        if board[start_position[0]][start_position[1] + 1] == 0:
            poss_moves.append([start_position[0], start_position[1] + 1])
        # left move
        if board[start_position[0]][start_position[1] - 1] == 0:
            poss_moves.append([start_position[0], start_position[1] - 1])
    # right edge case
    elif start_position[1] == width - 1:
        # left move
        if board[start_position[0]][start_position[1] - 1] == 0:
            poss_moves.append([start_position[0], start_position[1] - 1])
    # left edge case
    else:
        # right move
        if board[start_position[0]][start_position[1] + 1] == 0:
            poss_moves.append([start_position[0], start_position[1] + 1])
    
    print(poss_moves)
    return poss_moves

moves(board, (2, 0)) # 1,0 and 3,0 and 2,1
moves(board, (5, 0)) 
moves(board, (0, 3)) 
moves(board, (3, 2)) 
moves(board, (2, 5))
moves(board, (0, 0)) 
