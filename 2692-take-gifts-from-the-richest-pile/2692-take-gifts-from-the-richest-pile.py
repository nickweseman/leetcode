class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        for gift in gifts:
            max_heap.append(-gift)
        heapq.heapify(max_heap)
        for _ in range(k):
            pile = -heapq.heappop(max_heap)
            pile = math.floor(pile ** .5)
            heapq.heappush(max_heap, -pile)
        return -sum(max_heap)