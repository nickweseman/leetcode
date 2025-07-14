class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(index):
            if index == len(nums):
                result.append(nums.copy())
                return
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                dfs(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        dfs(0)
        return result
        