''' game of life '''

import numpy as np


TILE = {}
STATE = ['Untouched', 'Populated', 'Underpopulated', 'Overpopulated']
STATE = list(enumerate(STATE))

def create_board(size):
    ''' create board '''
    for i in range(1, (size*size)+1):
        TILE[i] = [i, False, STATE[0], []]
    return size

def neighbors_corners(size):
    ''' create network of checks for dict '''
    #helper variables
    lowerleft = (size * (size-1)) + 1
    lowerright = size * size

    #Get Corners: UL, UR, LL, LR
    TILE[1][3].append(TILE[2][0])
    TILE[1][3].append(TILE[size+1][0])
    TILE[size][3].append(TILE[size-1][0])
    TILE[size][3].append(TILE[size*2][0])
    TILE[lowerleft][3].append(TILE[lowerleft+1][0])
    TILE[lowerleft][3].append(TILE[lowerleft-size][0])
    TILE[lowerright][3].append(TILE[lowerright-1][0])
    TILE[lowerright][3].append(TILE[lowerright-size][0])

def game_of_life(size):
    ''' main engine '''
    size = create_board(size)
    neighbors_corners(size)

    # to get a better sense of things #
    print(np.arange(1, size * size + 1).reshape(size, size))

game_of_life(3)