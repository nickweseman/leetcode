class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = right = 0
        while right < len(haystack):
            if right - left + 1 > len(needle):
                left += 1
            if right - left + 1 == len(needle) and haystack[left:left+len(needle)] == needle:
                return left
            right += 1
        return -1