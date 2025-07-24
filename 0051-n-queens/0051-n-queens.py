class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diags = set() # r - c
        neg_diags = set() # r + c
        grid = [[] for _ in range(n)]
        for row in grid:
            for _ in range(n):
                row.append(".")
        result = []
        def backtrack(r):
            if r == n:
                grid_entry = []
                for i in range(n):
                    row = []
                    for j in range(n):
                        row.append(grid[i][j])
                    grid_entry.append("".join(row))
                result.append(grid_entry)
                return
            for c in range(n):
                if c not in cols and r - c not in pos_diags and r + c not in neg_diags:
                    cols.add(c)
                    pos_diags.add(r - c)
                    neg_diags.add(r + c)
                    grid[r][c] = "Q"
                    backtrack(r + 1)
                    cols.remove(c)
                    pos_diags.remove(r - c)
                    neg_diags.remove(r + c)
                    grid[r][c] = "."
        backtrack(0)
        return result