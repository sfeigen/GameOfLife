''' check and update functions '''
from search_optimized import board_tiles
import numpy as np

# debug
SIZE = 5
TILE = board_tiles(SIZE)
ALIVE = []
STATE = ['Untouched', 'Populated', 'Underpopulated', 'Overpopulated']
STATE = list(enumerate(STATE))

# Seed Config. 1
# Try and find better searching mech.
# __ __ __ __ __
#|__|__|__|__|__|
#|__|07|__|09|__|
#|__|12|13|14|__|
#|__|17|18|__|__|
#|__|__|__|__|__|

def seed():
    ''' seed '''
    seeds = [7, 9, 12, 13, 14, 17, 18]
    for i in TILE:
        if i in seeds:
            TILE[i][1] = True
            TILE[i][2] = STATE[1]

def check():
    ''' checks the state of the board '''
    # debug
    seed()

    # check for True tiles.
    for i in TILE:
        for j in TILE:
            # select alive tiles, check to see if
            if TILE[i][1] and TILE[j][1] and i in TILE[j][3]:
                print("Overlap ", "Neighbor", i, j)

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

# debug
print_status(TILE)
check()
