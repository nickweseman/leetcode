class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        left, right = 0, 1
        max_diff = float('-inf')

        while right < len(nums):
            if nums[left] < nums[right]:
                max_diff = max(max_diff, nums[right] - nums[left])
            else:
                left = right
            right += 1
        return -1 if max_diff == float('-inf') else max_diff