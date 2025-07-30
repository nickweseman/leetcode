class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            else:
                parent[px] = py
                return True
        networks = n
        for a, b in connections:
            if union(a, b):
                networks -= 1
        return networks - 1 if len(connections) >= n - 1 else -1
