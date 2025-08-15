class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        result = []
        n = len(graph)
        def backtrack(node):
            if node == n - 1:
                result.append(path.copy())
                return
            for nei in graph[node]:
                path.append(nei)
                backtrack(nei)
                path.pop()
        backtrack(0)
        return result