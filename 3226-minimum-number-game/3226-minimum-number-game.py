class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        result = []
        while nums:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            result.append(bob)
            result.append(alice)
        return result
