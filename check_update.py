''' check and update functions '''
import numpy as np
from search_optimized import board_tiles

# debug
SIZE = 5
TILE = board_tiles(SIZE)
ALIVE = []
STATE = ['Untouched', 'Populated', 'Underpopulated', 'Overpopulated']
STATE = list(enumerate(STATE))

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
def seed_test():
    ''' seed '''
    seed = [7, 9, 12, 13, 14, 17, 18, 21]
    # seed = [0]
    for i in TILE:
        if i in seed:
            TILE[i][1] = True

def check():
    ''' checks the state of the board '''
    # debug
    seed_test()

    # Conway's logic.
    count = 0
    dead_count = 0
    for tile in TILE:
        for nbr in TILE:
            # select tiles and check if neighbor is alive
            if TILE[tile][1] and TILE[nbr][1] and tile in TILE[nbr][3]:
                count += 1
            elif TILE[tile][1] is False and TILE[nbr][1] and tile in TILE[nbr][3]:
                dead_count += 1
        # apply Conway.
        if count > 1 and count < 4:
            TILE[tile][2] = STATE[1]
            count = 0
        elif count == 1:
            TILE[tile][2] = STATE[2]
            count = 0
        elif count > 3:
            TILE[tile][2] = STATE[3]
            count = 0
        # wake the dead, Conway.
        elif dead_count == 3:
            TILE[tile][2] = STATE[1]
        count = 0
        dead_count = 0

def update():
    ''' updates the state of the board, and ends if depletion '''
    end = 0
    for tile in TILE:
        if TILE[tile][2] == STATE[1]:
            TILE[tile][1] = True
        if TILE[tile][2] == STATE[0] or TILE[tile][2] == STATE[2] or TILE[tile][2] == STATE[3]:
            TILE[tile][1] = False
            end += 1
    # check for endgame by depletion.
    if end == len(TILE):
        end = 0
        endgame()
    else:
        end = 0

def endgame():
    ''' checks for end condition and returns false '''
    print("Endgame")
    return False

def print_status(tile):
    ''' print status '''
    for i in tile:
        print(i, tile[i][1], tile[i][2], tile[i][3])
    print("\n", np.arange(1, SIZE * SIZE + 1).reshape(SIZE, SIZE), "\n")

# debug
check()
update()
print_status(TILE)
