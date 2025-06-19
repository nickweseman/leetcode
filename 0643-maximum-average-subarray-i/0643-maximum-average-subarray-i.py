class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        left = right = 0
        max_avg = float('-inf')

        while right < len(nums):
            total += nums[right]

            if right - left + 1 > k:
                total -= nums[left]
                left += 1
            if right - left + 1 == k:
                max_avg = max(max_avg, total / k)
            right += 1
        return max_avg