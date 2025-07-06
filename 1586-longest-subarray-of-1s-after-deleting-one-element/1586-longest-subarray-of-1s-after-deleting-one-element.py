class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroes = 0
        left = right = 0
        longest = 0
        while right < len(nums):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            longest = max(longest, right - left)
            right += 1
        return longest