class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
        for i in range(len(mat)):
            left, right = 0, len(mat[i])
            while left < right:
                mid = (left + right) // 2
                if mat[i][mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            min_heap.append((left, i))
        heapq.heapify(min_heap)
        result = []
        for _ in range(k):
            _, i = heapq.heappop(min_heap)
            result.append(i)
        return result