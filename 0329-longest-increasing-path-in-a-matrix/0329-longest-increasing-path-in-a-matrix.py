class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(matrix), len(matrix[0])
        dp = [[-1] * cols for _ in range(rows)]
        def dfs(r, c, prev_value):
            if not (0 <= r < rows and 0 <= c < cols) or matrix[r][c] <= prev_value:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            max_nei = 1
            for dr, dc in dirs:
                max_nei = max(max_nei, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            dp[r][c] = max_nei
            return dp[r][c]
        lip = 0
        for r in range(rows):
            for c in range(cols):
                lip = max(lip, dfs(r, c, -1))
        return lip