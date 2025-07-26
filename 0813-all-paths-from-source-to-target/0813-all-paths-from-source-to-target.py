class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        result = []
        path = [0]
        def backtrack(index):
            if index == len(graph) - 1:
                result.append(path.copy())
                return
            for neighbor in graph[index]:
                path.append(neighbor)
                backtrack(neighbor)
                path.pop()
        backtrack(0)
        return result