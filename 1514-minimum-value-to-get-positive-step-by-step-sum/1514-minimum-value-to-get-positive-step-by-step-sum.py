class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = min_prefix_sum = 0

        for num in nums:
            prefix_sum += num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
        return 1 - min_prefix_sum