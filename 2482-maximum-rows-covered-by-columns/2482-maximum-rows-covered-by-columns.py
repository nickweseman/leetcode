class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        covered_cols = set()
        max_covered = 0
        def covered_rows():
            count = 0
            for r in range(rows):
                covered = True
                for c in range(cols):
                    if matrix[r][c] == 1 and c not in covered_cols:
                        covered = False
                        break
                if covered:
                    count += 1
            return count
        def backtrack(index, num_covered):
            nonlocal max_covered
            if index == cols or num_covered == numSelect:
                max_covered = max(max_covered, covered_rows())
                return
            covered_cols.add(index)
            backtrack(index + 1, num_covered + 1)
            covered_cols.remove(index)
            backtrack(index + 1, num_covered)
        backtrack(0, 0)
        return max_covered
