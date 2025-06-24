class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = min_value = 0

        for i, num in enumerate(nums):
            total += num
            min_value = min(min_value, total)
        
        return 1 - min_value