class Solution:
    def maxScore(self, s: str) -> int:
        zeroes = 0
        ones = s.count("1")
        max_score = 0

        for char in s[:-1]:
            if char == "0":
                zeroes += 1
            else:
                ones -= 1
            max_score = max(max_score, zeroes + ones)
        return max_score
