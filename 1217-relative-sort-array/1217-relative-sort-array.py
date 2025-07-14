class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        values = [0] * 1_001
        result = []
        for num in arr1:
            values[num] += 1
        for num in arr2:
            result.extend([num] * values[num])
            values[num] = 0
        for i, num in enumerate(values):
            if num:
                result.extend([i] * num)
        return result
