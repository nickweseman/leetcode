class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        for i in range(min(n, k)):
            item = (matrix[i][0], i, 0)
            heapq.heappush(min_heap, item)

        for _ in range(k):
            kth_smallest, row, col = heapq.heappop(min_heap)
            col += 1
            if col < n:
                item = (matrix[row][col], row, col)
                heapq.heappush(min_heap, item)
        return kth_smallest