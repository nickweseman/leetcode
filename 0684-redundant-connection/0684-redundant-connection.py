class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = list(range(n))
        rank = [1] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu != pv:
                if rank[pu] < rank[pv]:
                    parent[pu] = pv
                    rank[pu] += rank[pv]
                else:
                    parent[pu] = pv
                    rank[pu] += rank[pv]
                return True
            else:
                return False
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge