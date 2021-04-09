#### Examples with 4x4, 6x6 and 9x9 Sudokus:

    from backtracking.sudoku_solver import solve

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

    # For a grid with multiple solutions set g9[8][6] and g9[8][7] to None.
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
