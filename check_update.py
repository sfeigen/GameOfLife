''' check and update functions '''

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

def check(tiles):
    ''' checks the state of the board '''
    tiles = tiles

    # Conway's logic.
    count = 0
    dead_count = 0
    for tile in tiles:
        for nbr in tiles:
            # select live tiles and check if neighbor is alive
            if tiles[tile][1] and tiles[nbr][1] and tile in tiles[nbr][3]:
                count += 1
            # select dead tiles and check if neighbor is alive
            elif tiles[tile][1] is False and tiles[nbr][1] and tile in tiles[nbr][3]:
                dead_count += 1
            elif tiles[tile][1] and not tiles[nbr][1]:
                tiles[tile][2] = STATE[2]

        # apply Conway.
        if count == 2 or count == 3:
            tiles[tile][2] = STATE[1]
            count = 0
        elif count == 1:
            tiles[tile][2] = STATE[2]
            count = 0
        elif count > 3:
            tiles[tile][2] = STATE[3]
            count = 0
        # wake the dead, Conway.
        elif dead_count == 3:
            tiles[tile][2] = STATE[1]
        count = 0
        dead_count = 0
    return tiles

def update(tiles):
    ''' updates the state of the board, and ends if depletion '''
    for tile in tiles:
        if tiles[tile][2] == STATE[1]:
            tiles[tile][1] = True
        if tiles[tile][2] == STATE[0] or tiles[tile][2] == STATE[2] or tiles[tile][2] == STATE[3]:
            tiles[tile][1] = False
    return tiles

def endgame(tiles):
    ''' checks for end condition and returns false '''
    end = 0
    for i in tiles:
        if tiles[i][1] is False:
            end += 1
    if end == len(tiles):
        return False
    else:
        return True

def print_status(tiles):
    '''prints out status'''
    for i in tiles:
        print(i, " - ", tiles[i][1], tiles[i][2], tiles[i][3])
