class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        max_freq = len(s) + 1
        buckets = [[] for _ in range(max_freq)]
        for c, freq in counter.items():
            buckets[freq].append(c)
        result = []
        for freq in reversed(range(max_freq)):
            for c in buckets[freq]:
                result.append(c * freq)
        return "".join(result)
