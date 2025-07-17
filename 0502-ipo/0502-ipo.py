class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects_min_heap = []
        for capital, profit in zip(capital, profits):
            projects_min_heap.append((capital, profit))
        heapq.heapify(projects_min_heap)
        profits_max_heap = []
        while k:
            while projects_min_heap and projects_min_heap[0][0] <= w:
                _, profit = heapq.heappop(projects_min_heap)
                heapq.heappush(profits_max_heap, -profit)
            if not profits_max_heap:
                break
            profit = -heapq.heappop(profits_max_heap)
            w += profit
            k -= 1
        return w

            
