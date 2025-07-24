class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        left = right = 0
        subarrays = 0
        while right < len(nums):
            product *= nums[right]
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            subarrays += right - left + 1
            right += 1
        return subarrays