class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        valid_splits = 0
        left_sum, right_sum = 0, sum(nums)

        for i, num in enumerate(nums):
            right_sum -= num
            left_sum += num

            if left_sum >= right_sum and i < len(nums) - 1:
                valid_splits += 1
        return valid_splits