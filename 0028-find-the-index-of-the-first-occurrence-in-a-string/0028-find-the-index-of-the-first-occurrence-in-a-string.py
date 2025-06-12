class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        scan = 0

        while scan < len(haystack):
            if needle == haystack[scan:scan+len(needle)]:
                return scan
            scan += 1
        return -1