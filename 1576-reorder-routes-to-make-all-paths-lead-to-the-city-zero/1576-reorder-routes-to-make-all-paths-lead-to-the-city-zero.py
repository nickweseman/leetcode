class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1)) # original road
            graph[v].append((u, 0)) # synthetic road
        visited = set()
        reorders = 0
        def dfs(city):
            nonlocal reorders
            visited.add(city)
            for neighbor, direction in graph[city]:
                if neighbor not in visited:
                    reorders += direction
                    dfs(neighbor)
        dfs(0)
        return reorders
