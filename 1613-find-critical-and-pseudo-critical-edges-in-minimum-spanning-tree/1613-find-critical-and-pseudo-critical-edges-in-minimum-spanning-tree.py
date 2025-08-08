class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[px] = py
        self.components -= 1
        return True
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key = lambda x : x[2])
        critical, pseudo = [], []
        uf = UnionFind(n)
        mst_weight = 0
        for a, b, w, _ in edges:
            if uf.union(a, b):
                mst_weight += w
        for a1, b1, w1, i in edges:
            # Make a mst without the edge
            uf = UnionFind(n)
            weight = 0
            for a2, b2, w2, j in edges:
                if i != j and uf.union(a2, b2):
                    weight += w2
            if uf.components != 1 or weight > mst_weight:
                critical.append(i)
                continue
            # Make a mst with the forced edge
            uf = UnionFind(n)
            uf.union(a1, b1)
            weight = w1
            for a2, b2, w2, j in edges:
                if i != j and uf.union(a2, b2):
                    weight += w2
            if uf.components == 1 and weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]