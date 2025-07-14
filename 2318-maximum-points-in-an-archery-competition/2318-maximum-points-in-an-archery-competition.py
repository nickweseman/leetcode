class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        bob_best_arrows = [0] * 12
        bob_current_arrows = [0] * 12
        max_score = -math.inf
        def dfs(i, arrows_left, current_score):
            nonlocal max_score, bob_best_arrows
            if i < 1:
                if current_score > max_score:
                    max_score = current_score
                    bob_current_arrows[0] = arrows_left # dump remaining arrows in 0 to spend them all
                    bob_best_arrows = bob_current_arrows.copy()
                return
            cost = aliceArrows[i] + 1
            if arrows_left >= cost:
                bob_current_arrows[i] = cost
                dfs(i - 1, arrows_left - cost, current_score + i)
                bob_current_arrows[i] = 0
            dfs(i - 1, arrows_left, current_score)
        dfs(11, numArrows, 0)
        return bob_best_arrows
        