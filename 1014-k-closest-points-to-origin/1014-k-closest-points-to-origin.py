class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i, point in enumerate(points):
            distance = point[0] ** 2 + point[1] ** 2
            item = (-distance, point[0], point[1])
            if len(max_heap) < k:
                heapq.heappush(max_heap, item)
            elif item > max_heap[0]:
                heapq.heappushpop(max_heap, item)
        return [[item[1], item[2]] for item in max_heap]
