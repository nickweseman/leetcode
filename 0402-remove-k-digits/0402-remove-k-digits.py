class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        removals = k

        for digit in num:
            while stack and stack[-1] > digit and removals:
                stack.pop()
                removals -= 1
            stack.append(digit)
        
        while removals:
            stack.pop()
            removals -= 1
        
        s = "".join(stack).lstrip("0")
        
        return s if s else "0"
        