class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = 0
        half = len(arr) / 2
        counts = collections.Counter(arr)
        size = 0
        for i, freq in counts.most_common():
            size += freq
            count += 1
            if size >= half:
                return count
        return count