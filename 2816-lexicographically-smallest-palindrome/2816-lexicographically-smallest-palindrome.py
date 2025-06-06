class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left, right = 0, len(s) - 1
        ss = list(s)
        while left < right:
            if ss[left] < ss[right]:
                ss[right] = ss[left]
            else:
                ss[left] = ss[right]
            left += 1
            right -= 1
        return "".join(ss)