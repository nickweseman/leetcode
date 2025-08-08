class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(heights), len(heights[0])
        min_heap = [(0, 0, 0)] # diff, r, c
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
                diff = abs(heights[r][c] - heights[nr][nc])
                heapq.heappush(min_heap, (diff, nr, nc))
