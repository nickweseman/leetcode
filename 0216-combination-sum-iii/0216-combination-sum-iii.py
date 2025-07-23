class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []
        def backtrack(index, sum_so_far):
            if index > 10:
                return
            if len(path) == k:
                if sum_so_far == n:
                    result.append(path.copy())
                return
            path.append(index)
            backtrack(index + 1, sum_so_far + index)
            path.pop()
            backtrack(index + 1, sum_so_far)
        backtrack(1, 0)
        return result
