class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum, right_sum = 0, sum(cardPoints[-k:])
        score = max_score = right_sum

        for i in range(k):
            right_sum -= cardPoints[-(k-i)]
            left_sum += cardPoints[i]
            max_score = max(max_score, left_sum + right_sum)
        return max_score