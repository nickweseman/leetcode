class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        ss = list(s)
        while left < right:
            if not ss[left].isalpha():
                left += 1
            elif not ss[right].isalpha():
                right -= 1
            else:
                ss[left], ss[right] = ss[right], ss[left]
                left += 1
                right -= 1
        return "".join(ss)