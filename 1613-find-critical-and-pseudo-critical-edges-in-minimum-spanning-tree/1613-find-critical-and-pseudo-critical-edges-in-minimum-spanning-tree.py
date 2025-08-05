class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.components = n
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.par[px] = py
        self.components -= 1
        return True
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        critical, pseudo = [], []
        for i in range(len(edges)):
            edges[i].append(i) # v1, v2, w, i
        edges.sort(key = lambda x: x[2])
        uf = UnionFind(n)
        mst_weight = 0
        for v1, v2, w, _ in edges:
            if uf.union(v1, v2):
                mst_weight += w
        for v1, v2, w, i in edges:
            uf = UnionFind(n)
            weight = 0
            for v3, v4, w2, j in edges:
                if i != j and uf.union(v3, v4):
                    weight += w2
            if uf.components != 1 or weight > mst_weight:
                critical.append(i)
                continue
            uf = UnionFind(n)
            weight = w
            uf.union(v1, v2)
            for v3, v4, w2, j in edges:
                if i != j and uf.union(v3, v4):
                    weight += w2
            if uf.components == 1 and weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]
        