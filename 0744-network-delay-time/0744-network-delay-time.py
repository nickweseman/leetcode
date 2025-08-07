class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))
        min_heap = [(0, k)]
        visited = set()
        time = 0
        while min_heap:
            w, v = heapq.heappop(min_heap)
            if v in visited:
                continue
            visited.add(v)
            if len(visited) == n:
                return w
            for nei_weight, nei in adj[v]:
                heapq.heappush(min_heap, (nei_weight + w, nei))
        return -1
