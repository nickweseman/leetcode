class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        def dfs(r, c):
            nonlocal max_area
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
                return 0
            area = 1
            grid[r][c] = 0
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            max_area = max(max_area, area)
            return area
        for r in range(rows):
            for c in range(cols):
                dfs(r, c)
        return max_area