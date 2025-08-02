class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = collections.defaultdict(list) # list of (cost, node)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2) # manhattan distance
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        # Prim's
        result = 0
        visited = set()
        min_heap = [(0, 0)] # cost, point
        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            result += cost
            visited.add(point)
            for nei_cost, nei in adj[point]:
                if nei not in visited:
                    heapq.heappush(min_heap, (nei_cost, nei))
        return result

        