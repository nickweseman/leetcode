class Solution:
    def totalNQueens(self, n: int) -> int:
        num_possible = 0
        cols = set()
        pos_diags = set() # (r - c)
        neg_diags = set() # (r + c)
        def backtrack(r):
            nonlocal num_possible
            if r == n:
                num_possible += 1
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
        return num_possible