class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n # 0 - unvisited, 1 - visiting, 2 - visited and safe
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            return True
        for i in range(n):
            dfs(i)
        return [i for i, val in enumerate(state) if val == 2]