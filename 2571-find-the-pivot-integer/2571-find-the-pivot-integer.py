class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0
        right_sum = grand_sum = n * (n+1) // 2
        
        for i in range(1, n + 1):
            right_sum = grand_sum - left_sum
            left_sum += i
            if left_sum == right_sum:
                return i
        return -1

