class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        max_heap = [-a, -b, -c]
        heapq.heapify(max_heap)
        score = 0
        while len(max_heap) > 1:
            pile1 = -heapq.heappop(max_heap)
            pile2 = -heapq.heappop(max_heap)
            score += 1
            pile1 -= 1
            pile2 -= 1
            if pile1 > 0:
                heapq.heappush(max_heap, -pile1)
            if pile2 > 0:
                heapq.heappush(max_heap, -pile2)
        return score