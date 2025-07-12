class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)
        time = 0
        cooldown_queue = collections.deque()
        while max_heap or cooldown_queue:
            time += 1
            if max_heap:
                count = -heapq.heappop(max_heap) - 1
                if count > 0:
                    cooldown_queue.append((count, time + n))
            if cooldown_queue and cooldown_queue[0][1] == time:
                count = cooldown_queue.popleft()[0]
                heapq.heappush(max_heap, -count)
        return time
            
