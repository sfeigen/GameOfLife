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
from check_update import check, update, endgame, print_status

STATE = []

def game_of_life(size, seed):
    ''' main engine '''
    # create initial board space and set relationships
    board = initiate_board(size)
    seed_board(seed)
    print("\n", "Generation: 0")
    print_status(board)

    # start engine
    running = True
    gen = 1
    while running:
        print("\n", "Generation: ", gen)
        gen += 1
        # check, update, print, test
        check(board)
        update(board)
        print_status(board)
        running = endgame(board)

# SEED = [5, 10, 11, 12]
SEED = [8, 9, 13, 17, 18]
game_of_life(5, SEED)
