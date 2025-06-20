class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numset = set(nums)
        candidate_ks = [k for k in nums if k > 0 and -k in numset]
        return max(candidate_ks) if candidate_ks else -1
