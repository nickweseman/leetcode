class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, current_xor_sum):
            if index == len(nums):
                return current_xor_sum
            include_sum = dfs(index + 1, current_xor_sum ^ nums[index])
            exclude_sum = dfs(index + 1, current_xor_sum)
            return include_sum + exclude_sum
        return dfs(0, 0)