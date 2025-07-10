class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = len(nums) + 1
        buckets = [[] for _ in range(max_freq)]
        counter = collections.Counter(nums)
        for i, freq in counter.items():
            buckets[freq].append(i)
        result = []
        for freq in reversed(range(max_freq)):
            for i in buckets[freq]:
                if k:
                    result.append(i)
                    k -= 1
        return result