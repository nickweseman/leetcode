class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = collections.Counter(arr1)
        buckets = [0] * 1_001
        for i, freq in counts.items():
            buckets[i] = freq
        result = []
        for num in arr2:
            result.extend([num] * buckets[num])
            buckets[num] = 0
        for i in range(1_001):
            if buckets[i] > 0:
                result.extend([i] * buckets[i])
        return result