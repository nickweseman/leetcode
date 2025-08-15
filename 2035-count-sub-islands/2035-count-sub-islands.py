class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid2[r][c] == 0:
                return
            grid2[r][c] = 0
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        for r in range(rows):
            for c in range(cols):
                if grid1[r][c] == 0 and grid2[r][c] == 1:
                    dfs(r, c)
        subislands = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    dfs(r, c)
                    subislands += 1
        return subislands