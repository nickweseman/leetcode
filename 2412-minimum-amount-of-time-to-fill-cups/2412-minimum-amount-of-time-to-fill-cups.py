class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_heap = []
        for i in range(len(amount)):
            if amount[i] > 0:
                max_heap.append(-amount[i])
        heapq.heapify(max_heap)
        time = 0
        while len(max_heap) > 1:
            cup1 = -heapq.heappop(max_heap)
            cup2 = -heapq.heappop(max_heap)
            cup1 -= 1
            cup2 -= 1
            time += 1
            if cup1 > 0:
                heapq.heappush(max_heap, -cup1)
            if cup2 > 0:
                heapq.heappush(max_heap, -cup2)
        if max_heap:
            time += -heapq.heappop(max_heap)
        return time