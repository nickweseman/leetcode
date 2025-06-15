class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(g: int) -> int:
            left = right = 0
            total = 0
            subarrays = 0

            while right < len(nums):
                total += nums[right]

                while left <= right and total > g:
                    total -= nums[left]
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return helper(goal) - helper(goal - 1)