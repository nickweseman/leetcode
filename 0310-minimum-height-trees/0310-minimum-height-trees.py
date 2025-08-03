class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        leaves = collections.deque()
        edge_count = {}
        for node, neighbors in adj.items():
            edge_count[node] = len(neighbors)
            if edge_count[node] == 1:
                leaves.append(node)
        while n > 2:
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves.append(nei)
        return list(leaves)