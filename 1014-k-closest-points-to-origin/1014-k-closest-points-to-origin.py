class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, point in enumerate(points):
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            item = (-distance, point)
            if len(heap) < k:
                heapq.heappush(heap, item)
            elif distance > heap[0][0]:
                heapq.heappushpop(heap, item)
        return [item[1] for item in heap]
