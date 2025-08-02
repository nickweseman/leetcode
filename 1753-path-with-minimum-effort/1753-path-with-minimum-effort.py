class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_heap = [(0, 0, 0)] # diff, r, c
        visited = set()
        while min_heap:
            max_diff, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return max_diff
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in visited:
                    continue
                diff = abs(heights[r][c] - heights[nr][nc])
                heapq.heappush(min_heap, (max(max_diff, diff), nr, nc))
            