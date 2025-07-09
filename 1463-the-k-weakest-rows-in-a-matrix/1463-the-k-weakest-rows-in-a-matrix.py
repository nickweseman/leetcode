class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        result = []
        for i, row in enumerate(mat):
            left, right = 0, len(row)
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            item = (-left, -i)
            if len(heap) < k:
                heapq.heappush(heap, item)
            elif item > heap[0]:
                heapq.heappushpop(heap, item)
        heap.sort(reverse=True)
        return [-item[1] for item in heap]

            
                