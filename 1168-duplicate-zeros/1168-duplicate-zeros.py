class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)

        for i in reversed(range(n)):
            if arr[i] == 0:
                if i + zeroes < n:
                    arr[i + zeroes] = arr[i]
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0
            else:
                if i + zeroes < n:
                    arr[i + zeroes] = arr[i]
        