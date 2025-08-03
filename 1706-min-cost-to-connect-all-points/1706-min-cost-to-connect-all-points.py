class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        visited = set()
        min_heap = [(0, 0)]
        total_cost = 0
        while len(visited) < n:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            total_cost += cost
            visited.add(node)
            for nei_cost, nei in adj[node]:
                heapq.heappush(min_heap, ((nei_cost, nei)))
        return total_cost