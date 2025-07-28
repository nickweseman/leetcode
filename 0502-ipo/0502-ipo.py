class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects_min_heap = []
        for c, p in zip(capital, profits):
            projects_min_heap.append((c, p))
        heapq.heapify(projects_min_heap)
        profits_max_heap = []
        for _ in range(k):
            while projects_min_heap and w >= projects_min_heap[0][0]:
                c, p = heapq.heappop(projects_min_heap)
                heapq.heappush(profits_max_heap, ((-p, c)))
            if not profits_max_heap:
                break
            neg_p, c = heapq.heappop(profits_max_heap)
            p = -neg_p
            print(p)
            w += p
        return w