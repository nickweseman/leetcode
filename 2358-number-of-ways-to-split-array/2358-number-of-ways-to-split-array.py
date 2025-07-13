class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        num_splits = 0
        for i in range(len(nums) - 1):
            right_sum -= nums[i]
            left_sum += nums[i]
            if left_sum >= right_sum:
                num_splits += 1
        return num_splits