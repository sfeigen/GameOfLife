''' check and update functions '''

# Seed Config. 1: (Infinite)
# Run check() to transfer states.
# __ __ __ __ __      __ __ __ __ __      __ __ __ __ __
#|__|__|__|__|__|    |__|__|__|__|__|    |__|__|__|__|__|
#|__|07|__|09|__|    |__|07|__|09|__|    |__|up|__|09|__|
#|__|12|13|14|__| -> |rp|op|op|14|__| -> |11|rp|rp|14|rp|
#|__|17|18|__|__|    |rp|op|op|rp|__|    |16|rp|--|19|__|
#|21|__|__|__|__|    |up|rp|__|__|__|    |up|up|__|__|__|
#
# Run update() to assign new states.
#
# Seed Config. 2: (Finite, dies @ 3)
# Run check() to transfer states.
# __ __ __ __ __      __ __ __ __ __      __ __ __ __ __
#|__|__|__|__|__|    |__|__|__|__|__|    |__|__|__|__|__|
#|__|__|08|09|__|    |__|__|08|09|__|    |__|__|__|__|__|
#|__|__|13|__|__| -> |__|__|__|__|__| -> |__|12|__|14|__|
#|__|17|18|__|__|    |__|17|18|__|__|    |__|__|__|__|__|
#|__|__|__|__|__|    |__|__|__|__|__|    |__|__|__|__|__|
#

import json
from setup_board import STATE

STORE = []

def check(tiles):
    ''' checks the state of the board '''
    board = tiles

    # Conway's logic
    count = 0
    dead_count = 0
    for tile in board:
        for nbr in board:
            # select live tiles and check if neighbor is alive
            if board[tile][1] and board[nbr][1] and tile in board[nbr][3]:
                count += 1
            # select dead tiles and check if neighbor is alive
            elif board[tile][1] is False and board[nbr][1] and tile in board[nbr][3]:
                dead_count += 1
            elif board[tile][1] and not board[nbr][1]:
                board[tile][2] = STATE[2]

        # apply Conway
        if count == 2 or count == 3:
            board[tile][2] = STATE[1]
            count = 0
        elif count == 1:
            board[tile][2] = STATE[2]
            count = 0
        elif count > 3:
            board[tile][2] = STATE[3]
            count = 0
        # wake the dead
        elif dead_count == 3:
            board[tile][2] = STATE[1]
        count = 0
        dead_count = 0
    return board

def update(board):
    ''' updates the state of the board '''
    for tile in board:
        if board[tile][2] == STATE[1]:
            board[tile][1] = True
        if board[tile][2] == STATE[0] or board[tile][2] == STATE[2] or board[tile][2] == STATE[3]:
            board[tile][1] = False
    json_store(board)
    return board

def json_store(board):
    ''' convert state to json and save '''
    json_board = json.dumps(board)
    STORE.append(json_board)

def endgame(board):
    ''' checks for end condition and returns false '''
    end = 0
    for tile in board:
        if board[tile][1] is False:
            end += 1
    if end == len(board):
        return False
    else:
        return True

def print_status(board):
    '''prints out status'''
    for tile in board:
        print(tile, ":", board[tile][1], board[tile][2])
