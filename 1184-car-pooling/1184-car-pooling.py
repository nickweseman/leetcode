class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        min_heap = []
        curr_passengers = 0
        for num_passengers, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                _, passengers_to_drop = heapq.heappop(min_heap)
                curr_passengers -= passengers_to_drop
            curr_passengers += num_passengers
            if curr_passengers > capacity:
                return False
            heapq.heappush(min_heap, (end, num_passengers))
        return True