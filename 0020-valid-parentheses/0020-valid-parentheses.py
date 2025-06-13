class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mappings = {'(':')', '{':'}', '[':']'}

        for char in s:
            if char in mappings:
                stack.append(char)
            elif char in mappings.values():
                if stack:
                    c = stack.pop()
                else:
                    return False
                if mappings[c] != char:
                    return False
        return len(stack) == 0

        