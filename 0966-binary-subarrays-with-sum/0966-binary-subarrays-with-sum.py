class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def numSubarrays(goal_):
            subarrays = 0
            left = right = 0
            total = 0
            while right < len(nums):
                total += nums[right]
                while left <= right and total > goal_:
                    total -= nums[left]
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return numSubarrays(goal) - numSubarrays(goal - 1)