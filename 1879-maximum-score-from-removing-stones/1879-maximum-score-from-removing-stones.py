class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        small, medium, large = sorted([a, b, c])
        if large >= small + medium:
            return small + medium
        else:
            return (small + medium + large) // 2
    