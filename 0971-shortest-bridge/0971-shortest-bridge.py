class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        def invalid(r, c):
            return not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited
        def dfs(r, c):
            if invalid(r, c) or grid[r][c] == 0:
                return
            visited.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        def bfs():
            queue = collections.deque(visited)
            turns = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if invalid(nr, nc):
                            continue
                        if grid[nr][nc] == 1:
                            return turns
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                turns += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()