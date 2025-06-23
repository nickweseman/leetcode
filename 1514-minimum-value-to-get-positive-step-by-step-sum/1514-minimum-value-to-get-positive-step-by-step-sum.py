class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        left_sum = 0
        min_left_sum = float('inf')

        for num in nums:
            left_sum += num
            min_left_sum = min(min_left_sum, left_sum)
        return abs(min_left_sum) + 1 if min_left_sum < 0 else 1