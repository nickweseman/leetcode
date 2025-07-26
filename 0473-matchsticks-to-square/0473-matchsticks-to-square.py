class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4
        n = len(matchsticks)
        sides = [0] * 4
        matchsticks.sort(reverse=True)
        def backtrack(index):
            if index == n:
                return True
            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                    if sides[i] == 0:
                        break
            return False
        return backtrack(0)