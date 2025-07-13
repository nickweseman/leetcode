class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        min_heap = []
        time = 0
        for num_passengers, start, end in trips:
            time = start
            while min_heap and min_heap[0][0] <= time:
                _, dropped_off_passengers = heapq.heappop(min_heap)
                capacity += dropped_off_passengers
            if num_passengers > capacity:
                return False
            capacity -= num_passengers
            heapq.heappush(min_heap, (end, num_passengers))
        return True