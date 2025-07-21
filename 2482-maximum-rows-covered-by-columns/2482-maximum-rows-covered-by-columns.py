class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        max_rows = 0
        cols_selected = [False] * COLS
        def get_covered_rows() -> int:
            count = 0
            for r in range(ROWS):
                covered = True
                for c in range(COLS):
                    if matrix[r][c] == 1 and not cols_selected[c]:
                        covered = False
                if covered:
                    count += 1
            return count
        def backtrack(index, cols_left):
            nonlocal max_rows
            if index == COLS:
                if cols_left == 0:
                    max_rows = max(max_rows, get_covered_rows())
                return
            if cols_left > 0:
                cols_selected[index] = True
                backtrack(index + 1, cols_left - 1)
                cols_selected[index] = False
            backtrack(index + 1, cols_left)
        backtrack(0, numSelect)
        return max_rows