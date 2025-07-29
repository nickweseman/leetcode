class UnionFind:
    def __init__(self):
        self.parent = list(range(26))
        self.rank = [1] * 26
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 != p2:
            if p1 < p2:
                self.parent[p2] = p1
                self.rank[p1] += self.rank[p2]
            else:
                self.parent[p1] = p2
                self.rank[p2] += self.rank[p1]
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for i in range(len(s1)):
            s1_idx = ord(s1[i]) - ord('a')
            s2_idx = ord(s2[i]) - ord('a')
            uf.union(s1_idx, s2_idx)
        result = []
        for c in baseStr:
            c_idx = ord(c) - ord('a')
            replace_idx = uf.find(c_idx)
            result.append(chr(replace_idx + ord('a')))
        return "".join(result)
        