class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(grid)
        visited = set()
        def oob(r, c):
            if not (0 <= r < n and 0 <= c < n) or (r, c) in visited:
                return True
            return False
        def dfs(r, c):
            if oob(r, c) or grid[r][c] == 0:
                return
            visited.add((r, c))
            for dr, dc in directions:
                if oob(r + dr, c + dc):
                    continue
                dfs(r + dr, c + dc)
        def bfs():
            queue = collections.deque(visited)
            turns = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if oob(nr, nc):
                            continue
                        visited.add((nr, nc))
                        if grid[nr][nc] == 1:
                            return turns
                        queue.append((nr, nc))
                turns += 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()