class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        candidate_ks = [k for k in nums if -k in nums]
        return max(candidate_ks, default=-1)