class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        par = list(range(n))
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                par[px] = py
                return True
            else:
                return False
        for a, b in edges:
            if not union(a, b):
                return [a, b]