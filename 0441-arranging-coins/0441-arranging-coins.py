class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n + 1
        while left < right:
            mid = (left + right) // 2
            num_coins = mid * (mid + 1) // 2
            if num_coins <= n:
                left = mid + 1
            else:
                right = mid
        return left - 1