class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for i, freq in counts.items():
            buckets[freq].append(i)
        result = []
        for i in reversed(range(len(buckets))):
            for j in buckets[i]:
                result.append(j)
                k -= 1
                if k == 0:
                    return result
        return result