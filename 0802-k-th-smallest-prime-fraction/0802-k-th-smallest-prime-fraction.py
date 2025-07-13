class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        start = n - k
        min_heap = []
        for j in range(max(1, start), n):
            min_heap.append((arr[0] / arr[j], 0, j))
        heapq.heapify(min_heap)
        while min_heap:
            _, i, j = heapq.heappop(min_heap)
            k -= 1
            if k == 0:
                return [arr[i], arr[j]]
            if i + 1 < j:
                heapq.heappush(min_heap, (arr[i + 1] / arr[j], i + 1, j))
        return result
