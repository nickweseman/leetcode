class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        min_avg_diff = math.inf
        min_index = -1
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)

        for i, num in enumerate(nums):
            right_sum -= num
            left_sum += num

            left_avg = left_sum // (i + 1)
            right_avg = right_sum // (n - i - 1) if n - i - 1 != 0 else 0
            diff = abs(left_avg - right_avg)
            if diff < min_avg_diff:
                min_avg_diff = diff
                min_index = i
        return min_index