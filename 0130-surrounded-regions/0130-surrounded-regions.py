class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != "O":
                return
            board[r][c] = "T"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and r in (0, rows - 1) or c in (0, cols - 1):
                    dfs(r, c)
        # 2. Capture surrounded regions (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # 3.  Uncapture unsurrounded regions (T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        

        