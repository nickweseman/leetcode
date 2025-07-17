class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        end = min(k, len(nums2))
        for j in range(end):
            min_heap.append((nums1[0] + nums2[j], 0, j))
        heapq.heapify(min_heap)
        result = []
        for _ in range(k):
            _, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
        return result
