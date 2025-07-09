class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        for row in range(min(k,n)):
            heapq.heappush(min_heap, (matrix[row][0], row, 0))
        
        kth_smallest = -1
        for _ in range(k):
            kth_smallest, row, col = heapq.heappop(min_heap)

            if col + 1 < n:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
        return kth_smallest