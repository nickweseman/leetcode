class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        dp = [[0] * cols for _ in range(rows)]
        def dfs(r, c, prev_val):
            if not (0 <= r < rows and 0 <= c < cols) or matrix[r][c] <= prev_val:
                return 0
            if dp[r][c] != 0:
                return dp[r][c]
            best = 1
            for dr, dc in dirs:
                best = max(best, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            dp[r][c] = best
            return best
        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c, -1))
        return ans