''' check and update functions '''
from search_optimized import board_tiles
import numpy as np 

# debug
SIZE = 5
TILE = board_tiles(SIZE)
print(np.arange(1, SIZE * SIZE + 1).reshape(SIZE, SIZE), "\n")

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

print_status(TILE)
