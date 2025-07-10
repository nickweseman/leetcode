class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_heap = []
        for i, row in enumerate(mat):
            left, right = 0, len(row)
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            item = (-left, -i)
            if len(max_heap) < k:
                heapq.heappush(max_heap, item)
            elif item > max_heap[0]:
                heapq.heappushpop(max_heap, item)
        max_heap.sort(reverse=True)
        return [-item[1] for item in max_heap]