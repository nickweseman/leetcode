class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect.bisect_right(nums, -1)
        pos = bisect.bisect_right(nums, 0)

        return max(neg, len(nums) - pos)