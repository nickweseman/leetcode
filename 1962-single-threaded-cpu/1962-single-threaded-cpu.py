class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = []
        # New format: (enqueueTime, processingTime, originalIndex)
        for i, task in enumerate(tasks):
            indexed_tasks.append((task[0], task[1], i))
        indexed_tasks.sort()
        result = []
        min_heap = []
        current_task = 0
        time = 0
        n = len(tasks)
        while len(result) < n:
            while current_task < n and indexed_tasks[current_task][0] <= time:
                _, process_time, i = indexed_tasks[current_task]
                heapq.heappush(min_heap, (process_time, i))
                current_task += 1
            if min_heap:
                process_time, i = heapq.heappop(min_heap)
                result.append(i)
                time += process_time
            else:
                time = indexed_tasks[current_task][0]
        return result