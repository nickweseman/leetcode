class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * 1_001
        for num_passengers, start, end in trips:
            passengers[start] -= num_passengers
            passengers[end] += num_passengers
        for i, num in enumerate(passengers):
            capacity += num
            if capacity < 0:
                return False
        return True