class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = [(0, 0)]
        n = len(points)
        visited = set()
        total_cost = 0
        while len(visited) < n:
            dist, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            x1, y1 = points[i]
            visited.add(i)
            total_cost += dist
            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]
                    dist2 = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist2, j))
        return total_cost