class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sides = [0] * 4
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        length = total // 4
        n = len(matchsticks)
        matchsticks.reverse()
        def backtrack(index):
            if index == n:
                return True
            for i in range(4):
                if sides[i] + matchsticks[index] <= length:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index] 
                    if sides[i] == 0:
                        break
            return False
        return backtrack(0)