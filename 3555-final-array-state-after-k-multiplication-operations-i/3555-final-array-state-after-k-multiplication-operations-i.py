class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = []
        for i, num in enumerate(nums):
            min_heap.append((num, i))
        heapq.heapify(min_heap)
        for _ in range(k):
            val, i = heapq.heappop(min_heap)
            val *= multiplier
            nums[i] = val
            heapq.heappush(min_heap, (val, i))
        return nums