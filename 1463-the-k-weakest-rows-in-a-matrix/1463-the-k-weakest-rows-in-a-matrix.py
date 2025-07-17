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
            soldiers = left
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-soldiers, -i))
            else:
                heapq.heappushpop(max_heap, (-soldiers, -i))
        result = []
        for _ in range(k):
            _, neg_i = heapq.heappop(max_heap)
            i = -neg_i
            result.append(i)
        return result[::-1]
            

                