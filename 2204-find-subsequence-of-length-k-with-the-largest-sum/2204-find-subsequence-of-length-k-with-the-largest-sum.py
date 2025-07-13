class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        result = []
        for i, num in enumerate(nums):
            max_heap.append((-num, i))
        heapq.heapify(max_heap)
        for _ in range(k):
            neg_num, i = heapq.heappop(max_heap)
            num = -neg_num
            result.append(i)
        result.sort()
        for i in range(len(result)):
            result[i] = nums[result[i]]
        return result