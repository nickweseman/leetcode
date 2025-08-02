class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        edge_count = {}
        leaves_queue = collections.deque()
        for src, neighbors in adj.items():
            neighbors_count = len(neighbors)
            if neighbors_count == 1:
                leaves_queue.append(src)
            edge_count[src] = neighbors_count
        while leaves_queue:
            if n <= 2:
                return list(leaves_queue)
            for i in range(len(leaves_queue)):
                node = leaves_queue.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves_queue.append(nei)
        
        