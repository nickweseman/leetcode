class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        n = len(candidates)
        def backtrack(index, sum_so_far):
            if index == n:
                if sum_so_far == target:
                    result.append(path.copy())
                return
            if sum_so_far > target:
                return
            path.append(candidates[index])
            backtrack(index, sum_so_far + candidates[index])
            path.pop()
            backtrack(index + 1, sum_so_far)
        backtrack(0, 0)
        return result