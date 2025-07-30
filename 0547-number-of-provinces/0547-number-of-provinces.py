class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = provinces = len(isConnected)
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            nonlocal provinces
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                provinces -= 1
        for r in range(n):
            for c in range(n):
                if r != c and isConnected[r][c] == 1:
                    union(r, c)
        return provinces
