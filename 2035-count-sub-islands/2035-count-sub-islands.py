class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid1), len(grid1[0])
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid2[r][c] == 0:
                return
            grid2[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and grid1[r][c] == 0:
                    dfs(r, c)
        subislands = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    dfs(r, c)
                    subislands += 1
        return subislands