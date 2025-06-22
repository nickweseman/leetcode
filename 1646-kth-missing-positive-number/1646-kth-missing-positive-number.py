class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            missing_numbers = arr[mid] - (mid + 1)
            if missing_numbers < k:
                left = mid + 1
            else:
                right = mid
        return left + k