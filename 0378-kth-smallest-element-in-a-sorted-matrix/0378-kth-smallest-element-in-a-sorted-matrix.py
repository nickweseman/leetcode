class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        n = len(matrix)
        for i in range(min(k, n)):
            min_heap.append((matrix[i][0], i, 0))
        heapq.heapify(min_heap)
        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if j + 1 < n:
                heapq.heappush(min_heap, (matrix[i][j + 1], i, j + 1))
        return min_heap[0][0]