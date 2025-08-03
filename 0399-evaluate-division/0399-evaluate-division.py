class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, equation in enumerate(equations):
            a, b = equation
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            visited = set()
            queue = collections.deque()
            queue.append((src, 1))
            visited.add(src)
            while queue:
                for _ in range(len(queue)):
                    node, value = queue.popleft()
                    if node == target:
                        return value
                    for nei, val in adj[node]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append((nei, value * val))
            return -1
        result = []
        for q in queries:
            result.append(bfs(q[0], q[1]))
        return result
