class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = math.inf
        left = right = 0
        while right < len(nums):
            if right - left + 1 > k:
                left += 1
            if right - left + 1 == k:
                min_diff = min(min_diff, nums[right] - nums[left])
            right += 1
        return min_diff
