''' optimizing search'''

BOARD = {}
STATE = ['Untouched', 'Populated', 'Underpopulated', 'Overpopulated']
STATE = list(enumerate(STATE))

def create_board(size):
    ''' helper method to create inital, blank board '''
    for i in range(1, (size*size) + 1):
        BOARD[i] = [i, False, STATE[0], []]

def find_neighbors(size):
    ''' change defaults to reflect BOARD relationships '''
    #corner helper variables
    corners = [1, size, (size * (size-1)) + 1, len(BOARD)]
    lowerleft = (size * (size-1)) + 1
    lowerright = len(BOARD)
    left = (size + 1) % size

    run_interior, run_corners = True, True
    for i in range(1, (len(BOARD)) + 1):
        if run_interior:
            for i in range(0, size-2):
                for j in range(size+2, size*2):
                    tile = (i*size) + j
                    BOARD[tile][3].append(tile-1)
                    BOARD[tile][3].append(tile+1)
                    BOARD[tile][3].append(tile+(size-1))
                    BOARD[tile][3].append(tile+size)
                    BOARD[tile][3].append(tile+(size+1))
                    BOARD[tile][3].append(tile-(size-1))
                    BOARD[tile][3].append(tile-size)
                    BOARD[tile][3].append(tile-(size+1))
                    run_interior = False

        elif i % size == left and i < size * (size-1) + 1:
            # left: up, down, rt
            BOARD[i][3].append(i-size)
            BOARD[i][3].append(i-size+1)
            BOARD[i][3].append(i + 1)
            BOARD[i][3].append(i + size)
            BOARD[i][3].append((i + size) + 1)

        elif i in corners:
            # corners
            if run_corners:
                BOARD[1][3].append(2)
                BOARD[1][3].append(size+1)
                BOARD[1][3].append(size+2)
                BOARD[size][3].append(size-1)
                BOARD[size][3].append(size*2)
                BOARD[size][3].append((size*2) - 1)
                BOARD[lowerleft][3].append(lowerleft+1)
                BOARD[lowerleft][3].append(lowerleft-size)
                BOARD[lowerleft][3].append((lowerleft-size) + 1)
                BOARD[lowerright][3].append(lowerright-1)
                BOARD[lowerright][3].append(lowerright-size)
                BOARD[lowerright][3].append((lowerright-size) - 1)
                run_corners = False

        elif i % size == 0 and i <= size * (size-1):
            BOARD[i][3].append(i + size)
            BOARD[i][3].append(i + (size - 1))
            BOARD[i][3].append(i - 1)
            BOARD[i][3].append(i - size)
            BOARD[i][3].append(i - (size + 1))

        elif i < size:
            # top
            BOARD[i][3].append(i+(size-1))
            BOARD[i][3].append(i+size)
            BOARD[i][3].append(i+(size+1))
            BOARD[i][3].append(i-1)
            BOARD[i][3].append(i+1)

        else:
            # bottom
            BOARD[i][3].append(i-(size-1))
            BOARD[i][3].append(i-size)
            BOARD[i][3].append(i-(size+1))
            BOARD[i][3].append(i-1)
            BOARD[i][3].append(i+1)

def seed_board(seed):
    ''' seed '''
    #seed board
    for i in BOARD:
        if i in seed:
            BOARD[i][1] = True
            BOARD[i][2] = 1

def initiate_board(size):
    '''initiate board'''
    #create board
    create_board(size)
    #find neighbors
    find_neighbors(size)

    return BOARD
