## Algorithm notes
Personal notes and Python implementations of some interesting algorithms I've not found clearly
presented elsewhere so far.

#### Notes
- Running files that import modules from the project's packages and reside in sub-directories
directly instead of via main.py, requires adding the src directory to PYTHONPATH first

      export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

- Auxiliary classes UtilsChart, UtilsPDA imported in main.py require package
[utils_tabdata](https://github.com/Asta1986/utils_tabdata)

