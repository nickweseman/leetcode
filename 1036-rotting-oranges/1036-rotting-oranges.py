class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        time = 0
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    queue.append((row, col))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
