class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = []
        for i, num in enumerate(nums):
            min_heap.append((num, i))
        heapq.heapify(min_heap)
        for _ in range(k):
            val, i = heapq.heappop(min_heap)
            val *= multiplier
            heapq.heappush(min_heap, (val, i))
        min_heap.sort(key = lambda x: x[1])
        return [num for num, _ in min_heap]