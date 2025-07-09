class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        result = []
        for i in range(len(mat)):
            heapq.heappush(heap, (mat[i].count(1), i))
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result