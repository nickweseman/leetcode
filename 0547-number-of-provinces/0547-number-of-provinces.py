class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        provinces = n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return True
            else:
                return False
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    if union(i, j):
                        provinces -= 1
        return provinces