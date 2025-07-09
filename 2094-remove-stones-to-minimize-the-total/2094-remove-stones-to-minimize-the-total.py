class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        for _ in range(k):
            pile = -heapq.heappop(piles)
            pile = math.ceil(pile / 2)
            if pile > 0:
                heapq.heappush(piles, -pile)
        return -sum(piles)