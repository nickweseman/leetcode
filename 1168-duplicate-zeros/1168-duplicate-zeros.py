class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeroes = arr.count(0)
        i = n - 1

        while i >= 0:
            if arr[i] == 0:
                if zeroes + i < n:
                    arr[zeroes + i] = arr[i]
                zeroes -= 1
                if zeroes + i < n:
                    arr[zeroes + i] = 0
            elif zeroes + i < n:
                arr[zeroes + i] = arr[i]
            i -= 1
        