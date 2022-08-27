from utils_tabdata import UtilsChart, UtilsPDA

from backtracking.sudoku_solver import solve as solvesudoku
from graphs.maze_solver import solve as solvemaze

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
UtilsPDA.print_numtable(solvesudoku(g9).pop())

m0 = [
    ["S"],
    ["E"]
]
print(solvemaze(m0))

