class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        edge_count = collections.defaultdict(int)
        for a, b in edges:
            edge_count[a] += 1
            edge_count[b] += 1
        leaves_queue = collections.deque()
        for node, freq in edge_count.items():
            if freq == 1:
                leaves_queue.append(node)
        while n > 2:
            for _ in range(len(leaves_queue)):
                leaf = leaves_queue.popleft()
                n -= 1
                for nei in adj[leaf]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves_queue.append(nei)
        return list(leaves_queue)

        