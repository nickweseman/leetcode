class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        max_freq = len(nums) + 1
        buckets = [[] for _ in range(max_freq)]
        for num, freq in counter.items():
            buckets[freq].append(num)
        result = []
        for freq in reversed(range(max_freq)):
            for num in buckets[freq]:
                k -= 1
                result.append(num)
                if k == 0:
                    return result
        return result
