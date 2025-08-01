class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "[":"]", "{":"}"}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            elif not stack or c != pairs[stack.pop()]:
                return False
        return len(stack) == 0
