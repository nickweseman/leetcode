class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        left_even, right_even = 0, sum(nums[i] for i in range(0, len(nums), 2))
        left_odd, right_odd = 0, sum(nums[i] for i in range(1, len(nums), 2))
        
        num_fairs = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                right_even -= num
            else:
                right_odd -= num
            
            new_even_sum = left_even + right_odd
            new_odd_sum = left_odd + right_even
            if new_even_sum == new_odd_sum:
                num_fairs += 1

            if i % 2 == 0:
                left_even += num
            else:
                left_odd += num
        return num_fairs
