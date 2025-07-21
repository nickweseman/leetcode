class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(min(k, ROWS)):
            min_heap.append((matrix[r][0], r, 0))
        heapq.heapify(min_heap)
        for _ in range(k - 1):
            _, r, c = heapq.heappop(min_heap)
            if c + 1 < COLS:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        return min_heap[0][0]
