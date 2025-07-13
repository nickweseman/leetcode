class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_xor_sum = 0
        def dfs(i, current_xor):
            nonlocal total_xor_sum
            if i == len(nums):
                total_xor_sum += current_xor
                return
            dfs(i + 1, current_xor ^ nums[i])
            dfs(i + 1, current_xor)
        dfs(0, 0)
        return total_xor_sum