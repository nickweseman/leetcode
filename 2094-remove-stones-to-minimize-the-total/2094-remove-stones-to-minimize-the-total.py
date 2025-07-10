class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        for i in range(len(piles)):
            max_heap.append(-piles[i])
        heapq.heapify(max_heap)
        for _ in range(k):
            stones = -heapq.heappop(max_heap)
            stones = math.ceil(stones / 2)
            heapq.heappush(max_heap, -stones)
        return sum(-stone for stone in max_heap)