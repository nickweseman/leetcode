class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        edges_changed = 0
        for a, b in connections:
            graph[a].append((b, 1)) # original direction
            graph[b].append((a, 0)) # synthetic direction
        visited = set()
        def dfs(city):
            nonlocal edges_changed
            visited.add(city)
            for nei, direction in graph[city]:
                if nei not in visited:
                    edges_changed += direction
                    dfs(nei)
        dfs(0)
        return edges_changed