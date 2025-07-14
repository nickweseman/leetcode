class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        max_rows = 0
        chosen_cols = set()
        num_cols = len(matrix[0])
        num_rows = len(matrix)
        def covered_rows() -> int:
            count = 0
            for r in range(num_rows):
                covered = True
                for c in range(num_cols):
                    if matrix[r][c] == 1 and c not in chosen_cols:
                        covered = False
                        break
                if covered:
                    count += 1
            return count
        def dfs(col_index, columns_left):
            nonlocal max_rows
            if columns_left == 0:
                count = covered_rows()
                max_rows =  max(max_rows, count)
                return
            if col_index == num_cols:
                return
            chosen_cols.add(col_index)
            dfs(col_index + 1, columns_left - 1)
            chosen_cols.remove(col_index)
            dfs(col_index + 1, columns_left)
        dfs(0, numSelect)
        return max_rows

        