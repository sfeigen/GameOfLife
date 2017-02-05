''' optimizing search'''
from time import time

#benchmark
T0 = time()

TILE = {}
STATE = ['Untouched', 'Populated', 'Underpopulated', 'Overpopulated']
STATE = list(enumerate(STATE))

def create_board(size):
    ''' create board '''
    for i in range(1, (size*size) + 1):
        TILE[i] = [i, False, STATE[0], []]
    return size

def alg(size):
    '''smarter search'''
    create_board(size)

    #corner helper variables
    corners = [1, size, (size * (size-1)) + 1, size*size]
    lowerleft = (size * (size-1)) + 1
    lowerright = size * size
    left = (size + 1) % size

    run_interior, run_corners = True, True
    for i in range(1, (size*size) + 1):
        if run_interior:
            for i in range(0, size-2):
                for j in range(size+2, size*2):
                    num = (i*size) + j
                    TILE[num][3].append(num-1)
                    TILE[num][3].append(num+1)
                    TILE[num][3].append(num+(size-1))
                    TILE[num][3].append(num+size)
                    TILE[num][3].append(num+(size+1))
                    TILE[num][3].append(num-(size-1))
                    TILE[num][3].append(num-size)
                    TILE[num][3].append(num-(size+1))
                    run_interior = False

        elif i % size == left and i < size * (size-1) + 1:
            # left: up, down, rt
            TILE[i][3].append(i-size)
            TILE[i][3].append(i-size+1)
            TILE[i][3].append(i + 1)
            TILE[i][3].append(i + size)
            TILE[i][3].append((i + size) + 1)

        elif i in corners:
            # corners
            if run_corners:
                TILE[1][3].append(2)
                TILE[1][3].append(size+1)
                TILE[size][3].append(size-1)
                TILE[size][3].append(size*2)
                TILE[lowerleft][3].append(lowerleft+1)
                TILE[lowerleft][3].append(lowerleft-size)
                TILE[lowerright][3].append(lowerright-1)
                TILE[lowerright][3].append(lowerright-size)
                run_corners = False

        elif i % size == 0 and i <= size * (size-1):
            TILE[i][3].append(i + size)
            TILE[i][3].append(i + (size - 1))
            TILE[i][3].append(i - 1)
            TILE[i][3].append(i - size)
            TILE[i][3].append(i - (size + 1))

        elif i < size:
            # top
            TILE[i][3].append(i+(size-1))
            TILE[i][3].append(i+size)
            TILE[i][3].append(i+(size+1))
            TILE[i][3].append(i-1)
            TILE[i][3].append(i+1)

        else:
            # bottom
            TILE[i][3].append(i-(size-1))
            TILE[i][3].append(i-size)
            TILE[i][3].append(i-(size+1))
            TILE[i][3].append(i-1)
            TILE[i][3].append(i+1)

def main(size):
    '''testing optimal search'''
    #create board
    create_board(size)

    #run alg
    alg(size)

main(3)
for i in TILE:
    print(i, TILE[i][3])
#benchmark
T1 = time()
print(T1 - T0, "seconds.")
