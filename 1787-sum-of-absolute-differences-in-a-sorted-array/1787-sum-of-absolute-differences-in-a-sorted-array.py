class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 0, sum(nums)
        result = []
        n = len(nums)
        for i, num in enumerate(nums):
            left_sum += num
            right_sum -= num
            curr_left = num * (i + 1) - left_sum
            curr_right = right_sum - num * (n - (i + 1))
            print(curr_left, curr_right)
            result.append(curr_left + curr_right)
        return result