class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
                return 0
            gold = grid[r][c]
            grid[r][c] = 0
            max_gold_from_neighbors = 0
            for dr, dc in directions:
                max_gold_from_neighbors = max(max_gold_from_neighbors, dfs(r + dr, c + dc))
            grid[r][c] = gold
            return gold + max_gold_from_neighbors
        max_gold = 0
        for r in range(rows):
            for c in range(cols):
                max_gold = max(max_gold, dfs(r, c))
        return max_gold