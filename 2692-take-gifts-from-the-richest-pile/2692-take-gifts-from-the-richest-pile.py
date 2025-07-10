class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)
        for _ in range(k):
            gift = -heapq.heappop(gifts)
            gift = math.floor(math.sqrt(gift))
            heapq.heappush(gifts, -gift)
        return sum(-gift for gift in gifts)