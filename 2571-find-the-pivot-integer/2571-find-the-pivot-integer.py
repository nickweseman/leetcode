class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum, right_sum = 0, n * (n+1) // 2
        for i in range(1,n + 1):
            right_sum -= i
            if left_sum == right_sum:
                return i
            left_sum += i
        return -1