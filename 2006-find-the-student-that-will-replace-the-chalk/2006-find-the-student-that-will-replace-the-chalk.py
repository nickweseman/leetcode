class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        i = 0
        while k >= 0:
            if k >= chalk[i]:
                k -= chalk[i]
                i += 1
            else:
                return i
