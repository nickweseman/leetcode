class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        total = 0
        for i, num in enumerate(nums):
            total += num
            result[i] = total
        return result