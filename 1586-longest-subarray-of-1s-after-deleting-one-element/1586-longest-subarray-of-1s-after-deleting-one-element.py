class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window = 0 # num zeroes
        left = right = 0
        max_size = 0

        while right < len(nums):
            if nums[right] == 0:
                window += 1
            while window > 1:
                if nums[left] == 0:
                    window -= 1
                left += 1
            max_size = max(max_size, right - left)
            right += 1
        return max_size # - 1 if max_size == window else max_size