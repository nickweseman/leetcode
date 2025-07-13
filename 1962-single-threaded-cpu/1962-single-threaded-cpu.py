class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key = lambda x: x[0])
        time = 1
        i = 0
        min_heap = []
        result = []
        print(tasks)
        while len(result) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if min_heap:
                processing_time, index = heapq.heappop(min_heap)
                result.append(index)
                time += processing_time
            else:
                time = tasks[i][0]
        return result
