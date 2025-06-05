class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        left = right = 0
        min_diff = float('inf')

        nums.sort()

        while right < len(nums):
            if right - left > k - 1:
                left += 1

            if right - left == k - 1:
                min_diff = min(min_diff, nums[right] - nums[left])
            right += 1
        return min_diff
        