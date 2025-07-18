class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        result = []
        path = []
        def backtrack(index):
            if index == len(nums):
                result.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(index + 1)
                path.pop()
                used[i] = False
        backtrack(0)
        return result