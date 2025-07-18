class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        max_rows = 0
        num_cols = len(matrix[0])
        num_rows = len(matrix)
        cols_selected = [False] * num_cols
        def get_covered_rows():
            count = 0
            for i in range(num_rows):
                row_covered = True
                for j in range(num_cols):
                    if matrix[i][j] == 1 and not cols_selected[j]:
                        row_covered = False
                if row_covered:
                    count += 1
            return count
        def backtrack(index, cols_left):
            nonlocal max_rows
            if cols_left < 0:
                return
            if index == num_cols:
                if cols_left == 0:
                    max_rows = max(max_rows, get_covered_rows())
                return
            cols_selected[index] = True
            backtrack(index + 1, cols_left - 1)
            cols_selected[index] = False
            backtrack(index + 1, cols_left)
        backtrack(0, numSelect)
        return max_rows