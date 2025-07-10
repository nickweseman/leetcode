class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        max_freq = len(s) + 1
        buckets = [[] for _ in range(max_freq)]
        for c, freq in counts.items():
            buckets[freq].append(c)
        result = []
        for freq in reversed(range(max_freq)):
            for char in buckets[freq]:
                result.append(char * freq)
        return "".join(result)