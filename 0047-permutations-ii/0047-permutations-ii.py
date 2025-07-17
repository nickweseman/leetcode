class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        n = len(nums)
        used = [False] * n
        def backtrack(index):
            if index == n:
                result.append(path.copy())
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(index + 1)
                used[i] = False
                path.pop()
        backtrack(0)
        return result