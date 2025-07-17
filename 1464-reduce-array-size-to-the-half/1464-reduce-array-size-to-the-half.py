class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        max_freq = len(arr) + 1
        buckets = [0 for _ in range(max_freq)]
        for num, freq in counter.items():
            buckets[freq] += 1
        size = len(arr) // 2
        count = 0
        for i in reversed(range(max_freq)):
            for j in range(buckets[i]):
                size -= i
                count += 1
                if size <= 0:
                    return count
        return count


