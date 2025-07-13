class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_passengers = [0] * 1_001
        for num_passengers, start, end in trips:
            curr_passengers[start] -= num_passengers
            curr_passengers[end] += num_passengers
        simulated_passengers = capacity
        for i in range(len(curr_passengers)):
            simulated_passengers += curr_passengers[i]
            if simulated_passengers < 0:
                return False
        return True