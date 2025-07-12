class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Create a timeline of all possible locations (0 to 1000).
        # The size is 1001 to include location 1000.
        timeline = [0] * 1_001
        # Record the change in passengers at each pickup and drop-off location.
        for num_passengers, start, end in trips:
            timeline[start] += num_passengers
            timeline[end] -= num_passengers
        # Iterate through the timeline to check the number of passengers at each point.
        current_passengers = 0
        for passenger_change in timeline:
            current_passengers += passenger_change
            if current_passengers > capacity:
                return False
        return True