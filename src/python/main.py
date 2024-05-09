from backtracking.wolf_goat_and_cabbage import solve as solvewgc
from dynamic_programming.cheapest_path_in_matrix import cheapest_path
from dynamic_programming.paths_in_grid import grid_paths

# move to separate files with examples
print("Solution for Wolf, Goat and Cabbage problem:", solvewgc([False, False, False, False], []))

print(cheapest_path([[1, 2, 2], [1, 3, 4]]))

print(grid_paths(6, 8))
