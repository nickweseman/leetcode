import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Create a range of numbers from 1 to n
        numbers = range(1, n + 1)
        
        # Use itertools.combinations to get all combinations of length k
        # and convert the resulting list of tuples to a list of lists.
        return list(itertools.combinations(numbers, k))