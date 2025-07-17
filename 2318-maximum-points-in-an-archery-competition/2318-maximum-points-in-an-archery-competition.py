class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        best_bob_arrows = [0] * 12
        current_bob_arrows = [0] * 12
        max_score = 0
        def backtrack(index, arrows_left, score_so_far):
            nonlocal best_bob_arrows, max_score
            if index == 0 or arrows_left == 0:
                current_bob_arrows[0] = arrows_left
                if score_so_far > max_score:
                    max_score = score_so_far
                    best_bob_arrows = current_bob_arrows.copy()
                return
            if arrows_left < 0:
                return
            cost = aliceArrows[index] + 1
            if cost <= arrows_left:
                current_bob_arrows[index] = cost
                backtrack(index - 1, arrows_left - cost, score_so_far + index)
                current_bob_arrows[index] = 0
            backtrack(index - 1, arrows_left, score_so_far)
        backtrack(11, numArrows, 0)
        return best_bob_arrows