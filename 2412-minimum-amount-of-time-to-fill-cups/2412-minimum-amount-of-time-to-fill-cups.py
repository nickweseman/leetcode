class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # Time needed if limited by the largest pile
        largest_pile = max(amount)
        
        # Time needed if limited by total cups (2 per second)
        total_cups = sum(amount)
        time_for_total = math.ceil(total_cups / 2)
        
        # The actual time is the maximum of these two constraints
        return int(max(largest_pile, time_for_total))