class Solution:
    def fillCups(self, amount: List[int]) -> int:
        small, med, large = sorted(amount)
        if small + med < large:
            return large
        else:
            return math.ceil((small + med + large) / 2)