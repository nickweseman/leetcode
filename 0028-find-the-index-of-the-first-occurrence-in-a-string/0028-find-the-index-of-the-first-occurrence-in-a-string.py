class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        left, right = 0, n - 1

        while right < len(haystack):
            if haystack[left:right+1] == needle:
                return left
            left += 1
            right += 1
        return -1
        