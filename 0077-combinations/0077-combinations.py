class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        comb = []
        def dfs(i, remaining_k):
            if remaining_k == 0:
                result.append(comb.copy())
                return
            if i > n:
                return
            comb.append(i)
            dfs(i + 1, remaining_k - 1)
            comb.pop()
            dfs(i + 1, remaining_k)
        dfs(1, k)
        return result