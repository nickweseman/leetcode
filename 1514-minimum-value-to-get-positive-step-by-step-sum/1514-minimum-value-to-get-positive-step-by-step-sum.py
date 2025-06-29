class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = summ = 0

        for num in nums:
            summ += num
            min_sum = min(min_sum, summ)
        return 1 - min_sum