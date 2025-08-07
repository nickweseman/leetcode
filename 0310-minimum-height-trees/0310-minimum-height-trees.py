class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        leaves_queue = collections.deque()
        edge_count = collections.Counter()
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        for node, neighbors in adj.items():
            edge_count[node] = len(neighbors)
            if edge_count[node] == 1:
                leaves_queue.append(node)
        while leaves_queue and n > 2:
            for _ in range(len(leaves_queue)):
                leaf_node = leaves_queue.popleft()
                n -= 1
                for nei in adj[leaf_node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves_queue.append(nei)
        return list(leaves_queue)