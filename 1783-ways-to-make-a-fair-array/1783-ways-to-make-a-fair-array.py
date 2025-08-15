class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        left_even_sum, right_even_sum = 0, sum(num for i, num in enumerate(nums) if i % 2 == 0)
        left_odd_sum, right_odd_sum = 0, sum(num for i, num in enumerate(nums) if i % 2 == 1)
        num_fair = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                right_even_sum -= num
            else:
                right_odd_sum -= num
            curr_even_sum = left_even_sum + right_odd_sum
            curr_odd_sum = left_odd_sum + right_even_sum
            if curr_even_sum == curr_odd_sum:
                num_fair += 1
            if i % 2 == 0:
                left_even_sum += num
            else:
                left_odd_sum += num
        return num_fair
        