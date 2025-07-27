class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))
        components = n
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            nonlocal components
            pi, pj = find(i), find(j)
            if pi != pj:
                parent[pj] = pi
                components -= 1
        for a, b in connections:
            union(a, b)
        return components - 1