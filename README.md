### algorithms-notes
Personal notes and Python implementations of some algorithms I've not found clearly presented 
elsewhere so far.

#### Notes
Running files that import modules from the project's packages and reside in sub-directories 
(i. e. src/dynamic_programming/paths_in_grid.py), requires adding the src directory to PYTHONPATH first

    export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
