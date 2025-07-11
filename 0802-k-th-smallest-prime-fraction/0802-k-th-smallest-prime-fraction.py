class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []
        for j in range(1, len(arr)):
            min_heap.append((arr[0] / arr[j], 0, j)) # fraction, i, j
        heapq.heapify(min_heap)
        for _ in range(k - 1):
            val, i, j = heapq.heappop(min_heap)
            if i + 1 < j:
                heapq.heappush(min_heap, (arr[i + 1] / arr[j], i + 1, j))
        _, i, j = min_heap[0]
        return [arr[i], arr[j]]
