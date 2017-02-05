''' check and update functions '''
from search_optimized import board_tiles
import numpy as np

# debug
SIZE = 6
TILE = board_tiles(SIZE)
STATE = ['Untouched', 'Populated', 'Underpopulated', 'Overpopulated']
STATE = list(enumerate(STATE))

def seed():
    ''' stable '''
    TILE[9][1] = True
    TILE[9][2] = STATE[1]
    TILE[10][1] = True
    TILE[10][2] = STATE[1]
    TILE[14][1] = True
    TILE[14][2] = STATE[1]
    TILE[15][1] = True
    TILE[15][2] = STATE[1]
    TILE[16][1] = True
    TILE[16][2] = STATE[1]
    TILE[17][1] = True
    TILE[17][2] = STATE[1]
    TILE[20][1] = True
    TILE[20][2] = STATE[1]
    TILE[21][1] = True
    TILE[21][2] = STATE[1]

def check():
    ''' checks the state of the board '''
    return None

def update():
    ''' updates the state of the board '''
    return None

def endgame():
    ''' checks for end condition and returns false '''
    return False

def print_status(tile):
    ''' print status '''
    for i in tile:
        print(i, tile[i][1], tile[i][2], tile[i][3])
    print("\n", np.arange(1, SIZE * SIZE + 1).reshape(SIZE, SIZE), "\n")

seed()
print_status(TILE)
