class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))
        total_cost = 0
        visited = set()
        def dfs(node):
            nonlocal total_cost
            visited.add(node)
            for nei, direction in adj[node]:
                if nei not in visited:
                    total_cost += direction
                    dfs(nei)
        dfs(0)
        return total_cost
