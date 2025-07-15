class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        MIN_VAL = -50_000
        MAX_VAL = 50_000
        buckets = [0] * (100_000 + 1)
        offset = -MIN_VAL
        for i, num in enumerate(nums):
            buckets[num + offset] += 1
        result = []
        for i in range(len(buckets)):
            if buckets[i]:
                result.extend(buckets[i] * [i - offset])
        return result