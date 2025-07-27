class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(start):
            visited.add(start)
            for end in range(n):
                if isConnected[start][end] == 1 and end not in visited:
                    dfs(end)
        provinces = 0
        for start in range(n):
            if start not in visited:
                dfs(start)
                provinces += 1
        return provinces