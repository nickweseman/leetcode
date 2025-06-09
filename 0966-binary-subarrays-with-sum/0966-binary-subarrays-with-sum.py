class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(my_goal: int) -> int:
            window = 0
            left = right = 0
            subarrays = 0

            while right < len(nums):
                window += nums[right]
                while left <= right and window > my_goal:
                    window -= nums[left]
                    left += 1
                subarrays += right - left + 1
                right += 1
            return subarrays
        return helper(goal) - helper(goal - 1)

        