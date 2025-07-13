class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project_min_heap = []
        profit_max_heap = []
        n = len(capital)
        num_projects = 0
        for i in range(n):
            project_min_heap.append((capital[i], profits[i]))
        heapq.heapify(project_min_heap)
        while project_min_heap or profit_max_heap:
            while project_min_heap and project_min_heap[0][0] <= w:
                needed_capital, profit = heapq.heappop(project_min_heap)
                heapq.heappush(profit_max_heap, -profit)
            if not profit_max_heap:
                break
            w += -heapq.heappop(profit_max_heap)
            num_projects += 1
            if num_projects == k:
                break
        return w
            