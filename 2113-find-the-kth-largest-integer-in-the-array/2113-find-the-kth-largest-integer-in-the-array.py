class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap = []
        for i in range(k):
            min_heap.append(int(nums[i]))
        heapq.heapify(min_heap)
        for num in nums[k:]:
            heapq.heappushpop(min_heap, int(num))
        return str(min_heap[0])