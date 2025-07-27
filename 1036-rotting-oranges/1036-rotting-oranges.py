class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh = time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != 1:
                        continue
                    queue.append((nr, nc))   
                    fresh -= 1
                    grid[nr][nc] = 2               
            time += 1
        return -1 if fresh > 0 else time