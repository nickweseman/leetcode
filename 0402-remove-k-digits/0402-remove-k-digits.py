class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and stack[-1] > digit and k:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        if k:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"