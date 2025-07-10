class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        left_even, right_even = 0, sum(nums[i] for i in range(0, len(nums), 2))
        left_odd, right_odd = 0, sum(nums[i] for i in range(1, len(nums), 2))
        num_fair = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                right_even -= num
            else:
                right_odd -= num
            if left_even + right_odd == left_odd + right_even:
                num_fair += 1
            if i % 2 == 0:
                left_even += num
            else:
                left_odd += num
        return num_fair