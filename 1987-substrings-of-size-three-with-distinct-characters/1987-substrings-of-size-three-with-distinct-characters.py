class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good = 0
        for i in range(0, len(s) - 2):
            if len(set(s[i:i + 3])) == 3:
                good += 1
        return good