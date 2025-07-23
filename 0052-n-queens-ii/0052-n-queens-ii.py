class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diags = set() # (r - c)
        neg_diags = set() # (r + c)
        solutions = 0
        def backtrack(r):
            nonlocal solutions
            if r == n:
                solutions += 1
                return
            for c in range(n):
                if c not in cols and r - c not in pos_diags and r + c not in neg_diags:
                    cols.add(c)
                    pos_diags.add(r - c)
                    neg_diags.add(r + c)
                    backtrack(r + 1)
                    cols.remove(c)
                    pos_diags.remove(r - c)
                    neg_diags.remove(r + c)
        backtrack(0)
        return solutions