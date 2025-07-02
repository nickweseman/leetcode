class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix_product = 1
        for i in range(n):
            answer[i] *= prefix_product
            prefix_product *= nums[i]
        
        suffix_product = 1
        for i in reversed(range(n)):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
        return answer