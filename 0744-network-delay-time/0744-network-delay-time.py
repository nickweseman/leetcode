class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))
        min_heap = [(0, k)]
        time = 1
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            time = max(time, weight)
            for nei_weight, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (weight + nei_weight, nei))
        return time if len(visited) == n else -1