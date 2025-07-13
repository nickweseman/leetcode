class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-distance, point[0], point[1]))
            else:
                heapq.heappushpop(max_heap, (-distance, point[0], point[1]))
        result = []
        while max_heap:
            _, x, y = heapq.heappop(max_heap)
            result.append([x, y])
        return result