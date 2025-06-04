class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = right = 0
        max_avg = float('-inf')
        window = 0

        while right < len(nums):
            window += nums[right]

            while right - left >= k:
                window -= nums[left]
                left += 1
            
            #print(f"{window=} {right=} {left=} {right - left + 1 = }")
            window_size = right - left + 1
            if window_size == k:
                window_avg = window / window_size
                max_avg = max(window_avg, max_avg)
            
            right += 1
        return max_avg