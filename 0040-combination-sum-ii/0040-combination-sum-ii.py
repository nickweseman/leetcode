class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        def dfs(index, remaining_target):
            if remaining_target == 0:
                result.append(path.copy())
                return
            if index == len(candidates) or remaining_target < 0:
                return
            path.append(candidates[index])
            dfs(index + 1, remaining_target - candidates[index])
            path.pop()
            next_i = index + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[next_i - 1]:
                next_i += 1
            dfs(next_i, remaining_target)
        dfs(0, target)
        return result