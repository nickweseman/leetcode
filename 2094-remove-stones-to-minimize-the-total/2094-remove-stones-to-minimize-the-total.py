class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        while k > 0:
            pile = -heapq.heappop(piles)
            pile = math.ceil(pile / 2)
            heapq.heappush(piles, -pile)
            k -= 1
        return -sum(piles)