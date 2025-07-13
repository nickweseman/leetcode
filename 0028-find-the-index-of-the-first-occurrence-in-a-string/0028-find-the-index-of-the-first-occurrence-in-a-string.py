class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        scan = 0
        while scan < len(haystack):
            if haystack[scan:scan+len(needle)] == needle:
                return scan
            scan += 1
        return -1