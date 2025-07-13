class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profit_max_heap = []
        project_min_heap = list(zip(capital, profits))
        heapq.heapify(project_min_heap)
        for _ in range(k):
            while project_min_heap and project_min_heap[0][0] <= w:
                _, profit = heapq.heappop(project_min_heap)
                heapq.heappush(profit_max_heap, -profit)
            if not profit_max_heap:
                break
            w += -heapq.heappop(profit_max_heap)
        return w
            