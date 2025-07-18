class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        def backtrack(index):
            if index == len(nums):
                result.append(path.copy())
                return
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()
            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1
            backtrack(index + 1)
        backtrack(0)
        return result