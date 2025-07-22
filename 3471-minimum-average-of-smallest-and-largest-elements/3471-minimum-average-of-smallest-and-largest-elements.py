class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        min_avg = math.inf
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            min_avg = min((nums[left] + nums[right]) / 2, min_avg)
            left += 1
            right -= 1
        return min_avg