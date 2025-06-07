class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left = right = 0
        window = 0

        while right < len(nums):
            window += nums[right]

            while window >= target:
                min_length = min(min_length, right - left + 1)
                window -= nums[left]
                left += 1
            right += 1
        return 0 if min_length == float('inf') else min_length