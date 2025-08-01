class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            digit = int(c)
            while stack and int(stack[-1]) > digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(c)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"