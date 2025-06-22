class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n + 1
        
        while left < right:
            mid = (left + right) // 2
            
            coins_needed = (mid * (mid + 1)) // 2

            if coins_needed <= n:
                left = mid + 1
            else:
                right = mid
        return left-1