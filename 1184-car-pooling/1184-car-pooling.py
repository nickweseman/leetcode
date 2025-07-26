class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1_001
        for num_passengers, start, end in trips:
            timeline[start] -= num_passengers
            timeline[end] += num_passengers
        for time in range(len(timeline)):
            capacity += timeline[time]
            if capacity < 0:
                return False
        return True