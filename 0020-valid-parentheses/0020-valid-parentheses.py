class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                    
                lastChar = stack.pop()
                if not ((lastChar == '(' and char == ')') or 
                    (lastChar == '[' and char == ']') or 
                    (lastChar == '{' and char == '}')):
                        return False
        if len(stack) == 0:
            return True
        else:
            return False