class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        result = []
        def backtrack(node):
            if node == len(graph) - 1:
                result.append(path.copy())
                return
            for i in graph[node]:
                path.append(i)
                backtrack(i)
                path.pop()
        backtrack(0)
        return result