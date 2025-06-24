class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        grand_sum = right_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum = grand_sum - left_sum
            left_sum += num
            if left_sum == right_sum:
                return i
        return -1