class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check_le(mid) -> int:
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += (row + 1)
                    col += 1
                else:
                    row -= 1
            return count
        low, high = matrix[0][0], matrix[n-1][n-1]
        while low < high:
            mid = (low + high) // 2
            count = check_le(mid)
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low