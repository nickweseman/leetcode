class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        best_bob_arrows = []
        current_bob_arrows = [0] * 12
        max_score = -math.inf
        def backtrack(index, arrows_left, score):
            nonlocal max_score, best_bob_arrows
            if index == 0:
                if score > max_score:
                    max_score = score
                    if arrows_left:
                        current_bob_arrows[0] = arrows_left
                    best_bob_arrows = current_bob_arrows.copy()
                    current_bob_arrows[0] = 0
                return
            cost = aliceArrows[index] + 1
            if arrows_left >= cost:
                current_bob_arrows[index] = cost
                backtrack(index - 1, arrows_left - cost, score + index)
                current_bob_arrows[index] = 0
            backtrack(index - 1, arrows_left, score)
        backtrack(11, numArrows, 0)
        return best_bob_arrows