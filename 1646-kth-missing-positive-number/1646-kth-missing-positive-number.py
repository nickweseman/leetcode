class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            num_missing = arr[mid] - (mid + 1)
            if num_missing < k:
                left = mid + 1
            else:
                right = mid
        return left + k
            