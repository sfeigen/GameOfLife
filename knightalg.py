
import numpy as np

SELECT = []
TEMP = []
SEARCH_PATTERN = {}

def search_range(size):
    ''' builds matrix to generate keys '''
    return np.arange(size).tolist()

def load_neighbors():
    ''' creates keys'''
    temp_grid = GRID[:]
    while len(SEARCH_PATTERN) <= 3:
        for row in range(temp_grid[0], temp_grid[0]+3):
            for col in range(temp_grid[0], temp_grid[0]+3):
                TEMP.append([row, col])
        key = TEMP.pop(4)
        SEARCH_PATTERN[str(key)] = TEMP[:]
        TEMP.clear()
        temp_grid.pop(0)

GRID = search_range(5)
load_neighbors()

print(np.arange(25).reshape(5, 5))
print(SEARCH_PATTERN)
