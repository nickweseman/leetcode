class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [(0, 0)]
        visited = set()
        total_cost = 0
        while len(visited) < n:
            dist, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            total_cost += dist
            x1, y1 = points[i]
            visited.add(i)
            for j in range(n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(min_heap, (dist, j))
        return total_cost
