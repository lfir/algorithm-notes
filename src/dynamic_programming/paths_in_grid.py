def grid_paths_recursive(rows, columns):
    """Returns the number of distinct paths from the starting point of a grid
    [0, 0] to the end point [m, n].
    Valid moves from any cell [i, j] are [i + 1, j] (go down) or [i, j + 1] (go right).
    Preconditions: rows > 0 and columns > 0.

    Example of function call:
    print(grid_paths_recursive(4, 5))
    """
    if rows == 1 or columns == 1:
        return 1
    else:
        return grid_paths_recursive(rows-1, columns) + grid_paths_recursive(rows, columns-1)

def grid_paths(rows, columns):
    """
    Example of function call:
    print(grid_paths(6, 8))
    """
    auxtable = [[None for _ in range(columns)] for _ in range(rows)]
    auxtable[0][0] = 1

    res = grid_paths_topdown(auxtable, rows-1, columns-1)
    print_numtable(auxtable)

    return res

def grid_paths_bottomup(rows, columns):
    auxtable = [[None for _ in range(columns)] for _ in range(rows)]
    # Base cases.
    for i in range(columns):
        auxtable[0][i] = 1 
    for i in range(rows):
        auxtable[i][0] = 1 

    for i in range(1, rows):
        for j in range(1, columns):
            auxtable[i][j] = auxtable[i-1][j] + auxtable[i][j-1]

    print_numtable(auxtable)
    return auxtable[rows-1][columns-1]

def grid_paths_topdown(auxtable, endrowidx, endcolidx):
    if endrowidx == 0 or endcolidx == 0:
      return 1

    if auxtable[endrowidx][endcolidx] is not None:
      return auxtable[endrowidx][endcolidx]

    auxtable[endrowidx][endcolidx] = grid_paths_topdown(auxtable, endrowidx-1, endcolidx) +\
        grid_paths_topdown(auxtable, endrowidx, endcolidx-1)

    return auxtable[endrowidx][endcolidx]
