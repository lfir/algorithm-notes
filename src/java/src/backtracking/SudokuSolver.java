package backtracking;

/**
 * Solves a 9x9 sudoku that has one or more solutions. -1 represents the empty cell.
 * Time complexity: O(9^E) where E is equal to the number of empty cells in the board.
 */
public class SudokuSolver {
    public static void solveSudoku(int[][] board) {
        solveAux(board);
    }

    static boolean solveAux(int[][] board) {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == -1) {
                    for (int d = 1; d <= 9; d++) {
                        if (isValidCell(board, r, c, d)) {
                            board[r][c] = d;
                            if (solveAux(board)) return true;
                            board[r][c] = -1;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    static boolean isValidCell(int[][] board, int r, int c, int d) {
        for (int row = 0; row < 9; row++) {
            if (board[row][c] == d) {
                return false;
            }
        }
        for (int col = 0; col < 9; col++) {
            if (board[r][col] == d) {
                return false;
            }
        }
        for (int row = (r / 3) * 3; row < (r / 3 + 1) * 3; row++) {
            for (int col = (c / 3) * 3; col < (c / 3 + 1) * 3; col++) {
                if (board[row][col] == d) {
                    return false;
                }
            }
        }
        return true;
    }
}
