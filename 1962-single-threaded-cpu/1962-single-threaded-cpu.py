class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_min_heap = []
        for i, task in enumerate(tasks):
            start_time, p_time = task
            tasks_min_heap.append((start_time, i, p_time))
        heapq.heapify(tasks_min_heap)
        waiting_min_heap = []
        result = []
        time = 1
        while tasks_min_heap or waiting_min_heap:
            while tasks_min_heap and tasks_min_heap[0][0] <= time:
                _, i, p_time = heapq.heappop(tasks_min_heap)
                heapq.heappush(waiting_min_heap, (p_time, i))
            if waiting_min_heap:
                p_time, i = heapq.heappop(waiting_min_heap)
                result.append(i)
                time += p_time
            else:
                time = tasks_min_heap[0][0]
        return result