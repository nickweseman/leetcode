class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numset = set(nums)

        candidates = [k for k in nums if k > 0 and -k in numset]

        return max(candidates) if candidates else -1
        