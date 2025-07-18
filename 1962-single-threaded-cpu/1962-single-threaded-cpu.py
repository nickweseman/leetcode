class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_min_heap = []
        for i, task in enumerate(tasks):
            start_time, processing_time = task
            heapq.heappush(tasks_min_heap, (start_time, i, processing_time))
        heapq.heapify(tasks_min_heap)
        processing_min_heap = []
        time = 1
        result = []
        while tasks_min_heap or processing_min_heap:
            while tasks_min_heap and tasks_min_heap[0][0] <= time:
                _, i, processing_time = heapq.heappop(tasks_min_heap)
                heapq.heappush(processing_min_heap, (processing_time, i))
            if processing_min_heap:
                processing_time, i = heapq.heappop(processing_min_heap)
                time += processing_time
                result.append(i)
            else:
                time = tasks_min_heap[0][0]
        return result
            

