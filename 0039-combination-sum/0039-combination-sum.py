class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        comb = []
        def dfs(i, remaining_target):
            if remaining_target == 0:
                result.append(comb.copy())
                return
            if i == len(candidates) or remaining_target < 0:
                return
            comb.append(candidates[i])
            dfs(i, remaining_target - candidates[i])
            comb.pop()
            dfs(i + 1, remaining_target)
        dfs(0, target)
        return result