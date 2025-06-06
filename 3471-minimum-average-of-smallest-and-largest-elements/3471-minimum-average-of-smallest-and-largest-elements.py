class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        min_avg = float('inf')
        left, right = 0, len(nums) - 1

        nums.sort()

        while left < right:
            min_avg = min(min_avg, (nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return min_avg