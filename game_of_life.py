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
from setup_board import initiate_board, seed_board
from check_update import check, update, print_status, check_store, endgame, resolve

def game_of_life(size, seed):
    ''' main engine '''
    # create initial board space and set relationships
    board = initiate_board(size)
    seed_board(seed)
    print("\n", "Generation: 0")
    print_status(board)

    # start engine
    running = True
    infinite = False
    gen = 1
    while running and not infinite:
        print("\n", "Generation: ", gen)
        gen += 1
        # check, update, log json, print, test
        check(board)
        update(board)
        print_status(board)
        infinite = check_store(board)
        running = endgame(board)

    #resolve with some stats
    resolve(board)

# scenario 1: death
# SEED = [8, 9, 13, 17, 18]

# scenario 2: stasis
# SEED = [7, 8, 12, 13]

# scenario 3: homeostatic
SEED = [12, 13, 14]

game_of_life(5, SEED)
