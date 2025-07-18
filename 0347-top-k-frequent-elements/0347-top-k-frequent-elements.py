class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for i, freq in counter.items():
            buckets[freq].append(i)
        result = []
        for freq in reversed(range(len(nums) + 1)):
            for i in buckets[freq]:
                k -= 1
                result.append(i)
                if k == 0:
                    return result
        return result
