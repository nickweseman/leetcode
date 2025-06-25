class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        valid_splits = 0
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)

        for i in range(0, n - 1):
            num = nums[i]
            right_sum -= num
            left_sum += num

            if left_sum >= right_sum:
                valid_splits += 1
        return valid_splits