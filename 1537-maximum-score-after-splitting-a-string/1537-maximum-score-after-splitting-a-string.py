class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeroes = max_score = 0

        for char in s[:-1]:
            if char == "0":
                zeroes += 1
            else:
                ones -= 1
            max_score = max(max_score, ones + zeroes)
        return max_score

                
