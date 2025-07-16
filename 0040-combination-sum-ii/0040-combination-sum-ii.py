class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        comb = []
        candidates.sort()
        used = [False] * len(candidates)
        def dfs(index, remaining_target):
            if remaining_target == 0:
                result.append(comb.copy())
                return
            if index == len(candidates) or remaining_target < 0:
                return
            if index == 0 or candidates[index] != candidates[index - 1] or used[index - 1]:
                comb.append(candidates[index])
                used[index] = True
                dfs(index + 1, remaining_target - candidates[index])
                comb.pop()
                used[index] = False
            dfs(index + 1, remaining_target)
        dfs(0, target)
        return result