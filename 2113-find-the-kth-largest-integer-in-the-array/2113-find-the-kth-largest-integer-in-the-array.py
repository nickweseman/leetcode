class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        k_largest = heapq.nlargest(k, nums, key=int)
        return k_largest[-1]