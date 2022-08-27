## Algorithm notes
Personal notes and Python and Java implementations of some interesting algorithms I've not found clearly
presented elsewhere so far.

#### Notes
- Running files (such as graphs/maze_solver.py) that import modules from the project's packages (i.e. utils.py) and
reside in sub-directories, directly instead of via main.py, requires adding the src directory to PYTHONPATH first

      export PYTHONPATH="${PYTHONPATH}:$(pwd)/src/python"

- Auxiliary classes UtilsChart, UtilsPDA imported in main.py require package
[utils_tabdata](https://github.com/Asta1986/utils_tabdata)
