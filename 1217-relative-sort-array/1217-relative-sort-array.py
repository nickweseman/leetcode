class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = [0] * 1001 # constraint says numbers are 0-1000
        for num in arr1:
            counts[num] += 1
        result = []
        for num in arr2:
            result.extend([num] * counts[num])
            counts[num] = 0
        for num in range(1001):
            if counts[num] > 0:
                result.extend([num] * counts[num])
        return result