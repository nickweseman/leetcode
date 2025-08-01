class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        max_heap = []
        for freq in counts.values():
            max_heap.append(-freq)
        heapq.heapify(max_heap)
        cooldown_queue = collections.deque()
        time = 0
        while max_heap or cooldown_queue:
            while cooldown_queue and cooldown_queue[0][0] <= time:
                heapq.heappush(max_heap, -cooldown_queue.popleft()[1])
            if max_heap:
                freq = -heapq.heappop(max_heap)
                freq -= 1
                if freq > 0:
                    cooldown_queue.append((time + n + 1, freq))
            time += 1
        return time