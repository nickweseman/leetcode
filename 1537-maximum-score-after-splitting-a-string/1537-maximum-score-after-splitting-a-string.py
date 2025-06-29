class Solution:
    def maxScore(self, s: str) -> int:
        left_sum, right_sum = 0, s.count("1")
        max_score = 0

        for c in s[:-1]:
            if c == "1":
                right_sum -= 1
            else:
                left_sum += 1
            max_score = max(max_score, left_sum + right_sum)
        return max_score