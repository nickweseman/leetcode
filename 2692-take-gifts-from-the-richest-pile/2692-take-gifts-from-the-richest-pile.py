class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        for gift in gifts:
            max_heap.append(-gift)
        heapq.heapify(max_heap)
        for _ in range(k):
            num = -heapq.heappop(max_heap)
            num = math.floor(math.sqrt(num))
            heapq.heappush(max_heap, -num)
        return -sum(max_heap)