class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def backtrack(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS) or grid[r][c] == 0:
                return 0
            original_gold = grid[r][c]
            grid[r][c] = 0
            gold_from_neighbors = 0
            for dr, dc in directions:
                gold_from_neighbors = max(gold_from_neighbors, backtrack(r + dr, c + dc))
            grid[r][c] = original_gold
            return original_gold + gold_from_neighbors
        max_gold = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    max_gold = max(max_gold, backtrack(r, c))
        return max_gold