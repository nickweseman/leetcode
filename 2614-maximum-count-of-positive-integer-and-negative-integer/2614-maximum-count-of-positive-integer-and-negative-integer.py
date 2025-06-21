class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = bisect.bisect_left(nums, 1)
        neg = bisect.bisect_left(nums, 0)

        return max(len(nums) - pos, neg)