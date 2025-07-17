class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_heap = []
        for freq in counter.values():
            max_heap.append(-freq)
        heapq.heapify(max_heap)
        cooldown_queue = collections.deque()
        time = 0
        while max_heap or cooldown_queue:
            time += 1
            while cooldown_queue and cooldown_queue[0][0] < time:
                _, freq = cooldown_queue.popleft()
                heapq.heappush(max_heap, -freq)
            if max_heap:
                freq = -heapq.heappop(max_heap)
                freq -= 1
                if freq > 0:
                    cooldown_queue.append((time + n, freq))
        return time
