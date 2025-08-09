class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        # dp = [[0] * cols for _ in range(rows)] # dp[r][c] -> longest increasing path from (r, c)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        @functools.lru_cache(None)
        def dfs(r, c, prev_val):
            if not (0 <= r < rows and 0 <= c < cols) or matrix[r][c] <= prev_val:
                return 0
            # if dp[r][c] != 0:
            #     return dp[r][c]
            result = 1
            for dr, dc in directions:
                result = max(result, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            # dp[r][c] = result
            return result
        max_val = 0
        for r in range(rows):
            for c in range(cols):
                max_val = max(max_val, dfs(r, c, -1))
        return max_val
            

        