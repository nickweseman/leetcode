class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if node == destination:
                return True
            visited.add(node)
            for nei in graph[node]:
                if dfs(nei):
                    return True
            return False
        return dfs(source)

            