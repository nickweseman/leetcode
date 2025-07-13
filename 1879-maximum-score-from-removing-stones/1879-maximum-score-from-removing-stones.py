class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        score = 0
        max_heap = []
        if a > 0:
            max_heap.append(-a)
        if b > 0:
            max_heap.append(-b)
        if c > 0:
            max_heap.append(-c)
        heapq.heapify(max_heap)
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