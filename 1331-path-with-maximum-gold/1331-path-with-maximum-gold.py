class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def backtrack(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return 0
            if grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            gold_from_neighbors = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                gold_from_neighbors = max(gold_from_neighbors, backtrack(r + dr, c + dc))
            visited.remove((r, c))
            return grid[r][c] + gold_from_neighbors
        max_gold = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    max_gold = max(max_gold, backtrack(r, c))
        return max_gold