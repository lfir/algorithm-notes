def cheapest_path_bottomup(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    auxtable = [[float('inf') for _ in range(columns+1)] for _ in range(rows+1)]
    auxtable[0][1] = 0
    auxtable[1][0] = 0

    for i in range(1, rows+1):
        for j in range(1, columns+1):
            auxtable[i][j] = matrix[i-1][j-1] + min(auxtable[i-1][j], auxtable[i][j-1])

    return auxtable[rows][columns]

def cheapest_path_topdown(auxtable, matrix, endrowidx, endcolidx):
    currcost = None
    if endrowidx < 0 or endcolidx < 0:
        currcost = float('inf')
    elif endrowidx == 0 and endcolidx == 0:
        currcost = matrix[0][0]
    elif auxtable[endrowidx][endcolidx] is not None:
        currcost = auxtable[endrowidx][endcolidx]
    else:
        auxtable[endrowidx][endcolidx] = matrix[endrowidx][endcolidx] + \
            min(
            cheapest_path_topdown(auxtable, matrix, endrowidx-1, endcolidx),
            cheapest_path_topdown(auxtable, matrix, endrowidx, endcolidx-1)
            )
        currcost = auxtable[endrowidx][endcolidx]

    return currcost

def cheapest_path(matrix):
    """Returns the total cost of the cheapest path
    from the starting point [0, 0] to the end point [m, n].
    Valid moves from any cell [i, j] are [i + 1, j] (go down) or [i, j + 1] (go right).
    Preconditions: The matrix received is not empty and each cell contains a number.
    """
    rows = len(matrix)
    columns = len(matrix[0])
    auxtable = [[None for _ in range(columns)] for _ in range(rows)]
    auxtable[0][0] = 0

    return cheapest_path_topdown(auxtable, matrix, rows-1, columns-1)
