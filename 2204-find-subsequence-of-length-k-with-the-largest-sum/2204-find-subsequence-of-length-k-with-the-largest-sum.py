class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        for i, num in enumerate(nums):
            if len(min_heap) < k:
                heapq.heappush(min_heap, (num, i))
            else:
                heapq.heappushpop(min_heap, (num, i))
        min_heap.sort(key = lambda x: x[1])
        return [num for num, i in min_heap]