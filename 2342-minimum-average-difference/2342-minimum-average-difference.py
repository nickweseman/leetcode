class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum, right_sum = 0, sum(nums)
        
        min_index, min_diff = 0, float('inf')
        
        for i, num in enumerate(nums):
            left_sum += num
            right_sum -= num
            
            left_avg = left_sum // (i + 1)
            right_avg = 0 if i == n - 1 else right_sum // (n - i - 1)
            
            current_diff = abs(left_avg - right_avg)
            
            if current_diff < min_diff:
                min_diff = current_diff
                min_index = i
        return min_index