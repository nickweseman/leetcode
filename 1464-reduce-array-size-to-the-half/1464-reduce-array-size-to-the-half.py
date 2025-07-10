class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        max_freq = len(arr) + 1
        buckets = [0] * max_freq # it doesn't matter what the actual numbers in the bucket are
        for freq in counter.values():
            buckets[freq] += 1
        size = max_freq // 2
        count = 0
        for freq in reversed(range(max_freq)):
            for _ in range(buckets[freq]):
                size -= freq
                count += 1
                if size <= 0:
                    return count
        return 0