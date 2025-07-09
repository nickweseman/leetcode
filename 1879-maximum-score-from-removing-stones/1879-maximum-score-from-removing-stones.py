class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapq.heapify(heap)
        score = 0
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone1 -= 1
            stone2 = -heapq.heappop(heap)
            stone2 -= 1
            if stone1 != 0:
                heapq.heappush(heap, -stone1)
            if stone2 != 0:
                heapq.heappush(heap, -stone2)
            score += 1
        return score
            
        