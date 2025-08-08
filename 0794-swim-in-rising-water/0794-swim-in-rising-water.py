class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        min_heap = [(grid[0][0], 0, 0)] # t, r, c
        visited = set()
        max_time = 0
        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            max_time = max(max_time, time)
            if (r, c) == (rows - 1, cols - 1):
                return max_time
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                heapq.heappush(min_heap, (grid[nr][nc], nr, nc))