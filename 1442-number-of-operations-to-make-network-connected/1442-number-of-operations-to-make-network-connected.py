class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            nonlocal networks
            px, py = find(x), find(y)
            if px == py:
                return False
            else:
                if rank[px] < rank[py]:
                    parent[px] = py
                    rank[py] += rank[px]
                else:
                    parent[py] = px
                    rank[px] += rank[py]
                return True
        networks = n
        for a, b in connections:
            if union(a, b):
                networks -= 1
        return networks - 1 if len(connections) >= n - 1 else -1
