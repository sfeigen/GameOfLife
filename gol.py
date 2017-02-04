'''
Conway's Game of Life
Sam Feigenbaum <sfeigen@live.com>

Key:
[] = Alive
## = Dead

Rule 1: Any cell with less than 2 living neighbors, dies.
Rule 2: Any living cell with 2 or 3 living neighbors, stays alive.
 __ __ __        __ __ __
|[]|__|__|      |##|__|__|
|__|[]|__|  ->  |__|[]|__|
|__|__|[]|      |__|__|##|
Living:  3      Living: 1

Rule 3: Any cell with greater than 3 neighbors, dies.
 __ __ __        __ __ __
|__|[]|__|      |__|[]|__|
|[]|[]|[]|  ->  |[]|##|[]|
|__|[]|__|      |__|[]|__|
Living:  5      Living:  4

Rule 4: Any cell with exactly 3 neighbors, lives.
 __ __ __        __ __ __
|[]|__|[]|      |##|[]|##|
|__|[]|__|  ->  |__|[]|__|
|__|__|__|      |__|__|__|
Living:  3      Living:  2

Example of all 4 in effect:
 __ __ __        __ __ __
|[]|__|[]|      |[]|[]|##|
|[]|[]|__|  ->  |[]|##|__|
|[]|__|__|      |[]|__|__|


End Conditions:
1. No living squares,           extinction.
2. No moving squares,           stasis.
3. Infinite repeating pattern,  symbiosis.
'''

import numpy as np

STATE = []

def make_grid(x_axis, y_axis):
    '''set up grid'''
    return np.zeros([x_axis, y_axis])

def save_state(habitat):
    '''save the matrix state'''
    STATE.append(habitat)

def check(habitat):
    '''check neighbors // find a smart way to check the neighbors'''
    neighbors = []
    for i in range(1, len(habitat)-1):
        neighbors.append(habitat[i, i-1])
        neighbors.append(habitat[i, i+1])
        neighbors.append(habitat[i-1, 1])
        neighbors.append(habitat[i+1, 1])
        neighbors.append(habitat[i-1, i-1])
        neighbors.append(habitat[i-1, i+1])
        neighbors.append(habitat[i+1, i-1])
        neighbors.append(habitat[i+1, i+1])

    return neighbors

def game_of_life():
    '''main engine'''

    # habitat = make_grid(3, 3)
    habitat = np.matrix([[1, 4, 6, 9], [4, 7, 2, 3], [2, 6, 7, 1], [1, 3, 7, 0]])
    print(habitat)
    generation = 0
    running = True

    while running:
        print(check(habitat))

        save_state(habitat)
        generation += 1
        running = False

game_of_life()
