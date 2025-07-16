class Solution:
    def frequencySort(self, s: str) -> str:
        result = []
        counter = collections.Counter(s)
        for letter, freq in counter.most_common():
            result.extend([letter] * freq)
        return "".join(result)