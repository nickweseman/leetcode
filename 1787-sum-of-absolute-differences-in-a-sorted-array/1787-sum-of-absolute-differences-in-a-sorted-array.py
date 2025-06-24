class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        n = len(nums)
        result = []

        for i, num in enumerate(nums):
            left_total = i * num - left_sum
            right_total = (total - left_sum - num) - (n - 1 - i) * num

            result.append(left_total + right_total)
            left_sum += num
        return result