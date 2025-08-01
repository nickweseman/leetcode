class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh = 0
        rotten_queue = collections.deque()
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    visited.add((r, c))
                    rotten_queue.append((r, c))
        while rotten_queue:
            for _ in range(len(rotten_queue)):
                r, c = rotten_queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in visited or grid[nr][nc] != 1:
                        continue
                    visited.add((nr, nc))
                    num_fresh -= 1
                    if num_fresh == 0:
                        return time + 1
                    rotten_queue.append((nr, nc))
            time += 1
        return 0 if num_fresh == 0 else -1