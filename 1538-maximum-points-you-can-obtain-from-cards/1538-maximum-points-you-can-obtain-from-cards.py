class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum, right_sum = 0, sum(cardPoints[-k:])
        max_score = right_sum
        n = len(cardPoints)
        for i in range(k):
            left_sum += cardPoints[i]
            right_sum -= cardPoints[i - k]
            max_score = max(max_score, left_sum + right_sum)
        return max_score