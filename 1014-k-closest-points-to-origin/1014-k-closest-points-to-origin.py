class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            min_heap.append((distance, point[0], point[1]))
        heapq.heapify(min_heap)
        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            result.append([x, y])
        return result