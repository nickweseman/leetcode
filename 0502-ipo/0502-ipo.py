class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        max_heap = []
        curr_project = 0
        for _ in range(k):
            while curr_project < len(projects) and projects[curr_project][0] <= w:
                heapq.heappush(max_heap, -projects[curr_project][1])
                curr_project += 1
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
        return w