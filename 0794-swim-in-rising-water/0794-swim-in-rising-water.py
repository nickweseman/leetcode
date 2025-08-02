class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set([(0, 0)])
        min_heap = [(grid[0][0], 0, 0)] # time/max height, r, c
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            if r == rows - 1 and c == cols - 1:
                return time
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                heapq.heappush(min_heap, (max(time, grid[nr][nc]), nr, nc))