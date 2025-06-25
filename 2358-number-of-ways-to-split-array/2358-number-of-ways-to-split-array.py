class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        valid_splits = 0
        left_sum, right_sum = 0, sum(nums)

        for i in range(len(nums) - 1):
            right_sum -=  nums[i]
            left_sum +=  nums[i]

            if left_sum >= right_sum:
                valid_splits += 1
        return valid_splits