class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = []
        for i, num in enumerate(nums):
            min_heap.append((num, i))
        heapq.heapify(min_heap)
        for _ in range(k):
            num, i = heapq.heappop(min_heap)
            num *= multiplier
            heapq.heappush(min_heap, (num, i))
        min_heap.sort(key = lambda x: x[1])
        return [x[0] for x in min_heap]