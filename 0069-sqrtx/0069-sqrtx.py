class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x + 1
        while left < right:
            mid = (left + right) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        return left - 1