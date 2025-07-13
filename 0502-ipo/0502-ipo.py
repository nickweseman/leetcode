class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project_min_heap = []
        profit_max_heap = []
        n = len(capital)
        for i in range(n):
            project_min_heap.append((capital[i], profits[i]))
        heapq.heapify(project_min_heap)
        for _ in range(k):
            while project_min_heap and project_min_heap[0][0] <= w:
                needed_capital, profit = heapq.heappop(project_min_heap)
                heapq.heappush(profit_max_heap, -profit)
            if not profit_max_heap:
                break
            w += -heapq.heappop(profit_max_heap)
        return w
            