def validcellvalue(x, y, n, grid, size):
    # Validate row and column.
    for i in range(size):
        if grid[x][i] == n or grid[i][y] == n:
            return False
    
    blockrows = 2
    blockcols = 2
    if size == 6:
        blockcols += 1
    if size == 9:
        blockrows += 1
        blockcols += 1
    inix = (x // blockrows) * blockrows
    iniy = (y // blockcols) * blockcols

    # Validate block. 
    for i in range(blockrows):
        for j in range(blockcols):
            if grid[inix+i][iniy+j] == n:
                return False
     
    return True

def solveaux(grid, solutions):
    size = len(grid)
    # For each row.
    for x in range(size):
        # For each column.
        for y in range(size):
            # If target cell is empty.
            if grid[x][y] is None:
                # For each possible value the cell can take.
                for n in range(1, size+1):
                    # If the value is valid.
                    if validcellvalue(x, y, n, grid, size):
                        grid[x][y] = n
                        # Process the remaining cells.
                        solveaux(grid, solutions)
                        # Backtrack.
                        grid[x][y] = None
                return

    solutions.add(tuple(tuple(row) for row in grid))

def solve(grid):
    """Returns a set with the solutions for a 4x4, a 6x6 or a 9x9 Sudoku."""
    solutions = set()

    solveaux(grid, solutions)

    return solutions


"""Examples:
g4 = [
    [None, None, None, 3],
    [3, None, 2, None],
    [None, 4, None, 1],
    [1, None, None, None]
]

g6 = [
    [None, None, None, None, 4, None],
    [None, None, None, None, None, 2],
    [4, 3, None, None, 6, 1],
    [1, 5, None, None, 3, 4],
    [3, None, None, None, None, None],
    [None, 1, None, None, None, None],
]

For a grid with multiple solutions set g9[8][6] and g9[8][7] to None.
g9 = [
    [None, 1, 2, None, None, 6, 5, 8, 9],
    [6, 7, None, None, None, None, None, None, 2],
    [None, 8, 4, 1, None, 5, 6, 3, None],
    [4, 3, 8, 2, 5, 9, 1, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, 7, 8, 1, 4, 3, 9, 5],
    [None, 9, 6, 5, None, 1, 7, 2, None],
    [7, None, None, None, None, None, None, 5, 1],
    [5, 4, 1, 7, None, None, 8, 6, None]
]

print_numtable(solve(g9).pop())
"""
