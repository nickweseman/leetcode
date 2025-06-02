class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ss = list(s)
        for i in range(0, len(s), 2 * k):
            ss[i:i+k] = reversed(ss[i:i+k])
        return "".join(ss)
        