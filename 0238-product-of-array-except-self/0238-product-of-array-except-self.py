class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left_sum = 1
        for i in range(n):
            result[i] *= left_sum
            left_sum *= nums[i]
        right_sum = 1
        for i in reversed(range(n)):
            result[i] *= right_sum
            right_sum *= nums[i]
        return result
            
