class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = collections.deque()
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))
        while queue:
            r, c, turns = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                fresh -= 1
                if fresh == 0:
                    return turns + 1
                queue.append((nr, nc, turns + 1))
        return 0 if fresh == 0 else -1