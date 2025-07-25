class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        used = [False] * n
        path = []
        result = []
        def backtrack(index, sum_so_far):
            if index == n:
                if sum_so_far == target:
                    result.append(path.copy())
                return
            if sum_so_far > target:
                return
            path.append(candidates[index])
            backtrack(index + 1, sum_so_far + candidates[index])
            path.pop()
            while index + 1 < n and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, sum_so_far)
        backtrack(0, 0)
        return result