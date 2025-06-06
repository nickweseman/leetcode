class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)

        for i in range(n-1,-1,-1):
            if arr[i] == 0:
                if zeroes + i < n:
                    arr[zeroes + i] = arr[i]
                zeroes -= 1
                if zeroes + i < n:
                    arr[zeroes + i] = 0
            elif zeroes + i < n:
                arr[zeroes + i] = arr[i]