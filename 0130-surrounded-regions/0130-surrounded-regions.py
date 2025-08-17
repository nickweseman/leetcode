class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != "O":
                return
            board[r][c] = "T"
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"

        