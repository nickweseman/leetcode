class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        size = 1_000 + 1
        buckets = [0] * size
        for num in arr1:
            buckets[num] += 1
        result = []
        for num in arr2:
            result.extend([num] * buckets[num])
            buckets[num] = 0
        for i, freq in enumerate(buckets):
            if freq:
                result.extend([i] * freq)
        return result
