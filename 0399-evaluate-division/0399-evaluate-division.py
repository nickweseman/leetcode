class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, equation in enumerate(equations):
            a, b = equation
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        def bfs(src, tgt):
            if src not in adj or tgt not in adj:
                return -1.0
            if src == tgt:
                return 1.0
            queue = collections.deque([(src, 1.0)])
            visited = {src}
            while queue:
                for _ in range(len(queue)):
                    node, val = queue.popleft()
                    if node == tgt:
                        return val
                    for nei, nei_val in adj[node]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append((nei, nei_val * val))
            return -1.0
        return [bfs(q[0], q[1]) for q in queries]
        