class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = len(nums) + 1
        counter = collections.Counter(nums)
        buckets = [set() for _ in range(max_freq)]
        for num, freq in counter.items():
            buckets[freq].add(num)
        result = []
        for i in reversed(range(max_freq)):
            for item in buckets[i]:
                result.append(item)
                k -= 1
                if k == 0:
                    return result
        return result
