class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited, cycle = set(), set()
        n = len(graph)
        output = []
        adj = collections.defaultdict(list)
        for i, neighbors in enumerate(graph):
            for nei in neighbors:
                adj[i].append(nei)
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            visited.add(node)
            return True
        for node in range(n):
            if dfs(node):
                output.append(node)
        return output
                