class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(index, remaining_target):
            if remaining_target == 0:
                result.append(path.copy())
                return
            if remaining_target < 0 or index == len(candidates):
                return
            path.append(candidates[index])
            backtrack(index, remaining_target - candidates[index])
            path.pop()
            backtrack(index + 1, remaining_target)
        backtrack(0, target)
        return result