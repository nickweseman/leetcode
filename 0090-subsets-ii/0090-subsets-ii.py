class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        path = []
        result = []
        def backtrack(index):
            if index == n:
                result.append(path.copy())
                return
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()
            while index + 1 < n and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1)
        backtrack(0)
        return result