class Solution:
    def fillCups(self, amount: List[int]) -> int:
        small, medium, large = sorted(amount)
        if small + medium < large:
            return large
        else:
            return math.ceil((small + medium + large) / 2)