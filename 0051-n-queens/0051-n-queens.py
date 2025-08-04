class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diags = set() # r - c
        neg_diags = set() # r + c
        board = [["."] * n for _ in range(n)]
        result = []
        def backtrack(r):
            if r == n:
                copy = []
                for row in range(n):
                    copy.append("".join(board[row]))
                result.append(copy.copy())
                return
            for c in range(n):
                if c not in cols and r - c not in pos_diags and r + c not in neg_diags:
                    board[r][c] = "Q"
                    cols.add(c)
                    pos_diags.add(r - c)
                    neg_diags.add(r + c)
                    backtrack(r + 1)
                    board[r][c] = "."
                    cols.remove(c)
                    pos_diags.remove(r - c)
                    neg_diags.remove(r + c)
        backtrack(0)
        return result