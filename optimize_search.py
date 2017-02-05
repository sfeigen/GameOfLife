''' optimizing search'''

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
    corners = [1, size, (size * (size-1)) + 1, size*size]
    left = (size + 1) % size

    for i in range(1, (size*size) + 1):
        if i > (size) and i <= size * (size-1):
            if i % size == left:
                # left: up, down, right
                print(i, "left")
            elif i % size == 0:
                # right: up, down, left
                print(i, "right")
            else:
                #top, bottom, l, r
                print(i, "interior")
        elif i in corners:
            # corners
            print(i, "corner")
        elif i < size:
            # top
            print(i, "top")
        elif i > (size * (size-1) + 1):
            # bottom
            print(i, "bottom")

def main(size):
    '''testing optimal search'''
    #create board
    create_board(size)

    #run alg
    alg(size)

main(5)
