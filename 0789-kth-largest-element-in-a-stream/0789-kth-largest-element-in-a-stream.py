class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for i in range(len(nums)):
            if len(self.min_heap) < k:
                heapq.heappush(self.min_heap, nums[i])
            elif nums[i] > self.min_heap[0]:
                heapq.heappushpop(self.min_heap, nums[i])

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)