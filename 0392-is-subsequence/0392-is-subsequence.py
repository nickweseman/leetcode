class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        need = scan = 0

        while need < len(s) and scan < len(t):
            if s[need] == t[scan]:
                need += 1

            scan += 1
        return need == len(s)
            