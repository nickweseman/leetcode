class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeros = arr.count(0)
        for i in reversed(range(n)):
            if arr[i] == 0:
                if i + zeros < n:
                    arr[i + zeros] = arr[i]
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
            else:
                if i + zeros < n:
                    arr[i + zeros] = arr[i]
        