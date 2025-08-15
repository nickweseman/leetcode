class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rolling_sum = 0
        subarrays = 0
        prefix_count = collections.defaultdict(int)
        prefix_count[0] = 1
        for num in nums:
            rolling_sum += num
            if prefix_count[rolling_sum - k] > 0:
                subarrays += prefix_count[rolling_sum - k]
            prefix_count[rolling_sum] += 1
        return subarrays