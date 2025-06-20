class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {"(":")", "{":"}", "[":"]"}
        stack = []

        for char in s:
            if char in mappings:
                stack.append(char)
            else:
                if not stack or mappings[stack.pop()] != char:
                    return False
        return len(stack) == 0