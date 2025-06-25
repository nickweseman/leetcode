class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = lowest_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            lowest_sum = min(lowest_sum, prefix_sum)
        return 1 - lowest_sum