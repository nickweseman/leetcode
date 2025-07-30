class UnionFind:
    def __init__(self, edges):
        n = len(edges) + 1
        self.parent = list(range(n))
        self.rank = [1] * n
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 != p2:
            if self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
                self.rank[p2] += self.rank[p1]
            else:
                self.parent[p2] = p1
                self.rank[p1] += self.rank[p2]
            return True
        else:
            return False
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(edges)
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge