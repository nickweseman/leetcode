class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        min_total = 0
        for i, num in enumerate(nums):
            total += num
            min_total = min(min_total, total)
        return 1 - min_total