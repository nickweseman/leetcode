class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_heap = []
        for a in amount:
            if a > 0:
                max_heap.append(-a)
        heapq.heapify(max_heap)
        time = 0
        while len(max_heap) >= 2: # process 2 cups as long as you can
            cup1 = -heapq.heappop(max_heap)
            cup2 = -heapq.heappop(max_heap)
            cup1 -= 1
            cup2 -= 1
            if cup1 > 0:
                heapq.heappush(max_heap, -cup1)
            if cup2 > 0:
                heapq.heappush(max_heap, -cup2)
            time += 1
        if max_heap: # if you have 1 cup left, process it
            time += -max_heap[0]
        return time