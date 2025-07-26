class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_val, max_val = -50_000, 50_000
        offset = -min_val
        size = max_val - min_val + 1
        buckets = [0] * size
        counts = collections.Counter(nums)
        for num, freq in counts.items():
            buckets[num + offset] = freq
        result = []
        for num in range(size):
            result.extend([num - offset] * buckets[num])
        return result