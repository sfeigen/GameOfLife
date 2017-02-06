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
from setup_board import initiate_board
from check_update import check, update, endgame, print_status

STATE = []

def game_of_life(size):
    ''' main engine '''
    # create initial board space and set relationships
    tiles = initiate_board(size)

    # start engine
    running = True
    while running:
        #show state
        print_status(tiles)
        #check and log state
        check(tiles)
        #update state
        update(tiles)
        #check the condition
        running = endgame(tiles)

    # debug

game_of_life(5)
