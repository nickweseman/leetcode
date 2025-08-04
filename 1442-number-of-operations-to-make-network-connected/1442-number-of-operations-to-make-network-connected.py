class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n))
        networks = n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            nonlocal networks
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                networks -= 1
        for a, b in connections:
            union(a, b)
        return networks - 1 if len(connections) >= n - 1 else -1