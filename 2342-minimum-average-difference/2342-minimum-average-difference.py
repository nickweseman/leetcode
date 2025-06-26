class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        min_avg_diff = math.inf
        min_avg_index = -1
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)

        for i, num in enumerate(nums):
            right_sum -= num
            left_sum += num

            left_avg = left_sum // (i + 1)
            right_avg = right_sum // (n - i - 1) if n - i - 1 != 0 else 0
            current_diff = abs(left_avg - right_avg)
            if current_diff < min_avg_diff:
                min_avg_diff = current_diff
                min_avg_index = i
        return min_avg_index