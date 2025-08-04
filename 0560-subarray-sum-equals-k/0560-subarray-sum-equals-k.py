class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        total = 0
        prefix_sums = {0 : 1} # empty subarray
        for num in nums:
            total += num
            diff = total - k
            subarrays += prefix_sums.get(diff, 0)
            prefix_sums[total] = 1 + prefix_sums.get(total, 0)
        return subarrays