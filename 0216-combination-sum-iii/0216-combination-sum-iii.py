class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        comb = []
        def dfs(i, remaining_n):
            if len(comb) == k and remaining_n == 0:
                result.append(comb.copy())
                return
            if len(comb) == k or remaining_n < 0 or i > 9:
                return
            comb.append(i)
            dfs(i + 1, remaining_n - i)
            comb.pop()
            dfs(i + 1, remaining_n)
        dfs(1, n)
        return result