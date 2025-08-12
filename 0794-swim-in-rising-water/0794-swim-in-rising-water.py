class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_heap = [(grid[0][0], 0, 0)]
        visited = set()
        max_diff = 0
        while min_heap:
            diff, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            max_diff = max(max_diff, diff)
            if (r, c) == (rows - 1, cols - 1):
                return max_diff
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                print(nr, nc)
                heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
        