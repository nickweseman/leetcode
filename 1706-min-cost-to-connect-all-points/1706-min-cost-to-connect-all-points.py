class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = [(0, 0)] # distance, point
        visited = set()
        n = len(points)
        total_cost = 0
        while len(visited) < n:
            distance, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            x1, y1 = points[i]
            total_cost += distance
            for j in range(n):
                if i != j and j not in visited:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, j))
        return total_cost