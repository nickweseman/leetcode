class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = collections.defaultdict(int)
        prefix_sums[0] = 1
        total = 0
        subarrays = 0
        for num in nums:
            total += num
            subarrays += prefix_sums[total - k]
            prefix_sums[total] += 1
        return subarrays