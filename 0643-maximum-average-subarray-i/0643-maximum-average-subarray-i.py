class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        window = 0
        left = right = 0

        while right < len(nums):
            window += nums[right]

            if right - left + 1 > k:
                window -= nums[left]
                left += 1
           
            if right - left + 1 == k:
                max_avg = max(max_avg, window / (right - left + 1))
            right += 1
        return max_avg
        