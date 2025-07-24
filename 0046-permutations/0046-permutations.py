class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        result = []
        path = []
        def backtrack(index):
            if len(path) == n:
                result.append(path.copy())
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(i + 1)
                used[i] = False
                path.pop()
        backtrack(0)
        return result