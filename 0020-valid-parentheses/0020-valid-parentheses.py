class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {"(":")", "{":"}", "[":"]"}
        stack = []

        for char in s:
            if char in mappings:
                stack.append(char)
            else:
                if not stack:
                    return False
                ch = stack.pop()
                if ch not in mappings or mappings[ch] != char:
                    return False
        return len(stack) == 0