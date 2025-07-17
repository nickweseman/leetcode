class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        min_diff, min_index = math.inf, -1
        n = len(nums)
        for i, num in enumerate(nums):
            right_sum -= num
            left_sum += num
            left_total = left_sum // (i + 1)
            right_total = right_sum // (n - i - 1) if n - i - 1 != 0 else 0
            diff = abs(left_total - right_total)
            if diff < min_diff:
                min_diff = diff
                min_index = i
        return min_index
