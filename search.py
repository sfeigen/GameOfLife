''' game of life '''

TILE = {}
STATE = ['Untouched', 'Populated', 'Underpopulated', 'Overpopulated']
STATE = list(enumerate(STATE))

def create_board(size):
    ''' create board '''
    for i in range(1, (size*size)+1):
        TILE[i] = [i, False, STATE[0], []]
    return size

def neighbors_corners(size):
    ''' establish neighbors for corners '''
    #helper variables
    lowerleft = (size * (size-1)) + 1
    lowerright = size * size

    #Get Corners: UL, UR, LL, LR
    TILE[1][3].append(2)
    TILE[1][3].append(size+1)
    TILE[size][3].append(size-1)
    TILE[size][3].append(size*2)
    TILE[lowerleft][3].append(lowerleft+1)
    TILE[lowerleft][3].append(lowerleft-size)
    TILE[lowerright][3].append(lowerright-1)
    TILE[lowerright][3].append(lowerright-size)

def search_engine(size, low_range, high_range):
    ''' establish neighbors for top '''

    for i in range(low_range, high_range):
        #side to side
        TILE[i][3].append(i-1)
        TILE[i][3].append(i+1)

        #top
        if TILE[i][0] < size * (size - 1):
            TILE[i][3].append(i+(size-1))
            TILE[i][3].append(i+size)
            TILE[i][3].append(i+(size+1))

        #bottom
        if TILE[i][0] > size + 1:
            TILE[i][3].append(i-(size-1))
            TILE[i][3].append(i-size)
            TILE[i][3].append(i-(size+1))

        if i == size-1:
            #redefine upper bounds
            upper_range = (size * (size - 1)) + 1

            #left
            for i in range(size + 1, upper_range, size):
                TILE[i][3].append(i-size)
                TILE[i][3].append(i-size+1)
                TILE[i][3].append(i + 1)
                TILE[i][3].append(i + size)
                TILE[i][3].append((i + size) + 1)

            #right
            for i in range(size * 2, upper_range, size):
                TILE[i][3].append(i + size)
                TILE[i][3].append(i + (size - 1))
                TILE[i][3].append(i - 1)
                TILE[i][3].append(i - size)
                TILE[i][3].append(i - (size + 1))

def initialize_board(size):
    ''' iterates over helper methods to fill interior '''
    size = create_board(size)

    # establish corner neighbors
    neighbors_corners(size)

    #establish bottom boundary neighbors
    search_engine(size, 2, size)

    # iterate to row # size - 1
    for row in range(1, size):
        #helper variables
        low = (size * row) + 2
        high = (size * row) + (size)

        #iterate using adjusting low and high bounds
        search_engine(size, low, high)
