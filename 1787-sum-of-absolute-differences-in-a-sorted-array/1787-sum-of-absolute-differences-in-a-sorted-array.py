class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = []
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)

        for i, num in enumerate(nums):
            right_sum -= num

            left_total = (num * i) - left_sum
            right_total = right_sum - (n - i - 1) * num
            result.append(left_total + right_total)
            
            left_sum += num
        return result