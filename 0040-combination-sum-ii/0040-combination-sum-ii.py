class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        comb = []
        n = len(candidates)
        def dfs(i, remaining_target):
            if remaining_target == 0:
                result.append(comb.copy())
                return
            if i == n or remaining_target < 0:
                return
            comb.append(candidates[i])
            dfs(i + 1, remaining_target - candidates[i])
            comb.pop()
            next_i = i + 1
            while next_i < n and candidates[next_i] == candidates[i]:
                next_i += 1
            dfs(next_i, remaining_target)
        dfs(0, target)
        return result