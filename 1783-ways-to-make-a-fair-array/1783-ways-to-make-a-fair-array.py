class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        left_even, right_even = 0, sum(nums[i] for i in range(0,n,2))
        left_odd, right_odd = 0, sum(nums[i] for i in range(1,n,2))
        num_fair = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                right_even -= num
            else:
                right_odd -= num

            current_even_sum = left_even + right_odd
            current_odd_sum = left_odd + right_even
            if current_even_sum == current_odd_sum:
                num_fair += 1

            if i % 2 == 0:
                left_even += num
            else:
                right_even += num
        return num_fair