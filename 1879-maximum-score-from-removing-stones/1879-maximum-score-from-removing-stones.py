class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        small, med, large = sorted([a, b, c])
        if small + med < large:
            return small + med
        else:
            return (small + med + large) // 2