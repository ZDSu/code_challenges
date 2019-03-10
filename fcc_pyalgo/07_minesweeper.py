"""
Write a function that wil take 3 arguments:
- bombs = list of bomb locations
- rows
- columns

mine_sweeper([[0,0], [1,2]], 3, 4)
translates to:
- bomb at row index 0, column index 0
- bomb at row index 1, column index 2
- 3 rows (0, 1, 2)
- 4 columns (0, 1, 2, 3)
[2 bomb location coordinates in a 3x4 matrix]

we should return a 3 x 4 array (-1) = bomb
(ends up deleting this stuff because he changed the original bomb location from [0,1] to [1,2])  [[-1, -1, 1, 0], [2, 2, 1, 0], the 2 bombs means 2 bombs in surrounding cells [1,0] knows [0,0] and [0,1] have ...?... 0,0,0,0]]

Comment: why doesn't he take in the rows and columns first and then the bombs since number of bombs can vary but there is also only one row and one column argument.

Visualization: https://goo.gl/h4h4ax

similar: https://leetcode.com/problems/minesweeper/
"""

def minesweeper(bombs, rows, cols):
    # build field using 2 for loops in one line, place 0 in each cell
    field = [[0 for i in range(cols)] for j in range(rows)]
    # bomb locations change from 0 to -1
    for location in bombs:
        (bomb_row, bomb_col) = location
        field[bomb_row][bomb_col] = -1

    # go through rows and columns to find bombs (check numerical value of cell); can put these directly in for loop, it's separate just for visualization
        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            for j in col_range:
                if 0 <= i < rows and 0 <= j < cols and field[i][j] != -1:
                    field[i][j] += 1

    return field

print(minesweeper([[0, 0], [1, 2]], 3, 4))
