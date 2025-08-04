class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        min_heap = [(0, k)]
        visited = set()
        time = 0
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            time = max(time, weight)
            for nei, nei_weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (weight + nei_weight, nei))
        return time if len(visited) == n else -1

        