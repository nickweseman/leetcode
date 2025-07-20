class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        target_length = total // 4
        if total != target_length * 4:
            return False
        sides = [0] * 4
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        def backtrack(index):
            if index == n:
                return True
            for i in range(4):
                if sides[i] + matchsticks[index] <= target_length:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
            return False
        return backtrack(0)
